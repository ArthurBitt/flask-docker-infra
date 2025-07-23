# Rodando a imagem

docker pull imagem package

docker run --name server_flask -p 5000:5000 <image>




# ação:rodando o container com bind volume do host e pull de imagem 
# contexto: testar funcionamento em diferentes versões

docker rm -f flask_server

docker run --network arthur_net -p 5000:5000 --name=flask_server -it -w /app/src --mount type=bind,source="$(pwd)/src",target=/app/src python:3.10-slim bash
docker run --network arthur_net -d --name redis -p 6379:6379 redis
redis-cli LRANGE flask_logs 0 10

```bash
docker run --name=flask_server \
-p 5000:5000 \
-it \
-w /app/src \
--mount type=bind, \
source="$(pwd)/src", \
target=/app/src \
python:3.10-slim bash
```


# ação:rodando o container com volume docker dedicado e pull de imagem 
# contexto: testar funcionamento em diferentes versões

```bash
docker run --name=flask_server \
-p 5000:5000 \
-it \
-w /app/src \
--mount type=bind, \
source="$(pwd)/src", \
target=/app/src \
python:3.10-slim bash
```

# ação:buildar uma imagem e rodar o container com volume docker dedicado 
# contexto: testar funcionamento da imagem buildada