# pip install fastapi[all]

from fastapi import FastAPI
from parser import kinoqidir

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "success"}

@app.get("/search")
async def qidirish(nom):
    return kinoqidir(nom=nom)