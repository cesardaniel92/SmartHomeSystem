// This code transmits fake sensor data every 5 seconds.

#include <SoftwareSerial.h>

SoftwareSerial bleModule(2, 3); // RX | TX
int fakeValueMax = 20;
int fakeValue = 0;

void setup() {
    // initialize both serial ports:
    Serial.begin(9600);
    bleModule.begin(9600);
}

void loop() {

  // Generating fake sensor data:
  fakeValue = random(fakeValueMax);
  Serial.write("Transmitting Sensor data...\n");
  bleModule.write(fakeValue);

  delay(5000);    // 5 seconds delay
//  if (Serial.available()) {
//    int inByte = Serial.read();
//    bleModule.write(inByte);
//  }
//
//  if (bleModule.available()) {
//    int inByte = bleModule.read();
//    Serial.write(inByte);
//  }

}
