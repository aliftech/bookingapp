# Instalation

## Install VENV

```
py -m pip install --user virtualenv
```

## Create New Env

```
py -m venv env
```

then acticate the virtual env by this command

```
.\env\Scripts\activate
```

## Install the Dependencies

```
pip install -r requirements.txt
```

# Database Migration

```
alembic upgrade head
```

# Running

```
uvicorn --reload main:app
```

```shell
docker run -p 8000:8000 my-app
```

## Docker

You can also running this application using docker.

```bash
docker-compose up --build
```

or

```bash
docker-compose up
```

With the container running, you can test the application by opening a web browser and navigating to `http://localhost:8000`.
