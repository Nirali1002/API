# database.py

from models import Item

fake_db = []

def get_item(item_id: int):
    return next((item for item in fake_db if item.id == item_id), None)

def create_item(item: Item):
    fake_db.append(item)
    return item

def update_item(item_id: int, data: dict):
    item = get_item(item_id)
    if item:
        item.name = data['name']
        item.description = data['description']
        item.price = data['price']
    return item

def delete_item(item_id: int):
    global fake_db
    fake_db = [item for item in fake_db if item.id != item_id]
