
# Taller de Docker Compose y PostgreSQL
## Autor : Jhonatan Steven Baron
## Requisitos
## Tener Docker y Docker compose instalados

## Pasos para ejecutar

##1. Se clona el repositorio:

   git clone https://github.com/jhonatanBaron/-docker-compose-taller.git
##   Nos ubicamos en la carpeta del proyecto -->
   cd -docker-compose-taller
##luego levantamos los contenedores
docker compose up -d --build
##y despues ya se podria probar la API usando -->

curl http://localhost:5000

