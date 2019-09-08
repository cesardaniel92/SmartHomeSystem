/*
 * Working Arduino code for NANO board.
 * */

#include <SoftwareSerial.h>

#include "DHT.h";

#define DHT_PIN 2
#define DHTTYPE DHT11 // DHT type is DHT 11

#define sensor    A0                      //sensor on Analog 0

DHT dht(DHT_PIN, DHTTYPE);

float hum; //Stores humidity value
float temp; // Stores temp value

int gasLevel = 0;     //int variable for gas level

// SoftwareSerial bleModule(0, 1); // RX | TX

void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
  // bleModule.begin(9600);
  dht.begin();
  pinMode(sensor,INPUT);      //set sensor for input
}

void loop() {

  delay(3000); //Delay so sensor can stablize

  // Temp and humidity (DHT 11)
  hum = dht.readHumidity(); // Get humidity value
  temp= dht.readTemperature(); // Get Temperature value
  gasLevel = analogRead(sensor);

  float test = 3.5;

  Serial.write((int)hum);
  Serial.write((int)temp);
  Serial.write(gasLevel);

}
