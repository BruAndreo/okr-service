# OKR Service

API service for OKRs

## Run project locally

Before cloning the project for your workspace, enter in the directory and install the dependencies.

*Obs: It's recommend use `virtualenv` to install dependencies and use this project.*
```SHELL
pip3 install -r requirements.txt
```

Generate your `.env` with your preferences and configurations
```SHELL
cp .example.env .env
```

To initialize the server, run the `entrypoint.py`
```SHELL
python3 entrypoint.py
```

## Run in a Docker container

To run the project in a docker container, you need to clone and generate your `.env`.

After this steps, build de container
```SHELL
docker build -t okr-service-container .
```

And finally, run the container
```SHELL
docker run -p 3000:3000 --network host okr-service-container
```

## Run with Docker Compose

It's possible to use docker-compose too. Just execute the command
```SHELL
docker-compose up
```

## Endpoints and Docs

After the server running, put `http://localhost:{APP_PORT_IN_DOTENV}/docs` in your navigator.
Will be loaded a docs from all endpoints can you use.