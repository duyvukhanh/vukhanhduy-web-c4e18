from flask import Flask, render_template
import mlab
from models.customer import Customer
from mongoengine import *

app = Flask(__name__)

# create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    all_customer = Customer.objects()
    return render_template('search.html',all_customer=all_customer)

@app.route('/customer10')
def customer10():
  all_customer = Customer.objects(gender = 0,contact = False)[:10]
  return render_template('search.html',all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True) 
 