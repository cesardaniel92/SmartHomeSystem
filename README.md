![Smart Home Systems Architecture](https://github.com/cesardaniel92/SmartHomeSystem/architecture.png)

# Smart Home System using Raspberry Pi
Using Sensor Modules powered by Arduino Nano, this system will sample parameters like temperature, humidity and air quality and transfer it wireless to a Control Unit powered by Raspberry Pi 3 B+ with a 3.5 inch touch-screen running a Graphic User Interface. This data will be available through a Restful API supported by AWS.

## Main Features:
- Live sensor data displayed in the Control Unit through GUI.
- Data available in Restful API.
- Programmable notifications.

## Hardware:
- SH-HC-10: BLE module for wireless communication between Sensor Modules and Control Unit (Raspberry Pi).
- Arduino Nano: powers the Sensor Modules.
- Raspberry Pi 3 B+: powers the Control Unit where the data processing and main features are implemented.

## Directories:
**3DModel:** Contains files related to the 3D print of a case for the sensor modules where we will place the Arduino Nano board, sensors, etc.

**AWS:** Contains all documentation for the AWS architecture used around the Restful API and the AWS Lambda functions code.

**BLEcomms:** Contains the code for the initial communication. It has a basic Arduino code to send AT commands to the HC-10 module and the commands to connect and read to it from the Terminal in the Raspberry Pi.

**Documentation:** Contains files with resources that will be used to properly document the project and build a comprehensive User Manual at the end of the project.

**Graphic User Interface:** Contains the files related to the design of the GUI.

**Sensor module:** Contains the Arduino code files.

**SpringDemo:** Contains all files and code that was used for the Demo at the end of Spring 2019 semester.


#Potential Dependencies:
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module
sudo apt-get install --reinstall overlay-scrollbar-gtk2


# Raspberry Pi Setup Documentation:

### GUI setup:
Since we are using PyQt4 and other libraries in our GUI code, we need to run a few commands to make sure they are supported and the code does not fail.

```shell
sudo apt-get install python-qt4
pip install pygatt
pip install pexpect
```

### Code Update:
In order to run "updateCode.sh", first we need to run:

```shell
sudo apt-get install xterm
```


### Remote Control Setup:
First, vnc server must be installed **on the Pi** by running:
```shell
sudo apt-get install tightvncserver
```
Then we activate the server by running:
```shell
vncserver -nolisten tcp -nevershared -dontdisconnect :1
```
This command will prompt you for a password that you will need from the client side to connect.

Once this is setup, we can remote control the Pi screen from our own OS.
