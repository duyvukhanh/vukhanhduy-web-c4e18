from flask import *
import mlab
from models.service import Service
from mongoengine import *

app = Flask(__name__)

# create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
  all_service = Service.objects(gender=gender)
  return render_template('search.html',all_service=all_service)

@app.route('/admin')
def admin():
  all_service = Service.objects()
  return render_template('admin.html',all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
  service_to_delete = Service.objects().with_id(service_id)
  if service_to_delete is None:
    return "Service not found"
  else:
    service_to_delete.delete()
    return redirect(url_for('admin'))

@app.route('/new-service', methods = ["GET","POST"])
def create():
  if request.method == "GET":
    return render_template('new_service.html')
  elif request.method == "POST":
    form = request.form
    name = form["name"]
    yob = form["yob"]
    address = form["address"]
    return name + yob + address

if __name__ == '__main__':
  app.run(debug=True) 
 