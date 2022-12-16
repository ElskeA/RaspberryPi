import RPi.GPIO as GPIO

LED_Yellow = 16
BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)


while True:
    buttonState = GPIO.input(BUTTON_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_Yellow, GPIO.HIGH)
    else:
        GPIO.output(LED_Yellow, GPIO.LOW)
