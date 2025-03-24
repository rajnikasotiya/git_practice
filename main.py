from fastapi import FastAPI 
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}    

#index route added
@app.get("/root")
def my_index_root():
    return {"Hello": "World"}                


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.0.1", port=8000)