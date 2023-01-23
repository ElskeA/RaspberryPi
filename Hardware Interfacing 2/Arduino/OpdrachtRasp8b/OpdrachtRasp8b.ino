const int ledPin[] = {2, 4};
const int raspPin = 11;
const int raspPin2 = 8;
unsigned long lastTimes[] = {0, 0};
int ledStatus[] = {LOW, LOW};
int pinstate1 = 0;
int pinstate2 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin[0], OUTPUT);
  pinMode(ledPin[1], OUTPUT);
  pinMode(raspPin, INPUT);
}

void loop() {  
//  Uitlezen van de raspberry pinnen en opslaan in variabele
  pinstate1 = digitalRead(raspPin);
  pinstate2 = digitalRead(raspPin2);
  Serial.println(pinstate1);
  Serial.println(pinstate2);
//  De pin zal een bepaalde tijd op high staan door de methode vanuit
// de raspberry. Zolang deze pin op high staat, wordt de led ook aangezet
  if(pinstate1 == HIGH){
    digitalWrite(ledPin[0], HIGH);
  }else if(pinstate1 == LOW){
     digitalWrite(ledPin[0], LOW);
    }
//    Hetzelfde gebeurd bij deze pin, maar met een andere knippersnelheid
//    die door de raspberry pi wordt doorgecommuniceerd
    if(pinstate2 == HIGH){
      digitalWrite(ledPin[1], HIGH);
  }else if(pinstate2 == LOW){
     digitalWrite(ledPin[1], LOW);
    }
      }
