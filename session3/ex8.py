from models.river import River
import mlab7

mlab7.connect()

Africa_river = River.objects(continent = "Africa")

for river in Africa_river:
    print(river["name"])
    print(river["length"])
    print("- "*10)