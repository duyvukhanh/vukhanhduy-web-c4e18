from flask import *
import mlab
from models.service import Service, User, Order
from mongoengine import *
from datetime import datetime
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = "linhcute"
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
    if "loggedin" in session:
        service = Service.objects.with_id(service_id)
        return render_template('service_detail.html',service=service)
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if "loggedin" in session:
        all_service = Service.objects()
        return render_template('admin.html',all_service = all_service)
    else:
        return redirect(url_for('login'))

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

@app.route('/sign-up', methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        form = request.form
        new_user = User(
            name = form['name'],
            email = form['email'],
            username = form['username'],
            password = form['password'],   
        )
        new_user.save()
        return('Saved')

@app.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        #query from database
        users = User.objects()
        for user in users:
            if username == user.username:
                if password == user.password:
                    session['loggedin'] = True
                    session['useremail'] = user.email
                    

                    return redirect(url_for('search'))
                else:
                    return "Wrong Pass"
            else:
                return "User Not Found"

@app.route('/logout')
def logout():
    del session['loggedin']
    del session['useremail']
    
    return redirect(url_for('login'))



@app.route('/order/<service_id>')
def orderr(service_id):
    order_service = Service.objects().with_id(service_id)
    new_order = Order(
        serviceid = service_id,
        servicename = order_service.name,
        email = session['useremail'],
        userid = "Cái này khó quá",
        time = datetime.now(),
        is_accepted = False
    )    
    new_order.save()
    return 'Sent'

@app.route('/ordermanagement')
def ordermanagement():
    all_orders = Order.objects()
    return render_template('orderpage.html',all_orders = all_orders)

@app.route('/accept/<order_id>')
def accept(order_id):
    order = Order.objects().with_id(order_id)
    order.update(set__is_accepted = True)
    order.reload()
    gmail = GMail('duyvukhanhc4e@gmail.com','vukhanhduy')
    mess="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh"
    msg = Message('Hello',to=order.email,html=mess)
    gmail.send(msg)
    return redirect(url_for('ordermanagement'))

if __name__ == '__main__':
  app.run(debug=True) 
 