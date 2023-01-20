import RPi.GPIO as GPIO
import time

Raspberry_PIN2 = 6
Raspberry_PIN3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(Raspberry_PIN2, GPIO.OUT)
GPIO.setup(Raspberry_PIN3, GPIO.OUT)

while True:
    # Op de arduino zit een button aangesloten die een pin op high zet die zit aangesloten op de raspberry. Dit is pin2
    # Het moment dat de raspberry leest dat deze pin door de arduino op high wordt gezet, wordt de andere pin aangezet
    # Die loopt van de raspberry naar het led lampje.
    print(GPIO.input(Raspberry_PIN2))
    if GPIO.input(Raspberry_PIN2) == 1:
        GPIO.output(Raspberry_PIN3, GPIO.LOW)
    elif GPIO.input(Raspberry_PIN2) == 0:
        GPIO.output(Raspberry_PIN3, GPIO.HIGH)
