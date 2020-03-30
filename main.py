
import random
from bottle import Bottle, template, static_file, request, redirect, HTTPError

import model
import session

app = Bottle()


@app.route('/')
def index(db):
    session.get_or_create_session(db)

    info = {
        'title': "The WT Store",
        'products': model.product_list(db),
    }

    return template('index', info)

@app.route('/product/<id>')
def productpage(db, id):
    session.get_or_create_session(db)
    info = {
        'product': model.product_get(db, id),
    }

    return template('product', info)

@app.route('/cart')
def cart(db):
    session.get_or_create_session(db)

    info = {
        'contents': session.get_cart_contents(db),
    }
    return template('cart', info)

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')

if __name__ == '__main__':

    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
