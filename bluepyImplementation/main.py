
# from helpers import *

from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import threading
import requests
import time
import binascii

class NotificationDelegate(DefaultDelegate):

    def __init__(self, number):
        DefaultDelegate.__init__(self)
        self.number = number

    def handleNotification(self, cHandle, data):
        val = binascii.b2a_hex(data)
        if len(val) != 6:
            print 'ERROR: wrong length message received (size = ' + len(val) + ').'
        else:
            hum = val[:2]
            hum = int(hum, 16)
            temp = val[2:4]
            temp = int(temp, 16)
            airQ = val[4:6]
            airQ = int(airQ, 16)
            print 'Sensor ID: ' + str(self.number) + ' \tTemperature: ' + str(temp) + ' \tHumidity: ' + str(hum) + ' \tAirQuality: ' + str(airQ)
            print 'Writing to API ... '
            sensor_id = self.number
            api.write_data(temp, hum, airQ, sensor_id)

class ConnectionHandlerThread (threading.Thread):
    def __init__(self, connection_index):
        threading.Thread.__init__(self)
        self.connection_index = connection_index

    def run(self):
        connection = connected_modules[self.connection_index]
        connection.setDelegate(NotificationDelegate(self.connection_index))
        time.sleep(5)  # Waiting for sensors to stabilize
        while True:
            if not connection.waitForNotifications(10):
                print "ERROR: no message received from Sensor ID " + str(self.connection_index)

class API_handler:
    data_uri = 'https://l4gv9uqwpd.execute-api.us-west-1.amazonaws.com/prod/sensordata'
    config_uri = 'PENDING'

    def write_data(self, temp, hum, gas, sensor_id):
        command = self.data_uri + "?sensorID= " + str(sensor_id) + "&humidity=" + str(hum) + "&temperature=" + str(temp) + "&airQuality=" + str(gas)
        requests.put(command)

    def read_data(self):
        command = self.data_uri
        requests.get(command)

#\\\\\\\\\\\\  GLOBAL VARIABLES  \\\\\\\\\\\\\\\\

modules_MACs = ['18:93:d7:14:5e:2b', 'c8:fd:19:3e:be:7f']
connected_modules = []
connection_threads = []
scanner = Scanner(0)
api = API_handler()

#\\\\\\\\\\\\  MAIN  \\\\\\\\\\\\\\\\
while len(connection_threads) < len(modules_MACs):
    print 'Scanning...'
    devices = scanner.scan(2)
    for d in devices:
        if d.addr in modules_MACs:
            p = Peripheral(d)
            connected_modules.append(p)
            print 'Module ' + d.addr + ' connected. Assigned ID = ' + str(len(connected_modules)-1)
            t = ConnectionHandlerThread(len(connected_modules)-1)
            t.start()
            connection_threads.append(t)
            # time.sleep(7)

print 'All devices are connected.'
