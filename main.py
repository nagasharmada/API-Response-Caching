from fastapi import FastAPI
from routes.api import router
app = fastAPI()
app.include_router(router)
@app.get("/")
def home():
    return {"message":"LRU Cache Backend is running"};