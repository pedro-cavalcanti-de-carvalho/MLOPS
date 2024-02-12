import http.server
import socketserver
import pickle
import json
from http import HTTPStatus

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_length)

#         # Carregue o modelo aqui
        model = pickle.load(open('modelo_kmeans.pkl', 'rb'))

         # Lógica de predição aqui (exemplo: sempre retorna 0)
         # Substitua essa lógica com a lógica real de predição
        input_data = pickle.loads(post_data)
        prediction = model.predict([input_data])
        cluster = str(prediction)
        if prediction == 0:
            fraude_media = 28.923973
            persona = 'Renda Média sem cadastro de sexo e do Sul'
        if prediction == 1:
            fraude_media = 25.752149
            persona = 'Renda Média Homens Jovens'
        if prediction == 2:
            fraude_media = 23.738199
            persona = 'Renda Alta Jovens do Sul'
        if prediction == 3:
            fraude_media = 18.84012
            persona = 'Renda Alta Não Binário'
        if prediction == 4:
            fraude_media = 25.304336
            persona = 'Renda Baixa Mulheres'
        result = {
            'Cluster': cluster,
            'Probabilidade de Fraude': fraude_media,
            'Persona': persona
        }

         # Envie a resposta para o cliente
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(result).encode())

if __name__ == "__main__":
    PORT = 8000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
