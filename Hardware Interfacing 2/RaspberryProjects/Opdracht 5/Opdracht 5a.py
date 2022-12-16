import RPi.GPIO as GPIO
import time

LED_Yellow = 16
BUTTON_PIN = 5
previousMillis = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

def millis():
    return time.time() * 1000

def Yellow_blink():
    global previousMillis
    if millis() - previousMillis >= 1000:
        previousMillis = millis()
        if GPIO.input(LED_Yellow):
            GPIO.output(LED_Yellow, GPIO.LOW)
        else:
            GPIO.output(LED_Yellow, GPIO.HIGH)

while True:
    buttonState = GPIO.input(BUTTON_PIN)

    if buttonState == GPIO.HIGH:
        Yellow_blink()