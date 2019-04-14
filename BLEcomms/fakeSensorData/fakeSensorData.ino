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
  delay(5000);    // 5 seconds delay
  // Generating fake sensor data:
  fakeValue = random(fakeValueMax);
//  Serial.write("Transmitting Sensor data: ");
//  Serial.write(fakeValue);
//  Serial.write("\n");
  bleModule.write(fakeValue);
  bleModule.write(fakeValue);
  bleModule.write(fakeValue);

  
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
