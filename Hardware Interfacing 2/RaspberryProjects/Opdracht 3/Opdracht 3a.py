import RPi.GPIO as GPIO
import time

#Er worden nu 2 LEDjes gebruikt. Beide krijgen hun pin aangewezen
LED_Yellow = 16
LED_Green = 6

GPIO.setmode(GPIO.BCM)
#Voor beide ledjes wordt de output aangegeven, zodat ze aan kunnen
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)

#In de loop worden beide LEDs meteen aangezet. Er zit 1 seconde tussen door het gebruik van de time functie
#Vervolgens gaan de LEDs weer uit en wordt er nogmaals 1 seconde gewacht totdat de loop weer opnieuw begint.
while True:
    GPIO.output(LED_Yellow, GPIO.HIGH)
    GPIO.output(LED_Green, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_Yellow, GPIO.LOW)
    GPIO.output(LED_Green, GPIO.LOW)
    time.sleep(1)