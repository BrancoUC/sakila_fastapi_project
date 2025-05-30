from fastapi import FastAPI
from routers import (
    actor_router,
    address_router,
    category_router,
    city_router,
    country_router,
    customer_router,
    film_router,
    film_actor_router,
    film_category_router,
    film_text_router,
    inventory_router,
    language_router,
    payment_router,
    rental_router,
    staff_router,
    store_router
)

app = FastAPI(debug=True)

app.include_router(actor_router.router, prefix="/actors", tags=["actors"])
app.include_router(address_router.router, prefix="/addresses", tags=["addresses"])
app.include_router(category_router.router, prefix="/categories", tags=["categories"])
app.include_router(city_router.router, prefix="/cities", tags=["cities"])
app.include_router(country_router.router, prefix="/countries", tags=["countries"])
app.include_router(customer_router.router, prefix="/customers", tags=["customers"])
app.include_router(film_router.router, prefix="/films", tags=["films"])
app.include_router(film_actor_router.router, prefix="/film_actor", tags=["film_actor"])
app.include_router(film_category_router.router, prefix="/film_category", tags=["film_category"])
app.include_router(film_text_router.router, prefix="/film_text", tags=["film_text"])
app.include_router(inventory_router.router, prefix="/inventory", tags=["inventory"])
app.include_router(language_router.router, prefix="/language", tags=["language"])
app.include_router(payment_router.router, prefix="/payment", tags=["payment"])
app.include_router(rental_router.router, prefix="/rental", tags=["rental"])
app.include_router(staff_router.router, prefix="/staff", tags=["staff"])
app.include_router(store_router.router, prefix="/store", tags=["store"])
