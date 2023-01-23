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
//    De pin wordt uitgelezen, als de pin 1 is dan gaat de ledpin op low
//    De ledpin wordt weer uitgelezen door de raspberry om de leds aan of uit te zetten
    digitalWrite(ledPin, LOW);
  }
  else if (inputValue == 0) {
//    Is de pin op 0, dan wordt de ledpin op HIGH gezet
    digitalWrite(ledPin, HIGH);
  }
}
