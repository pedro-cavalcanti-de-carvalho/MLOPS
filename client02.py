import joblib
import numpy as np
from flask import Flask, jsonify, request

class client:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

import requests

# URL do servidor Flask
url = "http://localhost:8080/Cluster"

# Dados do novo registro a serem enviados
novo_registro = {"novo_registro": np.array(
        [0.011235955056179775,0.3275000000000001,0.9996412877768811,0.013728264314081425,0.2126880537269261,
         1.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,1.0,
         0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0,1.0,0.0,1.0,0.0])  # Substitua isso com seu próprio array
}  # Substitua isso pelo seu novo registro

# Enviar solicitação POST para o servidor Flask
response = requests.post(url, json=novo_registro)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extrair o grupo previsto da resposta
    grupo_previsto = response.json()['grupo_previsto']
    fraude_media = response.json()['Fraude_media']
    print("Grupo Previsto: ", grupo_previsto)
    print("Fraude média do grupo: ", fraude_media)
else:
    print("Erro ao enviar solicitação:", response.status_code)
