FROM python:3.8-slim
WORKDIR /code
COPY . .
RUN ls -lav
RUN pip install -r requirements.txt
CMD flask run -h 0.0.0.0 -p 80

