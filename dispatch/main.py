# main.py
from typing import Optional
from fastapi import FastAPI
app = FastAPI(title="My greeting server")
@app.get("/api/greet")
async def greet(name: Optional[str] = None):
    if name is None:
        name = "John"
    return { "greeting": f"Hello, {name}!" }