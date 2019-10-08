
from ble import *

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


#\\\\\\\\\\\\  GLOBAL VARIABLES  \\\\\\\\\\\\\\\\

ble = BLE_handler()
ble.addModuleMAC('18:93:d7:14:5e:2b')
ble.addModuleMAC('c8:fd:19:3e:be:7f')

ble.connect()
#\\\\\\\\\\\\  MAIN  \\\\\\\\\\\\\\\\
