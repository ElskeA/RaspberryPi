int Raspberry_PIN = 8;
int ledPin = 12;

void setup() {
//  Deze pin wordt high of low gezet door de raspberry pi
  pinMode(Raspberry_PIN, INPUT);
//  deze pin wordt gebruikt om de leds aan en uit te zetten
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int inputValue = digitalRead(Raspberry_PIN);
  if (inputValue == 1) {
//    De pin wordt uitgelezen, als de pin low is of 0, dan gaat de ledpin ook op low
//    als de pin hoog is dan wordt de ledpin aangezet. 
    digitalWrite(ledPin, LOW);
  }
  else if (inputValue == 0) {
    digitalWrite(ledPin, HIGH);
  }
}
