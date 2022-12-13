import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#Hetzelfde als de vorige opdracht. Led wordt eerst aangezet en de time functie zorgt ervoor dat het 1 seconde aan blijft.
#Vervolgens gaat het led weer uit, en nogmaals door de time functie pauzeert de loop voor 2 seconde voordat het opnieuw begint met de loop
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)