#import module voor de pgio interface
import RPi.GPIO as GPIO
#import een module voor methodes die tijd gebruiken
import time

#Aangeven aan welke pin de led wordt gekoppeld
LED_PIN = 16

#Er wordt een header gebruikt dus is de setmode gezet naar BCM
GPIO.setmode(GPIO.BCM)
#Aangeven dat de ledpin output is, zodat het licht kan geven
GPIO.setup(LED_PIN, GPIO.OUT)

#Hier begint de while loop die vervolgens begint met he aanzetten van de ledpin
#Met de time functie blijft het Led 1 seconde aan en gaat vervolgens weer uit
#Door nogmaals de time functie te gebruiken blijft het led ook 1 seconde uit voordat het weer aangaat, omdat de loop opnieuw begint
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
