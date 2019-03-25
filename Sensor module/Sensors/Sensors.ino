
#include "DHT.h";

#define DHT_PIN 7
#define DHTTYPE DHT11 // DHT type is DHT 11 

#define sensor    A0                      //sensor on Analog 0

DHT dht(DHT_PIN, DHTTYPE);

float hum; //Stores humidity value
float temp; // Stores temp value

int gasLevel = 0;     //int variable for gas level
String quality ="";

void setup() {

 Serial.begin(9600);
 dht.begin();
 pinMode(sensor,INPUT);      //set sensor for input

}


void loop() {

 
  delay(2000); //Delay so sensor can stablize

  // Temp and humidity (DHT 11)
  hum = dht.readHumidity(); // Get humidity value
  temp= dht.readTemperature(); // Get Temperature value

  gasLevel = analogRead(sensor);
  
  //Air quality (MQ 130)
   if(gasLevel<175){
    quality = "GOOD!    ";
  }
  else if (gasLevel >175 && gasLevel<225){
    quality = "poor   ";
  }
  else if (gasLevel >225 && gasLevel<300){
    quality = "Bad";
  }
  else if (gasLevel >300){
    quality = "Exteremly bad ";
  }
  

  //Print values to serial monitor

  Serial.print("Humidity: ");
  Serial.print(hum);
  Serial.print(" %, Temperature: ");
  Serial.print(temp);
  Serial.println(" Celsius ");

  Serial.print("Air Quality is:");
  Serial.print(quality);
  Serial.println(" ");
  Serial.print("Gas level: ");
  Serial.println(gasLevel);
}
