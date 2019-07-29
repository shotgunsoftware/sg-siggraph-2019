FROM python:2.7

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . .

EXPOSE 80

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]