from fastapi import APIRouter
from .endpoints import users_router, products_router, orders_router

api_router = APIRouter()
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])
api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])

