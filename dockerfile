FROM python:3.9

WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src/ /app
ENTRYPOINT [ "python3", "-u", "main.py" ]
