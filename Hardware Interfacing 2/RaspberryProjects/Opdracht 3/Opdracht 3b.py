import RPi.GPIO as GPIO
import time

#De twee leds koppelen aan hun pins
LED_Yellow = 16
LED_Green = 6

GPIO.setmode(GPIO.BCM)
#Leds op output zetten
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)

#In deze loop knipperen de leds om en om
while True:
    #Geel gaat op aan bij het starten van de loop en groen op uit
    GPIO.output(LED_Yellow, GPIO.HIGH)
    GPIO.output(LED_Green, GPIO.LOW)
    #1 seconde delay
    time.sleep(1)
    #Nu gaat geel op uit en groen op aan
    GPIO.output(LED_Yellow, GPIO.LOW)
    GPIO.output(LED_Green, GPIO.HIGH)
    #Weer 1 seconde delay
    time.sleep(1)
