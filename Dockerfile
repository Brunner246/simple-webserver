
#FROM python:3
#
#WORKDIR /app
#
## COPY src /app/src
#COPY requirements.txt /app
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#CMD ["python3", "app.py", "flask","run", "--host=0.0.0.0"]

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]