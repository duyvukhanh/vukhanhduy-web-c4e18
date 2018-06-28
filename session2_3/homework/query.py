from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b30ca9d70618c5f58922d9d"
search = Service.objects().with_id(id_to_find)

print(search.to_mongo())