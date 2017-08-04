4MICs HAT for Raspberry Pi
========================

## Introduction

This repository fork from [mic_hat](https://github.com/respeaker/mic_hat) and is made to be suitable for 4Mics Pi HAT.

## Requirements
+ [spidev](https://pypi.python.org/pypi/spidev)
+ [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)
+ [gpiozero](http://gpiozero.readthedocs.io/)

## Setup
1. Setup [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)
2. Use `raspi-config` to enable SPI.
3. Install `spidev` and `gpiozero` (`pip install spidev gpiozero`)
4. Run `python google_assistant.py`
