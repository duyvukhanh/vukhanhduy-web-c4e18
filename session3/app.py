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

@app.route('/search')
def search():
    all_service = Service.objects()     
    return render_template('search.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('service_detail.html',service=service)

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
    new_service = Service(
        name = form['name'],
        yob = form['yob'],
        phone = form['phone'],
        gender = form['gender'],        
        address = form['address'],
        height = form['height'],
    )
    new_service.save()
    return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ["GET","POST"])
def update(service_id):
  if request.method == "GET":
      service = Service.objects().with_id(service_id)
      return render_template('update.html', service = service)
  else:
      form = request.form
      service = Service.objects().with_id(service_id)
      service.update(
          set__name = form['name'],
          set__yob = form['yob'],
          set__address = form['address'],
          set__gender = form['gender'],
          set__phone = form['phone'],
          set__height = form['height'],
          set__description = form['description'],
          set__measurement = form['measurement']
      )
      service.reload()
      return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True) 
 