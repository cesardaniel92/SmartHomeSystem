#it will be faster to run this code with a sudo

import wifi
import urllib.request
import os
import subprocess




def Search():
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
    

class Finder:
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
            print("Successfully finds entered SSID")

       # for name in ssid_list:
            try:
                result = self.connection()
            except self.connection(self.password) as error:
                print("Couldn't connect check your ssid or password : {}. {}",error)
            else:
                if result:
                    print("Successfully connected to {}".format(self.server_name))

    def connection(self):
        try:
            print('executing nmcli command...')
            os.system("nmcli d wifi connect '{}' password '{}' iface {}".format(self.server_name, self.password, self.interface_name))
        except self.password as error:
            print("wrong password!",error)
            #raise

            return True


def check_connection():
    '''
    This function return True if there is internet Connection
    and False otherwise.
    '''
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)#checking the conectivity by trying to open a google url
        return True
    except urllib.request.URLError as err:
        return False

#***********************connect function that take the ssid and the password and check weather it is online/offline
def connect(ssid, input_password):
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)#checking the conectivity by trying to open a google url
        # print('You are Online')
        raise Exception('device is already online')
    except urllib.request.URLError as err:
        # print('You are offline ')

        # server_name = input("ssid name: ") #taking the ssid as user input to pass it to the connect function
        # password = input("password: ")  #taking the password as user input to pass it to the connect function
        interface_name = "wlan0" #
        F = Finder(server_name=ssid,
               password=input_password,
               interface=interface_name)
        F.run()
        # print(internet_on())
        return True


if __name__ == '__main__':

    #print (connect())
    print(Search())
