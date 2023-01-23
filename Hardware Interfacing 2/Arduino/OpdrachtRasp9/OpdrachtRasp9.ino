#include <IRremote.h>
#include <string.h>

const int irPin = 3;
const int raspPin[] = {9, 10, 11, 12};

unsigned long decValue[] = { 4077715200, 3877175040, 2707357440, 4144561920 };

unsigned long newDecValue = 0;

unsigned long prevMillis[] = { 0, 0 };

int count = 0;
int firstPress;
int secondPress;
int lastLed;

IRrecv irrecv(irPin);
decode_results results;

void setup() {
    Serial.begin(9600);
    irrecv.enableIRIn();

    for (int i = 0; i < 4; i++) {
        pinMode(raspPin[i], OUTPUT);
    }
}

void loop() {
    findButtons();

    if (count == 1 && millis() - prevMillis[0] >= 2000)
    {
        // terugzette van verstuurde pin waardoor een nieuwe pin kan worden aangezet
        for (int i = 0; i < 4; i++) {
            digitalWrite(raspPin[i], LOW);
        }
        count = 0;
    }
}


void findButtons() {
    if (irrecv.decode())
    {
        // Ophalen van Value van remote
        newDecValue = (irrecv.decodedIRData.decodedRawData);
        Serial.println(newDecValue);
        for (int i = 0; i < 4; i++)
        {
            // als remotecode overeenkomt met een uit de lijst
            // dan wordt de bijbehorende pin naar HIGH gezet, de raspberry kan dit zien
            if (newDecValue == decValue[i])
            {
                prevMillis[0] = millis();
                digitalWrite(raspPin[i], HIGH);
                lastLed = i;
            }
            irrecv.resume();
        }
    }
}
