import RPi.GPIO as GPIO

LED_Yellow = 16
BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)


while True:
    buttonState = GPIO.input(BUTTON_PIN)

    # Als button is ingedrukt aan
    if buttonState == GPIO.HIGH:
        GPIO.output(LED_Yellow, GPIO.HIGH)
    # Button is niet ingedrukt, dus led gaat uit
    else:
        GPIO.output(LED_Yellow, GPIO.LOW)
