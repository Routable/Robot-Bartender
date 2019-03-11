import RPi.GPIO as GPIO
from logger import sys_log
import threading
import time


class bartender():
    pumps = []

    def __init__(self):
        pumps = [17, 27, 22, 23, 24, 25]
        GPIO.setwarnings(False)
        for pump in pumps:
            GPIO.setup(pump, GPIO.OUT)

    def enable_pump(self, pin):
        sys_log("Enabling pin %s. [pumps.py, enable_pump" % pin)
        GPIO.output(pin, GPIO.HIGH)

    def disable_pump(self, pin):
        sys_log("Disabling pin %s. [pumps.py, disable_pump" % pin)
        GPIO.output(pin, GPIO.LOW)

