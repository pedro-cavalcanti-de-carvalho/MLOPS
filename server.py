 import http.server
 import socketserver
 import pickle
 from http import HTTPStatus

 class MyHandler(http.server.SimpleHTTPRequestHandler):
     def do_POST(self):
         content_length = int(self.headers['Content-Length'])
         post_data = self.rfile.read(content_length)

         # Carregue o modelo aqui
         model = pickle.load(open('model.pkl', 'rb'))

         # Lógica de predição aqui (exemplo: sempre retorna 0)
         # Substitua essa lógica com a lógica real de predição
         input_data = pickle.loads(post_data)
         prediction = model.predict_proba([input_data])

         # Envie a resposta para o cliente
         self.send_response(HTTPStatus.OK)
         self.send_header('Content-type', 'text/plain')
         self.end_headers()
         self.wfile.write(str(prediction).encode())

 if __name__ == "__main__":
     PORT = 8000

     with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
         print(f"Serving on port {PORT}")
         httpd.serve_forever()
