import pygatt
import subprocess
import signal
import time
from binascii import hexlify

# Class represents the BLE devices found in scan. It simplifies manipulation and display in the GUI.
class BLE_device:
    name = ""
    MAC_address = ""
    handle0x25_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"


    def __init__(self, new_name, new_MAC):
        self.name = new_name
        self.MAC_ADDRESS = new_MAC

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_MAC_ADDRESS(self, new_MAC):
        self.MAC_ADDRESS = new_MAC

    def get_MAC_ADDRESS(self):
        return self.MAC_ADDRESS

    def print_BLE_device(self):
        print "Name: ", self.name, "\t MAC_ADDRESS: ", self.MAC_ADDRESS

    # def set_UUID(self):   # PENDING!



class BLE_comms:
    buffer = []
    lastValue = 0

    # This function scans for 5 seconds and displays the list of devices found if no error occurs.
    def BLE_scan(self):
        scan = subprocess.Popen(["hcitool","lescan"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(5)
        scan.send_signal(signal.SIGINT) # Stopping the scan after 5 seconds.
        output,error = scan.communicate()

        if not error:
            return output
        else:
            raise error

    # This function returns a list of the devices found by BLE_scan:
    def get_found_devices(self, scan_output):
        lines = scan_output.split("\n")
        listOfDevices = []
        for i in range(1,len(lines)-1): # Ignoring first and last line
            parameters = lines[i].split()
            tempDevice = BLE_device(parameters[1], parameters[0])
            listOfDevices.append(tempDevice)
        return listOfDevices

    def reset_hci0(self):
        turn_off = subprocess.Popen(["hcitool","lescan"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        off_output, off_error = turn_off.communicate()
        turn_on = subprocess.Popen(["hcitool","lescan"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        on_output, on_error = turn_on.communicate()

        if on_error:
            raise on_error
        elif off_error:
            raise off_error
        else:
            print "hci0 interface reset."

    def BLE_connect(self, MAC_address):
        print 'Connecting to ', MAC_address , ' ...'
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(MAC_address)
        return device

    def handle_data(self, handle, value):
        """
        handle -- integer, characteristic read handle the data was received on
        value -- bytearray, the data returned in the notification
        """
        self.buffer.append(value)
        self.lastValue = value
        # print("Received data: %s" % hexlify(value))

    def print_buffer(self):
        print("Buffer:")
        for item in self.buffer:
            print "%s" % hexlify(item)

        print "Last Sensor Values:"
        allHex = self.buffer[len(self.buffer)-1]
        hum = allHex[0] # + allHex[1]
        temp = allHex[1] # + allHex[3]
        gas = allHex[2] # + allHex[5]

        print "Humidity: %s", hum
        print "Temp: %s", temp
        print "Gas: %s", gas


# Helper Functions:

def printMenu():
    # Menu:
    print "///// Capstone Control Unit Menu: /////"
    print "1- Scan BLE devices."
    print "2- Connect to a found BLE device."
    print "3- Disconnect."
    print "4- Show Buffer and lastValue read."
    print "5- Quit."
