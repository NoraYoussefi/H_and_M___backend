from typing import List
from unicodedata import category
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models.baseModel import ProductModel
from models.productModel import Product, ProductUpdateRequest,category
# from mongoengine import connect
from database import *
from routers.product import router_products
from routers import product
from models.productModel import Product
from models import productModel



app = FastAPI(title='product.ly', description='APIs for product Apis')
app.include_router(product.router_products)
# --------------------mysql database ----------------------------------------


@app.on_event("startup")
async def startup():
    if conn.is_closed():
        conn.connect()

@app.on_event("shutdown")
async def shutdown():
    print("Closing...")
    if not conn.is_closed():
        conn.close()

#---------------------- mongodb connection-----------------------
# connect(db="H_and_M", host="localhost", port=3306)

# --------------------local database------------------
# db: List[Product] = [
#     Product(
#         id=uuid4(),
#         name="tshirt",
#         category=category.male
#         ),
#      Product(
#         id=uuid4(),
#         name="sebat",
#         category=category.female
#         )
# ]

@app.get("/")
async def root():
    return {"hillooo" : "H & M"}

# @app.get("/products")
# async def fetch_products():
#     products=Product.objects().to_json()
#     print(products)
#     return {"products": products}

# 
# async def save_products(name: str,category: str):
@router_products.post("/", response_model=productModel, summary="Create a new contact")
async def create(name: str, category: str):
    return await create_product(name=name, category=category)

# @app.post("/save")
# async def save_products(product: Product):
#     db.append(product)
#     return {"id": product.id, "name": product.name};

# @app.delete("/delete/{product_id}")
# async def delete_product(product_id: UUID):
#     for product in db:
#         if(product.id == product_id):
#             db.remove(product)
#             return
#     raise HTTPException(
#         status_code=404,
#         detail=f"Product with id: {product_id} not found"
#     )

# @app.put("/update/{product_id}")
# async def update_product( product_update: ProductUpdateRequest, product_id: UUID):
#     for product in db:
#         if  product.id == product_id :
#             if product_update.name is not None :
#                 product.name = product_update.name
#             if product_update.category is not None :
#                 product.category = product_update.category
#             return
#     raise HTTPException(
#         status_code=404,
#         detail=f"Product with id: {product_id} not found"
#     )

