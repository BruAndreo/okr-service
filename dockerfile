FROM python:3.8.12-buster

COPY . . 

CMD pip install -r requirements.txt

EXPOSE 3000
ENTRYPOINT [ "uvicorn entrypoint:app --port 3000 --reload" ]