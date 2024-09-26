FROM python:3.11-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py", "forwardmessage.py"]