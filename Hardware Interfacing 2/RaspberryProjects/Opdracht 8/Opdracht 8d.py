import RPi.GPIO as GPIO
import time

ledPin = [22, 6]
raspPin = 4
raspOut = 9
btnPin = 13
btnstate = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin[0], GPIO.OUT)
GPIO.setup(ledPin[1], GPIO.OUT)
GPIO.setup(raspPin, GPIO.OUT)
GPIO.setup(raspOut, GPIO.IN)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # De if statement begint bij het checken of de button is ingedrukt
    if GPIO.input(btnPin) == 1:
        # ALs de button wel is ingedrukt dan wordt de raspin op high gezet
        # deze pin staat aangesloten op de arduino, die vervolgens de code daar
        # weer kan uitvoeren. Dan wordt de buttonstate gereset, zodat het de loop
        # weer kan doorlopen
        if btnstate == 1:
            GPIO.output(raspPin, GPIO.HIGH)
            btnstate = 0
        # Hier gebeurd precies hetzelfde, maar andersom.
        # Buttonstate wordt op 1 gezet, zodat het de loop weer
        # kan doorlopen
        elif btnstate == 0:
            GPIO.output(raspPin, GPIO.LOW)
            btnstate = 1
    # de raspout pin wordt door de arduino op hoog of laag gezet.
    # deze wordt hier uitgelezen. Als de pin op high staat gaat de ene
    # led aan en de andere uit. Bij low hetzelfde, maar dan andersom
    if GPIO.input(raspOut) == 1:
        GPIO.output(ledPin[0], GPIO.LOW)
        GPIO.output(ledPin[1], GPIO.HIGH)
    elif GPIO.input(raspOut) == 0:
        GPIO.output(ledPin[0], GPIO.HIGH)
        GPIO.output(ledPin[1], GPIO.LOW)
    time.sleep(0.1)