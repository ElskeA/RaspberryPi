import RPi.GPIO as GPIO
import time

# Deze pin gaat van de raspberry naar de arduino
Raspberry_PIN = 2
previousMillis = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(Raspberry_PIN, GPIO.OUT)

# Methode om gebruik te maken van millis
def millis():
    return time.time() * 1000
# Methode die ervoor zorgt dat de pin naar de raspberry 1 seconde op high zet en 1 seconde op low
# Dit wordt vervolgens opgepakt door de arduino
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