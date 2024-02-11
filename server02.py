from fastapi import FastAPI, File, UploadFile
import joblib
import numpy as np

server = FastAPI()

# Carregue o modelo
model = joblib.load("modelo_kmeans.pkl")


@server.post("/predict2")
async def predict(file: UploadFile):
    contents = await file.read()
    np_array = np.frombuffer(contents, dtype=np.float64)
    
    # Faça a predição usando o modelo carregado
    persona = model.predict(np_array.reshape(1, -1))

    if persona == 0:
        fraude_media = 0.34631
    if persona == 1:
        fraude_media = 0.197401
    if persona == 2:
        fraude_media = 0.107506
    if persona == 3:
        fraude_media = 0.340295
    if persona == 4:
        fraude_media = 0.221605

    return {"Cluster": persona, "Fraude Média": fraude_media}
