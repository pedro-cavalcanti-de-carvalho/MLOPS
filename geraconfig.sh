
echo '{                                                     ' >  config/microservices.json
echo '    "model": {                                        ' >> config/microservices.json
echo '      "version": "V01",                               ' >> config/microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor001 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict"            ' >> config/microservices.json
echo '    },                                                ' >> config/microservices.json
echo '    "modelo_kmeans": {                                ' >> config/microservices.json
echo '      "version": "V01",                               ' >> config/microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor002 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict2"           ' >> config/microservices.json
echo '    }                                                 ' >> config/microservices.json
echo '}                                                     ' >> config/microservices.json

echo "Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat config/microservices.json
