from typing import Union

from fastapi import FastAPI
import joblib

from pydantic import BaseModel

from model_app import load_model, predict

app = FastAPI()
model = load_model()

class House(BaseModel):
    size:float
    nb_bedrooms:int
    garden:int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
def read_item(input: House):
    pred = model.predict([[input.size, input.nb_bedrooms, int(input.garden)]])
    return {"pred": pred[0]}

