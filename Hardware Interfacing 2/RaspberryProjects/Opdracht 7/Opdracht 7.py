import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

Button1 = 5
Button2 = 21

gpioPins =  [4, 27, 9, 2]
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(Button2, GPIO.IN, GPIO.PUD_DOWN)

# Een instantie aanmaken vanuit de library
motor = RpiMotorLib.BYJMotor("MijnMotor", "28BYJ")

# De wachttijden berekenen
wait5 = (5 / 4096)
wait12 = (12 / 4096)

try:
    while True:
        buttonState2 = GPIO.input(Button2)
        buttonState1 = GPIO.input(Button1)

        if buttonState1 == GPIO.HIGH:
            # Als button1 is ingedrukt runt de motor voor 5 stappen
            motor.motor_run(gpioPins, wait5, 512, False, True, "half", 0)
        if buttonState2 == GPIO.HIGH:
            # Als button2 is ingedrukt runt de motor voor 12 stappen
            motor.motor_run(gpioPins, wait12, 512, True, True, "half", 0)

finally:
    GPIO.cleanup()