import RPi.GPIO as GPIO
import time

Button1 = 5
Button2 = 21
Servo = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Servo, GPIO.OUT)

# Starten van het PWM signaal voor de servo
pwm = GPIO.PWM(Servo, 50)
pwm.start(0)

# Functie om gebruik te maken van millis
def millis():
    return time.time() * 1000

# Variabele om de tijd bij te houden
huidigeTijd = millis()
vorigeTijd = millis()
pauze = millis()


# Methode om de angle van de servo te berekeken en daarbij de duty cycle aan te passen
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(Servo, True)
    pwm.ChangeDutyCycle(duty)

# Variabele voor het bewegen van de servo
draai1 = False
draai2 = False

while True:
    huidigeTijd = millis()
    btnState1 = GPIO.input(Button1)
    btnState2 = GPIO.input(Button2)

    global tijd

    # Check of button1 is ingedrukt
    if btnState1 == GPIO.HIGH:
        if not draai1:
            draai1 = True
            vorigeTijd = millis()
            tijd = 1000

    # Check of button 2 is ingedrukt
    if btnState2 == GPIO.HIGH:
        if not draai1:
            draai1 = True
            vorigeTijd = millis()
            tijd = 500

    # Check of dat de servo moet gaan draaien
    if draai1:
        # Check of de servo nog niet is gedraaid
        if not draai2:
            if (huidigeTijd - vorigeTijd) >= tijd:
                vorigeTijd = millis()
                SetAngle(120)
                draai2 = True
        # Check of de servo al wel is gedraaid
        if draai2:
            if (huidigeTijd - vorigeTijd) >= tijd:
                SetAngle(0)
                draai2 = False
                draai1 = False