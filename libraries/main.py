
from ble import *


#\\\\\\\\\\\\  GLOBAL VARIABLES  \\\\\\\\\\\\\\\\

ble = BLE_handler()
ble.addModuleMAC('18:93:d7:14:5e:2b')
ble.addModuleMAC('c8:fd:19:3e:be:7f')

ble.connect()

#\\\\\\\\\\\\  MAIN  \\\\\\\\\\\\\\\\
