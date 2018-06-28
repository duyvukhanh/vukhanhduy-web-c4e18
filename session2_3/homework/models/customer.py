from mongoengine import *

#1. design database
class Customer(Document):
  name = StringField()
  yob = IntField()
  gender = IntField()
  company = StringField()
  email = StringField()
  phone = StringField()
  address = StringField()
  contact = BooleanField()

