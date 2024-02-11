from fastapi import FastAPI, File, UploadFile
import joblib
import numpy as np

server = FastAPI()

# Carregue o modelo
model = joblib.load("model.pkl")


@server.post("/predict")
async def predict(file: UploadFile):
    contents = await file.read()
    np_array = np.frombuffer(contents, dtype=np.float64)
    
    # Faça a predição usando o modelo carregado
    prediction = model.predict_proba(np_array.reshape(1, -1))

    return {"probability_of_default": prediction[0, 1]}