
from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import threading
import requests
import time
import binascii


class NotificationDelegate(DefaultDelegate):
    '''
    This class handles the notifications received from the BLE devices.

    Constructor parameters:
    * connection_number = helps with the identification of the connection/thread represented.
    * api = API_handler object that allows for the sensor data received to be written into API.

    '''
    # Class constructor:
    def __init__(self, connection_number, api):
        DefaultDelegate.__init__(self)
        self.connection_number = connection_number
        self.api = api

    # Notification handler:
    def handleNotification(self, cHandle, data):
        # decoding received data:
        val = binascii.b2a_hex(data)

        # validating data lenght:
        if len(val) != 6:
            print 'ERROR: wrong length message received (size = ' + len(val) + ').'
        else:
            # parsing decoded sensor data:
            hum = val[:2]
            hum = int(hum, 16)
            temp = val[2:4]
            temp = int(temp, 16)
            airQ = val[4:6]
            airQ = int(airQ, 16)

            # outputting data for troubleshooting purposes:
            print 'Thread/SensorID: ' + str(self.connection_number) + ' \tTemperature: ' + str(temp) + ' \tHumidity: ' + str(hum) + ' \tAirQuality: ' + str(airQ)

            # writing to API:
            print 'Thread/SensorID: ' + str(self.connection_number) + ' writing data into API ...'
            sensor_id = self.connection_number
            self.api.write_data(temp, hum, airQ, sensor_id)


class ConnectionHandlerThread (threading.Thread):
    '''
        This class represents the threads that handle the connection to BLE devices.
        WHEN THIS CLASS IS NOT IN MAIN, IT FAILS! -> TEMPORAL
    '''
    # Constructor
    def __init__(self, connection_index, connected_modules, api):
        threading.Thread.__init__(self)
        self.connection_index = connection_index
        self.connected_modules = connected_modules
        self.api = api

    # Start method:
    def run(self):
        # initializing connection object and setting notification delegate:
        connection = self.connected_modules[self.connection_index]
        connection.setDelegate(NotificationDelegate(self.connection_index, self.api))

        # waiting for sensors to stabilize
        time.sleep(5)

        # infinite loop to throw error if no notifications are received:
        while True:
            if not connection.waitForNotifications(10):
                print "ERROR: no message received from Sensor ID " + str(self.connection_index)


class API_handler:
    '''
    This class contains the functions that communicate to the RestAPI for both
    sensor data and configuration.
    '''

    api_endpoint = 'https://l4gv9uqwpd.execute-api.us-west-1.amazonaws.com/prod/'
    data_uri = api_endpoint + 'sensordata'
    config_uri = api_endpoint + 'configuration'

    def write_data(self, temp, hum, gas, sensor_id):
        command = self.data_uri + "?sensorID= " + str(sensor_id) + "&humidity=" + str(hum) + "&temperature=" + str(temp) + "&airQuality=" + str(gas)
        requests.put(command)

    def read_data(self):
        command = self.data_uri
        requests.get(command)


class BLE_handler:
    '''
    This class handles the communication with the sensor modules through BLE protocol.

    '''
    # Constructor initializing all properties:
    def __init__(self):
        # modules_MACs = ['18:93:d7:14:5e:2b', 'c8:fd:19:3e:be:7f']
        self.modules_MACs = []
        self.connected_modules = []
        self.connection_threads = []
        self.scanner = Scanner(0)
        self.api = API_handler()
        self.apiWrite = False

    def addModuleMAC(self, new_MAC):
        self.modules_MACs.append(new_MAC)

    def connect(self):
        while len(self.connection_threads) < len(self.modules_MACs):
            print 'Scanning ...'
            devices = self.scanner.scan(2)
            for d in devices:
                if d.addr in self.modules_MACs:
                    p = Peripheral(d)
                    self.connected_modules.append(p)
                    print 'Module ' + d.addr + ' connected. Assigned ID = ' + str(len(self.connected_modules)-1)
                    t = ConnectionHandlerThread(len(self.connected_modules)-1, self.connected_modules, self.api)
                    t.start()
                    self.connection_threads.append(t)
                    # time.sleep(3)

        print 'All devices are connected.'
