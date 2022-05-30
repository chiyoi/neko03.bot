FROM python:3.9

WORKDIR /tmp
RUN apt update && apt install -y python3-opencv
COPY atri/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /atri
COPY atri/config.env atri/bot.py ./
COPY atri/src ./src
COPY atri/assets ./assets

CMD ["python3", "-m", "nb_cli", "run"]
