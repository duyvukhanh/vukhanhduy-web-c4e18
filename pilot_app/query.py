from models.service import Service, User
import mlab

mlab.connect()



user = User.objects(username = "duyvukhanh")
print(user.email)