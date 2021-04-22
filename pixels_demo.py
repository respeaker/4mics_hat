import signal
import sys
import time
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern
from rainbow_led_pattern import RainbowLedPattern

global pixels

class GracefulKiller:
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        global pixels
        pixels.off()
        sys.exit(0)

if __name__ == '__main__':
    global pixels
    pixels.pattern = RainbowLedPattern(show=pixels.show)
    killer = GracefulKiller()

    while True:
        try:
            pixels.wakeup()
            time.sleep(3)
            pixels.think()
            time.sleep(3)
            pixels.speak()
            time.sleep(6)
            pixels.off()
            time.sleep(3)
        except KeyboardInterrupt:
            break

    pixels.off()
    time.sleep(1)
