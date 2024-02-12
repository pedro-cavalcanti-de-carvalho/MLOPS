FROM python:3.9

# Instala aplicações básicas para caso precise vasculhar um contêiner da imagem
WORKDIR /MLOPS

COPY requirements.txt .
COPY model.pkl .
#COPY modelo_kmeans.pkl .
COPY server.py .

# Expõe para o HOST algumas portas, por padrão
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install requirements.txt

CMD ["python", "server.py"]
