# PRUEBAS EN LOCAL CON DOCKER

## construir container

```bash
docker build -t blipol-ai:latest .
```

## correr container
```bash
docker run -p 8081:8081 blipol-ai:latest
```

## con docker-compose
```bash
docker-compose up --build
```