from typing import Optional
from fastapi import Request, FastAPI
from selenium_scripts import bot, picking

app = FastAPI(title="My greeting server")
@app.get("/api/greet")
async def greet(name: Optional[str] = None):
    if name is None:
        name = "John"
    return { "greeting": f"Hello, {name}!" }

@app.post("/api/price")
async def get_price(request: Request):
    request = request.json()
    product_url = request['product_url']
    profile = bot.Profile(request['profile'])
    b = picking.pick(product_url)
    result = b.run(product_url, profile)
    return {
        'subtotal' : result.subtotal,
        'shipping' : result.shipping,
        'total' : result.total
    }