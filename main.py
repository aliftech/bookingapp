from fastapi import FastAPI
import uvicorn

import app.registration.router.registration_router as registration
import app.login.router.login_router as login
import app.refresh_token.router.refresh_token_router as token
import app.booking_price.router.booking_price_router as bookprice
import app.table.router.table_router as table
import app.booking.router.booking_router as booking

app = FastAPI()

app.include_router(registration.registration)
app.include_router(login.signin)
app.include_router(token.token)
app.include_router(bookprice.price)
app.include_router(table.table)
app.include_router(booking.booking)


@app.get('/')
def root_api():
    return {"message": "Welcome to Booking App"}
