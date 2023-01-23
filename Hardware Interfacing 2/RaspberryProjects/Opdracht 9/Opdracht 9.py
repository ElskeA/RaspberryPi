import RPi.GPIO as GPIO
import time

# Deze opdracht is met behulp van Eloi, Lincy, Joost en Jeremy gemaakt

ledPin = [5, 6, 13, 26]
arduinoPins = [17, 4, 3, 2]
blinkTimes = [100, 400, 600, 800]
vorigetijd = [0, 0, 0, 0]
vorigeLedInput = -1
ledPinStatus = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
blinkSelect = [0, 0, 0, 0]
vorigeLed = [0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin[0], GPIO.OUT)
GPIO.setup(ledPin[1], GPIO.OUT)
GPIO.setup(ledPin[2], GPIO.OUT)
GPIO.setup(ledPin[3], GPIO.OUT)

GPIO.setup(arduinoPins[0], GPIO.IN, GPIO.PUD_UP)
GPIO.setup(arduinoPins[1], GPIO.IN, GPIO.PUD_UP)
GPIO.setup(arduinoPins[2], GPIO.IN, GPIO.PUD_UP)
GPIO.setup(arduinoPins[3], GPIO.IN, GPIO.PUD_UP)

def millis():
    return time.time() * 1000

# Er wordt gekeken of de status van
# een LED aan of uit is. Als het ledje uit is
# worden alle andere leds die aan staan uitgezet.
def checkLed(led, tijd):
    if vorigeLed[led] == 0:
        s = 0
        for i in vorigeLed:
            if i == 2:
                ledPinStatus[s] = GPIO.LOW
                vorigeLed[s] = 0
                GPIO.output(ledPin[s], GPIO.LOW)
            if i == 1:
                vorigeLed[s] = 2
            s += 1
        ledPinStatus[led] = GPIO.HIGH
        vorigeLed[led] = 1
        GPIO.output(ledPin[led], GPIO.HIGH)

    # adhv de blinkTimes wordt de blinkSelect aangepast
    blinkSelect[led] = blinkTimes[tijd]
    blinkLed(led)



def blinkLed(led):
    # millis worden gebruikt om de huidigetijd variabele aan te passen
    huidigetijd = millis()
    # Controleert of de huidige tijd min de vorigetijddat de led knipperde groter of
    # gelijk is aan de geselcteerde kniiper tijd en of de vorige LED status groter of gelijk is
    # aan 1
    if huidigetijd - vorigetijd[led] >= blinkSelect[led] and vorigeLed[led] >= 1:
        # Update vorige tijd met huidige tijd
        vorigetijd[led] = huidigetijd
        # Controleer huidige status LED pin
        if ledPinStatus[led] == GPIO.LOW:
            ledPinStatus[led] = GPIO.HIGH
        else:
            ledPinStatus[led] = GPIO.LOW
        GPIO.output(ledPin[led], ledPinStatus[led])


# Wanneer de pinstatus op HIGH staat, wordt er gekeken of er al een LED geselecteerd was.
# Als dit het geval is, wordt de checkLed() functie uitgevoerd met de geselecteerde LED en de
# index van de snelheid. Als er geen LED geselecteerd was, wordt de huidige pin als
# de geselecteerde LED opgeslagen.
def ledInput(i):
    global vorigeLedInput
    pinstatus = GPIO.input(arduinoPins[i])
    if pinstatus == GPIO.HIGH:
        if vorigeLedInput > -1:
            checkLed(vorigeLedInput, i)
            vorigeLedInput = -1
        else:
            vorigeLedInput = i

checkLed(0, 0)
checkLed(1, 0)

while True:
    #Doorloopt elke led in the while loop
    for i in range(4):
        blinkLed(i)
        ledInput(i)
    time.sleep(0.1)
