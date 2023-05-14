from fastapi import FastAPI

from DB.handler import test_call

app = FastAPI()


@app.get("/")
async def root():
    s = test_call()
    return {"message": s}