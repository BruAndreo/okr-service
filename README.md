# OKR Service

API service for OKRs

## Run project locally

Before cloning the project for your workspace, enter in the directory.

First install the dependencies
*It's recommend use `virtualenv` to install dependencies and use this project.*
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

## Endpoints and Docs

After the server running, put `http://localhost:{APP_PORT_IN_DOTENV}/docs` in your navigator.
Will be loaded a docs from all endpoints can you use.