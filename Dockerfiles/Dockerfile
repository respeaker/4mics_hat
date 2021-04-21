FROM python:3.9.4-alpine

ENV PACKAGES="\
	alsa-plugins \
	alsa-plugins-a52 \
	alsa-plugins-jack \
	alsa-plugins-lavrate \
	alsa-plugins-pulse \
    bash \
    git \
    libc6-compat \
    libgfortran \
    libstdc++ \
    openblas \
	portaudio \
    "

ENV PYTHON_PACKAGES="\
    gpiozero \
	numpy \
	pigpio \
	pyaudio \
	spidev \
	wave \
    "

RUN apk add --virtual build-deps build-base openblas-dev freetype-dev pkgconfig gfortran linux-headers portaudio-dev \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install --no-cache-dir $PYTHON_PACKAGES \
	&& apk del build-deps \
    && apk add --no-cache --virtual build-runtime $PACKAGES \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

RUN git clone https://github.com/lavirott/4mics_hat

WORKDIR /usr/src/app/4mics_hat

ENTRYPOINT ["python3"]
CMD ["pixels_demo.py"]
