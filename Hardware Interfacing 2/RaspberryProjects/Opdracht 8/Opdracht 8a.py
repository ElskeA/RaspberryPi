import RPi.GPIO as GPIO
import time

Raspberry_PIN = 2
previousMillis = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(Raspberry_PIN, GPIO.OUT)

def millis():
    return time.time() * 1000

def Arduino_blink():
    global previousMillis
    if millis() - previousMillis >= 1000:
        previousMillis = millis()
        if GPIO.input(Raspberry_PIN):
            GPIO.output(Raspberry_PIN, GPIO.LOW)
        else:
            GPIO.output(Raspberry_PIN, GPIO.HIGH)

while True:
    Arduino_blink()