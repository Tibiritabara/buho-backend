# Buho Backend WebApp

Para construir esta webapp por favor asegurese de tener una base de datos PGSQL y posteriormente ejecutar los siguientes commandos

```bash
docker build --build-arg DB_USER="postgres" --build-arg DB_PASSWORD="password" --build-arg DB_HOST="172.17.0.1" --build-arg DB_PORT="5432" --build-arg DB_NAME="test" -t buho .
```

```bash
docker run -p 8080:8080 buho
```

Luego desde el cliente REST insomnia, cree un request tipo POST con body "GraphQL".
