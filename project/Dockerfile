FROM python:3.8-buster

WORKDIR /project

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /project
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /project

ENV LANG C.UTF-8
EXPOSE 8080

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "api/settings.py", "api:app"]
