import RPi.GPIO as GPIO
import time

LED_Yellow = 16
LED_Green = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)

#Methode voor het gele LED lampje
def Yellow_blink():
    #Gaat aan
    GPIO.output(LED_Yellow, GPIO.HIGH)
    #Blijf aan voor 1.3 seconde
    time.sleep(1.3)
    #Gaat weer uit
    GPIO.output(LED_Yellow, GPIO.LOW)
    #Blijft uit voor 0.7 seconde
    time.sleep(0.7)

#Methode voor het groene ledje, werkt hetzelfde als de methode hier boven
def Green_blink():
    GPIO.output(LED_Green, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_Green, GPIO.LOW)
    time.sleep(1.7)

#Beide methode worden aangesproken in de while loop
while True:
    #De loop begint bij de eerste methode, deze wordt volledig doorlopen
    #voordat de tweede methode wordt uitgevoerd 
    Yellow_blink()
    Green_blink()



