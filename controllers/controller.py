import re
from flask import render_template
from app import app
from order.create_order import orders


@app.route('/orders')
def order_placer():
    return render_template('index.html', title='order', orders=orders)

@app.route('/orders/index')
def order_retriveser():
    return render_template('order.html', title='order', orders=orders)

