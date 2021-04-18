FROM python:3.9.4-buster

RUN apt-get update
RUN apt-get install -y portaudio19-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/lavirott/4mics_hat

WORKDIR /usr/src/app/4mics_hat

CMD ["python3", "pixels_demo.py"]
