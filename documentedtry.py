#it will be faster to run this code with a sudo

import wifi
import urllib.request
import os
import subprocess



  
def Search(): #scan for availble networks around
    wifilist = []

    cells = wifi.Cell.all('wlan0') #will list all the networks are nearby 

    for cell in cells:
        wifilist.append(cell)

    return wifilist

class Finder:    #select a network and connect to it with a password
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = """sudo iwlist wlan0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name): #connection function 
        try:
            os.system("nmcli d wifi connect {} password {} iface {}".format(name,
       self.password,
       self.interface_name))
        except:
            raise
        else:
            return True

def internet_on(): #checking the conectivity by trying to open a google url
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        print(' Connected to wifi ')
    except urllib.request.URLError as err:
        print(' DisConnected from wifi ')
        print (Search())
        server_name = input("ssid name: ") #taking the ssid as user input to pass it to the connect function
        password = input("password: ")  #taking the password as user input to pass it to the connect function
        interface_name = "wlan0" # 
        F = Finder(server_name=server_name,
               password=password,
               interface=interface_name)
        F.run()



if __name__ == '__main__':
    
    print (internet_on())



