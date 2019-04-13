
from helperClasses import *


# MAIN CODE:
comms = BLE_comms()
choice = 0  # Menu choice:

while True:
    printMenu()
    # print
    selection = int(input("Enter your choice: "))

    # Input validation pending!

    if selection == 1:
        print "Scanning BLE devices...\n"
        scan_output = comms.BLE_scan()
        devicesList = comms.get_found_devices(scan_output)
        print "Devices found:"
        i = 0
        for device in devicesList:
            print i, ") ", device.print_BLE_device()
            i += 1
    if selection == 2:
        # print "Enter device number you want to connect to:"
        connect_selection = int(input("Enter device number you want to connect to:"))
        device = comms.BLE_connect(devicesList[connect_selection].get_MAC_ADDRESS())
        device.subscribe (devicesList[connect_selection].handle0x25_UUID, callback=comms.handle_data)
        print "Listening to device data ..."
    if selection == 3:
        print "PENDING!"
    if selection == 4:
        comms.print_buffer()
    if selection == 5:
        break
