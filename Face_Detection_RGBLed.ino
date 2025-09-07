#include <stdio.h>
#include <cvzone.h>
int potPin = A1;
int potVal = 0;
int rotate_val = 0;
int sendVals[2];

SerialData myserial;
void setup() {
  // put your setup code here, to run once:
myserial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
potVal = analogRead(potPin);
rotate_val = map(potVal, 0,1023,0,360);
sendVals[0] = rotate_val;
myserial.Send(sendVals);
delay(50);
}
