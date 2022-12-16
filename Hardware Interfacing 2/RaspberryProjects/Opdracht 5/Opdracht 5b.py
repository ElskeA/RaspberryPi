import RPi.GPIO as GPIO
import time

LED_Yellow = 16
LED_Green = 6
Button1 = 5
Button2 = 21
previousMillis = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(Button2, GPIO.IN, GPIO.PUD_DOWN)

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

def Green_blink():
    global previousMillis
    if millis() - previousMillis >= 700:
        previousMillis = millis()
        if GPIO.input(LED_Green):
            GPIO.output(LED_Green, GPIO.LOW)
        else:
            GPIO.output(LED_Green, GPIO.HIGH)

while True:
    buttonState2 = GPIO.input(Button2)
    buttonState1 = GPIO.input(Button1)

    if buttonState2 == GPIO.HIGH:
        Green_blink()

    if buttonState1 == GPIO.HIGH:
        Yellow_blink()
