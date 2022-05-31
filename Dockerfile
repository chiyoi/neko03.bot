FROM python:3.9-alpine

WORKDIR /tmp
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /atri
COPY ./atri .
COPY ./assets/assets ./assets

CMD ["nb", "run"]
