import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    order_id: int
    product_id: int
    quantity: int

orders_db = []

@app.post("/order")
def create_order(order: Order):
    product = requests.get(f"http://localhost:8002/product/{order.product_id}").json()
    
    if product["stock"] < order.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    product["stock"] = order.quantity
    x = requests.post("http://localhost:8002/product/order", json = product)    
    orders_db.append(order)
    return {"message": "Order created successfully"}

@app.get("/order")
def get_order():
    return orders_db

@app.get("/order/{order_id}")
def get_order(order_id: int):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]