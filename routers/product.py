from fastapi import APIRouter

router_products = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router_products.get("/products",summary="List of products", description="Returns all products" )
async def get_products():
    #create(first_name='Addu', last_name='Pagal', email='addu@gmail.com', phone='123-494', status=1)
    return [{'status': 'OK'}]

@router_products.get("/view/{id}", summary="Returns a single contact")
async def view(id: int):
    """
        To view all details related to a single contact

        - **id**: The integer id of the contact you want to view details.
    """
    return [{'status': 'OK'}]