FROM python:3.9
WORKDIR /app
COPY mongo.py .
RUN pip install mongo
ENTRYPOINT [ "python3", "mongo.py" ]