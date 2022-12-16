import RPi.GPIO as GPIO
import time

LED_Yellow = 16
BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

def Yellow_blink():
    GPIO.output(LED_Yellow, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_Yellow, GPIO.LOW)
    time.sleep(1)

while True:
    buttonState = GPIO.input(BUTTON_PIN)

    while buttonState == GPIO.HIGH:
        Yellow_blink()