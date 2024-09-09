from request import Request

from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(request: Request):
    return {
        "status":"success",
        "message":"Prediction Successful",
        "data":request
    }