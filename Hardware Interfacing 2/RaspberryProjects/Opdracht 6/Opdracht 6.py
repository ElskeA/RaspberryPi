import RPi.GPIO as GPIO
import time

Button1 = 5
Button2 = 21
Servo = 6
angle = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
pwm = GPIO.PWM(6, 50)
GPIO.setup(Button1, GPIO.IN, GPIO.PUD_DOWN)

pwm.start(0)
print("Wait 1 second")
time.sleep(1)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(Servo, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(Servo, False)
    pwm.ChangeDutyCycle(2.5)

SetAngle(0)
time.sleep(5)
SetAngle(120)
pwm.stop()
GPIO.cleanup()

