import RPi.GPIO as GPIO
import time

LED_Yellow = 16
LED_Green = 6
Button1 = 5
previousMillis = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, GPIO.PUD_DOWN)

def millis():
    return time.time() * 1000

def Blink_Down():
    global previousMillis
    if millis() - previousMillis >= 1000:
        previousMillis = millis()
        if GPIO.input(LED_Yellow):
            GPIO.output(LED_Yellow, GPIO.LOW)
            GPIO.output(LED_Green, GPIO.HIGH)
        else:
            GPIO.output(LED_Yellow, GPIO.HIGH)
            GPIO.output(LED_Green, GPIO.LOW)

def Blink_Up():
    global previousMillis
    if GPIO.input(LED_Yellow) == GPIO.HIGH:
        if millis() - previousMillis >= 1300:
            previousMillis = millis()
            GPIO.output(LED_Yellow, GPIO.LOW)
            GPIO.output(LED_Green, GPIO.HIGH)
    elif GPIO.input(LED_Yellow) == GPIO.LOW:
        if millis() - previousMillis >= 700:
            previousMillis = millis()
            GPIO.output(LED_Yellow, GPIO.HIGH)
            GPIO.output(LED_Green, GPIO.LOW)

while True:
    buttonState1 = GPIO.input(Button1)

    if buttonState1 == GPIO.HIGH:
        Blink_Down()
    else:
        Blink_Up()