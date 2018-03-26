const int trigPinL=5;
const int echoPinL=4;
const int trigPinR = 7;
const int echoPinR = 6;
const int ledRechts = 3;
const int ledLinks = 2;
int teller = 0;
int startLinks, startRechts;
long durationL, durationR;
int distanceL, distanceR;

void setup() {
  pinMode(trigPinL, OUTPUT);
  pinMode(echoPinL, INPUT);
  pinMode(trigPinR, OUTPUT);
  pinMode(echoPinR, INPUT);
  pinMode(ledRechts, OUTPUT);
  pinMode(ledLinks, OUTPUT);
  Serial.begin(9600);  
}

void loop() {
  digitalWrite(trigPinL, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPinL, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinL, LOW);
  durationL= pulseIn(echoPinL, HIGH);
  distanceL= durationL *(0.0343/2);
  delay(100);
  digitalWrite(trigPinR, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPinR, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinR, LOW);
  durationR= pulseIn(echoPinR, HIGH);
  distanceR= durationR *(0.0343/2);
  delay(100);

  if(teller == 0){
    startLinks = distanceL;
    startRechts = distanceR;
  }

  if(distanceL + startRechts/2 < distanceR){
    Serial.println("LINKS");
    digitalWrite(ledLinks, HIGH);
    digitalWrite(ledRechts, LOW);
  } else if(distanceR + startLinks/2 < distanceL){
    Serial.println("RECHTS");
    digitalWrite(ledRechts, HIGH);
    digitalWrite(ledLinks, LOW);
  } else {
    Serial.println("RECHTDOOR");
    digitalWrite(ledLinks, LOW);
    digitalWrite(ledRechts, LOW);
  }
}
