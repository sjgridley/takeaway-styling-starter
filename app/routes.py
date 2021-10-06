from flask import render_template

from app import app
from app.models import Item

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/menu')
def menu():
    items = Item.query.all()
    return render_template('menu.html', title = 'Menu', items = items)

@app.route('/orders')
def orders():
    return render_template('orders.html', title = 'Orders')