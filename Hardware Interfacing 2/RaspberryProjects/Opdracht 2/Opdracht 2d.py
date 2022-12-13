import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#Nogmaals met de time functie wordt de knipper interval nu gezet op 0.01 seconde
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.01)