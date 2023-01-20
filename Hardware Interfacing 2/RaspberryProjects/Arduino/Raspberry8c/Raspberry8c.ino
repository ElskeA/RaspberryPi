const int ledPin[] = {2, 4};
const int raspPin2 = 7;
const int raspOut = 12;
int pinstate = LOW;
int btnPin = 9;
int btnstate = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin[0], OUTPUT);
  pinMode(ledPin[1], OUTPUT);
  pinMode(raspPin2, OUTPUT);
  pinMode(raspOut, INPUT);
  pinMode(btnPin, INPUT);
}

void loop() {
//  Als de button is ingedrukt wordt de pin die naar de raspberry loopt op 
//  High gezet, zodat de raspberry dit kan inlezen. 
    if(digitalRead(btnPin) == HIGH){
        if(btnstate == 1){
              digitalWrite(raspPin2, HIGH);
//              Buttonstate resetten voordat de loop opnieuw begint
              btnstate = 0;
      }else if(btnstate == 0){
            digitalWrite(raspPin2, LOW);
//            Buttonstate aanpassen naar 1 voordat de loop opnieuw begint
            btnstate = 1;       
        }
    }
//    Dan wordt de pin uitgelezen die van de raspberry naar de arduino loopt
//    Als deze op high staat switchen de leds. De ene gaat aan de andere gaat uit
      if(digitalRead(raspOut) == HIGH){
        digitalWrite(ledPin[0], LOW);
        digitalWrite(ledPin[1], HIGH);
      }else if (digitalRead(raspOut) == LOW){
          digitalWrite(ledPin[0], HIGH);
          digitalWrite(ledPin[1], LOW);
        }
   
} 
