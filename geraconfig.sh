
echo '{                                                     ' >> microservices.json
echo '    "model": {                                        ' >> microservices.json
echo '      "version": "V01",                               ' >> microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor001 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict"            ' >> microservices.json
echo '    },                                                ' >> microservices.json
echo '    "modelo_kmeans": {                                ' >> microservices.json
echo '      "version": "V01",                               ' >> microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor002 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict2"           ' >> microservices.json
echo '    }                                                 ' >> microservices.json
echo '}                                                     ' >> microservices.json

echo "Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat config/microservices.json
