#import RPi.GPIO as GPIO
from logger import sys_log
import threading
import sqlite3
import time        
import threading


class Bartender():

    def __init__(self):
        sys_log("Initializing GPIO Pins. [pumps.py, init]")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.pumps = [16, 20, 21, 19, 13, 26]
        for p in self.pumps:
          GPIO.setup(p, GPIO.OUT)
          GPIO.output(p, GPIO.HIGH)

    def enable_pump(self, pin, timer):
      GPIO.output(pin, GPIO.LOW)
      time.sleep(timer)
      GPIO.output(pin, GPIO.HIGH)

    def make_drink(self, drink):
    
      try:
        sys_log("Starting Drink Pour  -  [pumps.py, make_drink]")
        
        # Connect to the Drinks Table
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        result = c.execute('SELECT GPIO_PIN, i.Component, ri.mix_time FROM PUMPS p, INGREDIENTS i, recipe_ingredients ri , recipes r WHERE p.ingredient_id = i.id AND i.id = ri.ingredient_id AND ri.recipe_id = r.id AND r.name = (?)', (drink,))
        
        drink_dict = {}
        
        for i in result:
          drink_dict[i[0]] = i[2]

    
        for key, val in drink_dict.items():
          sys_log("Enabling pump - [enable_pump, pumps.py]")
          thread1 = threading.Thread(target=self.enable_pump, args=(key,val))
          thread1.start()
          
      except Exception as e:
        sys_log(e)
        GPIO.cleanup()
        
    def prime_pumps():
      try:
        sys_log("Priming pumps - [pumps.py, prime_pumps]")
        for p in self.pumps:
          GPIO.output(p, GPIO.LOW)
        time.sleep(3)
        for p in slef.pumps:
          GPIO.output(p, GPIO.LOW)
      except Exception as e:
        sys_log(e)
        GPIO.cleanup()
    
    def clean_pumps():
      try:
        sys_log("Flushing pumps - [pumps.py, prime_pumps]")
        for p in self.pumps:
          GPIO.output(p, GPIO.LOW)
        time.sleep(60)
        for p in slef.pumps:
          GPIO.output(p, GPIO.LOW)
      
      except Exception as e:
        sys_log(e)
        GPIO.cleanup()
      
      
    def test_pumps(self, seconds):
      try:
        for p in self.pumps:
          sys_log("Enabling GPIO_PIN: %s [pumps.py, test_pumps]" % p)
          GPIO.output(p, GPIO.LOW)
          time.sleep(seconds)
          sys_log("Disabling GPIO_PIN: %s [pumps.py, test_pumps]" % p)
          GPIO.output(p, GPIO.HIGH)
      except Exception as e:
        sys_log(e)
        GPIO.cleanup()

    
    def test_pumps_all(self, seconds):
      try:
        for p in self.pumps:
          sys_log("Enabling GPIO_PIN: %s [pumps.py, test_pumps]" % p)
          GPIO.output(p, GPIO.LOW)
          
        time.sleep(seconds)
        
        for p in self.pumps:
          sys_log("Disabling GPIO_PIN: %s [pumps.py, test_pumps]" % p)
          GPIO.output(p, GPIO.HIGH)
    
      except Exception as e:
        sys_log(e)
        GPIO.cleanup()
        