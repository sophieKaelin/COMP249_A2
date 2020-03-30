"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json

import model
import dbschema

COOKIE_NAME = 'session'


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    # Check if there is a cookie.
    key = request.get_cookie(COOKIE_NAME)

    # Check if the cookie exists in the dataBase.
    cur = db.cursor()
    cur.execute(
        """
            SELECT sessionid 
            FROM sessions 
            WHERE sessionid = (?);
        """, (key,))

    dbCookie = cur.fetchone()

    # If there is no cookie in the database, create one and add to the database.
    if dbCookie == None:
        key = str(uuid.uuid4())
        cur.execute("INSERT INTO sessions (sessionid) VALUES (?);", (key,))
        db.commit()
        response.set_cookie(COOKIE_NAME, key, path="/")

    return key


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    sessionID = get_or_create_session(db)

    item = itemid.model.product_get
    # cur = db.cursor
    #
    # cur.execute()
    # Create JSON String with the item details
    # Add/update the string "data" in the sessions table for the corresponding sessionID



def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """


