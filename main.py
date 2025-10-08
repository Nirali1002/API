# main.py

from fastapi import FastAPI, HTTPException
from schemas import ItemCreate, ItemResponse
from models import Item
import database

app = FastAPI(title="Product API", version="1.0")

# Auto-increment ID counter
counter = 1

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Product API"}

@app.post("/items/", response_model=ItemResponse, tags=["Items"])
def create_item(item: ItemCreate):
    global counter
    new_item = Item(id=counter, **item.dict())
    counter += 1
    return database.create_item(new_item)

@app.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def read_item(item_id: int):
    item = database.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def update_item(item_id: int, item_data: ItemCreate):
    item = database.update_item(item_id, item_data.dict())
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int):
    item = database.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    database.delete_item(item_id)
    return {"message": f"Item {item_id} deleted successfully"}
