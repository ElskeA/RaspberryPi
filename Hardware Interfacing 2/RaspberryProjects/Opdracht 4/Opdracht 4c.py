import RPi.GPIO as GPIO
import time

LED_Yellow = 16
LED_Green = 6
BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

# Methode die het gele LEDje laat knipperen
def Yellow_blink():
    GPIO.output(LED_Yellow, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_Yellow, GPIO.LOW)
    time.sleep(0.7)

# Methode die het groene LEDje laat knipperen
def Green_blink():
    GPIO.output(LED_Green, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_Green, GPIO.LOW)
    time.sleep(0.7)

while True:
    buttonState = GPIO.input(BUTTON_PIN)

    # Als de knop is ingedrukt, gaat het groene ledje uit en de gele wordt aangezet dmv de methode
    if buttonState == GPIO.HIGH:
        GPIO.output(LED_Green, GPIO.LOW)
        Yellow_blink()
    # Als de knop niet is ingedrukt wordt precies het tegenover gestelde gedaan
    elif buttonState == GPIO.LOW:
        GPIO.output(LED_Yellow, GPIO.LOW)
        Green_blink()