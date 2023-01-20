import RPi.GPIO as GPIO
import time

Raspberry_PIN = 2
Raspberry_PIN2 = 22
previousMillis = 0
previousMillis2 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(Raspberry_PIN, GPIO.OUT)
GPIO.setup(Raspberry_PIN2, GPIO.OUT)

# Methode om muillis te berekenen
def millis():
    return time.time() * 1000

# Methode om de knippersnelheden aan te passen. De leds knipperen om en om. 1 seconde aan/uit, dan 3 seconde aan/uit
# de leds worden echter niet direct aangesproken, maar de pin die vanuit raspberry naar arduino loopt wordt high en low gezet
# De twee verschillende pinnen geven de verschillende knippersnelheden aan
def Arduino_blink():
    global previousMillis
    global previousMillis2
    if millis() - previousMillis >= 1000:
        previousMillis = millis()
        if GPIO.input(Raspberry_PIN):
            GPIO.output(Raspberry_PIN, GPIO.LOW)
        else:
            GPIO.output(Raspberry_PIN, GPIO.HIGH)

    if millis() - previousMillis2 >= 3000:
        previousMillis2 = millis()
        if GPIO.input(Raspberry_PIN2):
            GPIO.output(Raspberry_PIN2, GPIO.LOW)
        else:
            GPIO.output(Raspberry_PIN2, GPIO.HIGH)

while True:
    Arduino_blink()