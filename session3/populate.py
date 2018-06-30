from models.service import Service
import mlab
from faker import Faker
from random import *
mlab.connect()

fake = Faker()



new_service = Service(
    name = "Emma",
    yob = 1995,
    gender = 0,
    height = randint(155,190),
    description = choice(["Yeu To Quoc","Yeu Dong Bao","Hoc Tap Tot","Lao Dong Tot","Giu Ve Sinh Tot","Khiem Ton","That Tha","Dung Cam"]),
    measurement = choice(["60,90,60","90,90,90","61,91,61"]),      
    phone = fake.phone_number(),
    address = fake.address(),
    status = choice([True,False]),
    img = "../static/image/Emma.jpg"
)

new_service.save()