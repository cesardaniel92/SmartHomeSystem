#it will be faster to run this code with a sudo

import wifi
import urllib.request
import os
import subprocess

# https://www.freebsd.org/cgi/man.cgi?wpa_cli


class Finder:
    def __init__(self, *args, **kwargs):
        self.ssid = kwargs['ssid']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}
    
        command = """sudo iwlist wlan0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.ssid))
        result = list(result)

        if "Device or resource busy" in result:
            raise Exception("Device or resource busy")
        

    def connect(self):
        # adding network:
        add_network_cmd = 'sudo wpa_cli -i wlan0 add_network'
        # print("executing ", add_network_cmd)
        network_id = os.popen(add_network_cmd).read().split("\n")[0]

        # setting ssid:
        set_ssid_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " ssid '\"" + self.ssid + "\"'"
        # print("executing ", set_ssid_cmd)
        os.system(set_ssid_cmd)

        # setting password:
        set_pwd_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " psk '\"" + self.password + "\"'"
        # print("executing ", set_pwd_cmd)
        os.system(set_pwd_cmd)

        # setting protocol:
        set_key_cmd = "sudo wpa_cli -i wlan0 set_network " + str(network_id) + " key_mgmt WPA-PSK"
        # print("executing ", set_key_cmd)
        os.system(set_key_cmd)

        # enabling network:
        enable_network_cmd = "sudo wpa_cli -i wlan0 enable_network " + str(network_id)
        # print("executing ", enable_network_cmd)
        os.system(enable_network_cmd)

def check_connection():
    '''
    This function return True if there is internet Connection
    and False otherwise.
    '''
    try:
        # checking the conectivity by trying to open a google url
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False



def connect_to_wifi(input_ssid, input_password):
    
    F = Finder(ssid=input_ssid, password=input_password, interface="wlan0")        
    F.connect()
        
          

def scan_wifi():
    '''
    Search function all returns a list of available SSIDs in string format even if it's connected
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



# if __name__ == '__main__':
#
#     connect('ACR5G_5GEXT', 'Ringo@1128')
