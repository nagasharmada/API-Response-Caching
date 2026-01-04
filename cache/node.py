from fastapi import FastAPI
app = fastAPI()
@app.get("/")
def home():
    return {"message":"LRU Cache Backend is running"};