from .schemas import Item
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = Query(None, title="Query Parameter Example")):
    return {"item_id": item_id, "query_param": query_param}

@app.post("/items/")
def create_item(item: Item):
    return item.dict()