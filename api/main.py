from fastapi import FastAPI
from model.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Doctor Recommender API is running"}

@app.get("/predict")
def get_prediction(symptom: str):
    result = predict(symptom)
    return {"recommended_department": result}