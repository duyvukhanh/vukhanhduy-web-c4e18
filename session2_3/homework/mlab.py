import mongoengine
 
# mongodb://admin:admin123@ds217671.mlab.com:17671/muadongkhonglanh-c4e18

host = "ds217671.mlab.com"
port = 17671
db_name = "muadongkhonglanh-c4e18"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())