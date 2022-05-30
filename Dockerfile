FROM python:3.9

WORKDIR /tmp
RUN apt update && apt install -y python3-opencv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /neko
COPY config.env bot.py ./
COPY src ./src
COPY assets ./assets

CMD ["python3", "-m", "nb_cli", "run"]
