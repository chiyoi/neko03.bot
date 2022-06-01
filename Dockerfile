FROM python:3.9-slim

WORKDIR /tmp
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /bot
COPY ./atri ./atri
COPY ./bot.py ./config.env ./
COPY ./assets/assets ./assets

CMD ["nb", "run"]
