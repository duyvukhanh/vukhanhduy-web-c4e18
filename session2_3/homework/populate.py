from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()

for i in range(50):

    print(i+1)

    new_customer = Customer(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        company = fake.company(),
        email = fake.email(),
        phone = fake.phone_number(),
        address = fake.address(),
        contact = choice([True,False])
    )

    new_customer.save()