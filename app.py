import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/item/{item_id}")
async def get_item(item_id :int):
    return {"item_id": item_id}


 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)