from fastapi import FastAPI
app = fastAPI()
@app.get("/")
def hom():
    return {"message":"LRU Cache Backend is running"};