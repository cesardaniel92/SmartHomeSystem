
from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import threading
import requests
import time
import binascii


class API_handler:
    '''
    This class contains the functions that communicate to the RestAPI for both
    sensor data and configuration.
    '''
    api_endpoint = 'https://l4gv9uqwpd.execute-api.us-west-1.amazonaws.com/prod/'
    data_uri = api_endpoint + 'sensordata'
    config_uri = api_endpoint + 'configuration'

    def write_data(self, temp, hum, gas, sensor_id, label):
        command = self.data_uri + "?sensorID=" + str(sensor_id) + "&humidity=" + str(hum) + "&temperature=" + str(temp) + "&airQuality=" + str(gas) + "&label=" + str(label)
        requests.put(command)
        # testCommand: sensorID=1&humidity=400&temperature=300&airQuality=500&label=testLabel

    def read_data(self):
        command = self.data_uri
        response = requests.get(command)
        return response.text

    def read_configuration(self):
        command = self.config_uri
        response = requests.get(command)
        return response.text

    def write_configuration(self, user, email, tempT, humT, airQT, notification):
        command = self.config_uri + "?user=" + str(user) + "&email=" + str(email) + "&tempT=" + str(tempT) + "&humT=" + str(humT) + "&airQT=" + str(airQT) + "&notEnabled=" + str(notification).lower()
        # print(command)
        requests.put(command)
        # testCommand: user=test3&email=test@mail.com&tempT=500&humT=500&airQT=500&notEnabled=true


class NotificationDelegate(DefaultDelegate):
    '''
    This class handles the notifications received from the BLE devices.

    Constructor parameters:
    * connection_number = helps with the identification of the connection/thread represented.
    * api = API_handler object that allows for the sensor data received to be written into API.

    '''
    # Class constructor:
    def __init__(self, module_ID, api, label):
        DefaultDelegate.__init__(self)
        self.module_ID = module_ID
        self.api = api
        self.label = label

    # Notification handler:
    def handleNotification(self, cHandle, data):
        # decoding received data:
        val = binascii.b2a_hex(data)

        # validating data lenght:
        if len(val) != 6:
            print('ERROR: wrong length message received ')
        else:
            # parsing decoded sensor data:
            hum = val[:2]
            hum = int(hum, 16)
            temp = val[2:4]
            temp = int(temp, 16)
            airQ = val[4:6]
            airQ = int(airQ, 16)

            # writing to API:
            # print ("Thread/SensorID ",  str(self.module_ID), " with label ", self.label, " writing data into API ...")
            sensor_id = self.module_ID
            self.api.write_data(temp, hum, airQ, sensor_id, self.label)


class ConnectionHandlerThread (threading.Thread):
    '''
        This class represents the threads that handle the connection to BLE devices.
        WHEN THIS CLASS IS NOT IN MAIN, IT FAILS! -> TEMPORALphe
    '''
    # Constructor
    def __init__(self, connection_index, connected_modules, api, label):
        threading.Thread.__init__(self)
        self.connection_index = connection_index
        self.connected_modules = connected_modules
        self.api = api
        self.label = label

    # Start method:
    def run(self):
        # initializing connection object and setting notification delegate:
        connection = self.connected_modules[self.connection_index]
        connection.setDelegate(NotificationDelegate(self.connection_index, self.api, self.label))

        # waiting for sensors to stabilize
        time.sleep(5)

        # infinite loop to throw error if no notifications are received:
        while True:
            if not connection.waitForNotifications(10):
                print ("ERROR: no message received from Sensor")




class BLE_handler:
    '''
    This class handles the communication with the sensor modules through BLE protocol.

    '''
    # Constructor initializing all properties:
    def __init__(self):
        self.modules_MACs = []  # ['18:93:d7:14:5e:2b', 'c8:fd:19:3e:be:7f']
        self.modules_labels = [] # "default0", "default1"
        self.connected_modules = []
        self.connection_threads = []
        self.scanner = Scanner(0)
        self.api = API_handler()
        self.bleDevices = []

    def addModuleMAC(self, new_MAC):
        self.modules_MACs.append(new_MAC)

    def scan(self):
        self.bleDevices = self.scanner.scan(2)

    def connect(self):

        while len(self.connection_threads) < len(self.modules_MACs):
            for d in self.bleDevices:
                if d.addr in self.modules_MACs:
                    p = Peripheral(d)
                    self.connected_modules.append(p)
                    print ('Module ', d.addr , ' connected. Assigned ID = ', str(len(self.connected_modules)-1))

                    module_index = len(self.connected_modules)-1
                    module_label = self.modules_labels[module_index]
                    t = ConnectionHandlerThread(module_index, self.connected_modules, self.api, module_label)
                    t.start()
                    self.connection_threads.append(t)
                    time.sleep(3)   # This delay allows for API calls not to happen too close to eachother.

        print ('All devices are connected.')
