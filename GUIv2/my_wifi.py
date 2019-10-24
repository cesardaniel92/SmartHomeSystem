#it will be faster to run this code with a sudo

import wifi
import urllib.request
import os
import subprocess

# https://www.freebsd.org/cgi/man.cgi?wpa_cli
class WiFi_handler:
    '''
    This class represents the WiFi connection. Its properties are the SSID, password and interface_name
    corresponding to the WiFi connection.
    '''

    # Constructor:
    def __init__(self, *args, **kwargs):
        self.ssid = kwargs['ssid']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']

        # Checking if the wifi interface is ready to be used:
        command = """sudo iwlist wlan0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.ssid))
        result = list(result)

        if "Device or resource busy" in result:
            raise Exception("Device or resource busy")

    # Connecting using wpa_cli tool commands:
    def connect(self):
        # adding network:
        add_network_cmd = 'sudo wpa_cli -i wlan0 add_network'
        network_id = os.popen(add_network_cmd).read().split("\n")[0]

        # setting ssid:
        set_ssid_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " ssid '\"" + self.ssid + "\"'"
        os.system(set_ssid_cmd)

        # setting password:
        set_pwd_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " psk '\"" + self.password + "\"'"
        os.system(set_pwd_cmd)

        # setting protocol:
        set_key_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " key_mgmt WPA-PSK"
        os.system(set_key_cmd)

        # enabling network:
        enable_network_cmd = "sudo wpa_cli -i wlan0 enable_network " + str(network_id)
        os.system(enable_network_cmd)

# end of WiFi_handler class definition #################################################

def check_connection():
    '''
    This function return True if there is internet connection and False otherwise.
    '''
    try:
        # checking the conectivity by trying to open a google url
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False


def connect_to_wifi(input_ssid, input_password):
    '''
    This is the wrapper function that takes the SSID and password as input and
    uses the WiFi_handler to connect to the network.
    '''

    F = WiFi_handler(ssid=input_ssid, password=input_password, interface="wlan0")
    F.connect()


def scan_wifi():
    '''
    This function returns a list of strings corresponding to available SSIDs.
    '''
    wifilist = []
    cells = wifi.Cell.all('wlan0') #will list all the networks are nearby

    for cell in cells:
        wifilist.append(cell)

    list_comma = str(wifilist).split(',')

    result = []
    for line in list_comma:
        split1 = line.split('ssid=')[1]
        result.append(split1.split(')')[0])

    return result
