FROM python:3.8-slim
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN ls -lav
CMD flask run -h 0.0.0.0 -p 80

