from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# FastAPI handles JSONifying all of our information so we can work with strictly python types in our API


# @app.get("/")
# def home():
#     return {"Data": "Testing"}


# @app.get("/about")
# def about():
#     return {"Data": "About"}

inventory = {}

# multiple path parameters


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="the ID of the item you wish to view", gt=0)):
    return inventory[item_id]
    # None in Path is the default value


# Query Parameters

@app.get("/get-by-name")
def get_item(test: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
# http://127.0.0.1:8000/get-by-name?test=2&name=Milk

# Combing query and path parameters


@app.get("/get-by-name-c/{item_id}")
def get_item(item_id: int, test: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
# http://127.0.0.1:8000/get-by-name-c/1/?test=2&name=Milk


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist."}

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete("/delete-item/")
def delete_item(item_id: int = Query(..., description="The ID of the item to be deleted", gte=0)):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    del inventory[item_id]
    return {"Success": "Item deleted"}
