from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

products_db = {}

@app.post("/product")
def create_product(productIn: Product):
    if productIn.id in products_db:
        product = products_db[productIn.id]
        product.stock = productIn.stock
        product.price = productIn.price
        productIn = product
    products_db[productIn.id] = productIn
    return {"message": "Product created/updated successfully"}

@app.get("/product/{id}")
def get_product(id: int):
    if id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[id] 

@app.post("/product/order")
def order_product(productIn: Product):

    print("/product/product_id " + str(productIn.id)) 
    if productIn.id in products_db:
        product = products_db[productIn.id]
        print("Stock Quantity " + str(product.stock) + " " + str(productIn.stock))
        product.stock = product.stock - productIn.stock
        products_db[productIn.id] = product
    return {"message": "Product stock updated."}