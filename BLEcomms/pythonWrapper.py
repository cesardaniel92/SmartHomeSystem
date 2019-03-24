
import subprocess
import signal
import time

# Class represents the BLE devices found in scan. It simplifies manipulation and display in the GUI.
class BLE_device:
    name = ""
    MAC_address = ""

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


# This function scans for 5 seconds and displays the list of devices found if no error occurs.
def BLE_scan():
    scan = subprocess.Popen(["hcitool","lescan"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(5)
    scan.send_signal(signal.SIGINT) # Stopping the scan after 5 seconds.
    output,error = scan.communicate()

    if not error:
        return output
    else:
        raise error

# This function returns a list of the devices found by BLE_scan:
def get_found_devices(scan_output):

    lines = scan_output.split("\n")
    listOfDevices = []
    for i in range(1,len(lines)-1): # Ignoring first and last line
        parameters = lines[i].split()
        tempDevice = BLE_device(parameters[1], parameters[0])
        listOfDevices.append(tempDevice)
    return listOfDevices


# MAIN CODE:

print "Scanning BLE devices...\n"
scan_output = BLE_scan()
devicesList = get_found_devices(scan_output)

print "Devices found:"
for device in devicesList:
    device.print_BLE_device()
