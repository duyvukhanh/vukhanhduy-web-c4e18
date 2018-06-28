from models.river import River
import mlab7

mlab7.connect()

SA_river = River.objects(continent = "S. America")

for river in SA_river:
    if river["length"] <= 1000:
        print(river["name"])
        print("- "*10)