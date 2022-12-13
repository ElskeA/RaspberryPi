import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#Led gaat weer knipperen. Met de time functie wordt ervoor gezorgd dat het led 0.1 seconde aan staat en 0.1 seconde uitstaat
#Dan gaat de loop weer verder
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)