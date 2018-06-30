from mongoengine import *

#1. design database
class Service(Document):
  name = StringField()
  yob = IntField()
  gender = IntField()
  height = IntField()
  phone = StringField()
  address = StringField()
  status = BooleanField()
  description = StringField()
  measurement = StringField()
  img = StringField()

class User(Document):
  name = StringField()
  email = StringField()
  username = StringField()
  password = StringField()
  status = BooleanField()

class Order(Document):
  serviceid = StringField()
  servicename = StringField()
  userid = StringField()
  time = DateTimeField()
  is_accepted = BooleanField()
  email = StringField()
