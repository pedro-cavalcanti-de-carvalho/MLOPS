
echo '{                                                     ' >> MLOPS/MLOPS/microservices.json
echo '    "model": {                                        ' >> MLOPS/MLOPS/microservices.json
echo '      "version": "V01",                               ' >> MLOPS/MLOPS/microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor001 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict"            ' >> MLOPS/MLOPS/microservices.json
echo '    },                                                ' >> MLOPS/MLOPS/microservices.json
echo '    "modelo_kmeans": {                                ' >> MLOPS/MLOPS/microservices.json
echo '      "version": "V01",                               ' >> MLOPS/MLOPS/microservices.json
echo '      "url": "http://'$(sudo docker inspect servidor002 | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['rede_trabalho']['IPAddress'])")':8080/predict2"           ' >> MLOPS/MLOPS/microservices.json
echo '    }                                                 ' >> MLOPS/MLOPS/microservices.json
echo '}                                                     ' >> MLOPS/MLOPS/microservices.json

echo "Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat config/microservices.json
