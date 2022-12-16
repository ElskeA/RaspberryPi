import RPi.GPIO as GPIO
import time

Raspberry_PIN = 22
Raspberry_PIN2 = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(Raspberry_PIN, GPIO.OUT)
GPIO.setup(Raspberry_PIN2, GPIO.IN)

while True:
    if GPIO.input(Raspberry_PIN2) == 0:
        GPIO.output(Raspberry_PIN, GPIO.LOW)
    elif GPIO.input(Raspberry_PIN2) == 1:
        GPIO.output(Raspberry_PIN, GPIO.HIGH)
