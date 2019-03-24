# Smart Home System using Raspberry Pi
Using Sensor Modules powered by Arduino Nano, this system will sample parameters like temperature, humidity and air quality and transfer it wireless to a Control Unit powered by Raspberry Pi 3 B+ with a 3.5 inch touch-screen running a Graphic User Interface.  

## Main Features:
- Live sensor data displayed in the Control Unit through GUI.
- Data available in Restful API.
- Programmable notifications.

## Hardware:
- SH-HC-10: BLE module for wireless communication between Sensor Modules and Control Unit (Raspberry Pi).
- Arduino Nano: powers the Sensor Modules.
- Raspberry Pi 3 B+: powers the Control Unit where the data processing and main features are implemented.

## Directories:
**BLEcomms:** Contains the code for the initial communication. It has a basic Arduino code to send AT commands to the HC-10 module and the commands to connect and read to it from the Terminal in the Raspberry Pi.
