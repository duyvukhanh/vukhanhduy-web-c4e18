from models.service import Service
import mlab
from faker import Faker
from random import *
mlab.connect()

fake = Faker()



new_service = Service(
    name = "Linh MU",
    yob = 1995,
    gender = 0,
    height = randint(155,190),
    description = sample(["Yeu To Quoc","Yeu Dong Bao","Hoc Tap Tot","Lao Dong Tot","Giu Ve Sinh Tot","Khiem Ton","That Tha","Dung Cam"],3),
    measurement = sample(range(60,100,1),3),      
    phone = fake.phone_number(),
    address = fake.address(),
    status = choice([True,False]),
    img = "../static/image/TuLinh.jpg"
)

new_service.save()