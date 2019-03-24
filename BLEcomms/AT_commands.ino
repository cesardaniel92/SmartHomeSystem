// Simple code that allows to execute AT commands on the BLE module through
// the serial monitor.

#include <SoftwareSerial.h>

SoftwareSerial bleModule(2, 3); // RX | TX

void setup() {
    // initialize both serial ports:
    Serial.begin(9600);
    bleModule.begin(9600);
}

void loop() {

  if (Serial.available()) {
    int inByte = bleModule.read();
    bleModule.write(inByte);
  }

  if (bleModule.available()) {
    int inByte = bleModule.read();
    Serial.write(inByte);
  }

}
