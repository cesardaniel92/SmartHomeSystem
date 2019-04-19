# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGUI.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
sys.path.append('/home/pi/Desktop/SmartHomeSystem/BLEcomms')
from helperClasses import *
comms = BLE_comms()
devicesList = []
connectedDeviceIndex = 0

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SmartHomeSystemv1(object):
    def setupUi(self, SmartHomeSystemv1):
        SmartHomeSystemv1.setObjectName(_fromUtf8("SmartHomeSystemv1"))
        SmartHomeSystemv1.resize(400, 300)
        self.centralwidget = QtGui.QWidget(SmartHomeSystemv1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.airQualityLabel = QtGui.QLabel(self.centralwidget)
        self.airQualityLabel.setObjectName(_fromUtf8("airQualityLabel"))
        self.gridLayout.addWidget(self.airQualityLabel, 4, 1, 1, 1)
        self.scanButton = QtGui.QPushButton(self.centralwidget)
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.gridLayout.addWidget(self.scanButton, 0, 0, 1, 1)
        self.disconnectButton = QtGui.QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.gridLayout.addWidget(self.disconnectButton, 5, 0, 1, 1)
        self.humidityLCD = QtGui.QLCDNumber(self.centralwidget)
        self.humidityLCD.setObjectName(_fromUtf8("humidityLCD"))
        self.gridLayout.addWidget(self.humidityLCD, 3, 3, 1, 1)
        self.tempLCD = QtGui.QLCDNumber(self.centralwidget)
        self.tempLCD.setObjectName(_fromUtf8("tempLCD"))
        self.gridLayout.addWidget(self.tempLCD, 2, 3, 1, 1)
        self.airqualityLCD = QtGui.QLCDNumber(self.centralwidget)
        self.airqualityLCD.setObjectName(_fromUtf8("airqualityLCD"))
        self.gridLayout.addWidget(self.airqualityLCD, 4, 3, 1, 1)
        self.tempLabel = QtGui.QLabel(self.centralwidget)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.gridLayout.addWidget(self.tempLabel, 2, 1, 1, 1)
        self.humidityLabel = QtGui.QLabel(self.centralwidget)
        self.humidityLabel.setObjectName(_fromUtf8("humidityLabel"))
        self.gridLayout.addWidget(self.humidityLabel, 3, 1, 1, 1)
        self.devicesBox = QtGui.QComboBox(self.centralwidget)
        self.devicesBox.setObjectName(_fromUtf8("devicesBox"))
        self.gridLayout.addWidget(self.devicesBox, 1, 0, 1, 1)
        self.connectButton = QtGui.QPushButton(self.centralwidget)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.gridLayout.addWidget(self.connectButton, 1, 1, 1, 1)
        self.infoText = QtGui.QLabel(self.centralwidget)
        self.infoText.setText(_fromUtf8(""))
        self.infoText.setObjectName(_fromUtf8("infoText"))
        self.gridLayout.addWidget(self.infoText, 0, 2, 1, 2)
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.gridLayout.addWidget(self.refreshButton, 5, 1, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 5, 3, 1, 1)
        SmartHomeSystemv1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartHomeSystemv1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SmartHomeSystemv1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartHomeSystemv1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartHomeSystemv1.setStatusBar(self.statusbar)

        self.retranslateUi(SmartHomeSystemv1)
        QtCore.QMetaObject.connectSlotsByName(SmartHomeSystemv1)

        # ACTIONS configuration:
        self.scanButton.clicked.connect(self.scanAction)
        self.connectButton.clicked.connect(self.connectToSensorModule)
        self.refreshButton.clicked.connect(self.refreshData)
        self.quitButton.clicked.connect(self.exitGUI)

    def retranslateUi(self, SmartHomeSystemv1):
        SmartHomeSystemv1.setWindowTitle(_translate("SmartHomeSystemv1", "SmartHomeSystem v1.0", None))
        self.airQualityLabel.setText(_translate("SmartHomeSystemv1", "Air Quality", None))
        self.scanButton.setText(_translate("SmartHomeSystemv1", "Scan BLE devices", None))
        self.disconnectButton.setText(_translate("SmartHomeSystemv1", "Disconnect", None))
        self.tempLabel.setText(_translate("SmartHomeSystemv1", "Temperature (C)", None))
        self.humidityLabel.setText(_translate("SmartHomeSystemv1", "Humidity (%)", None))
        self.connectButton.setText(_translate("SmartHomeSystemv1", "Connect", None))
        self.refreshButton.setText(_translate("SmartHomeSystemv1", "Refresh", None))
        self.quitButton.setText(_translate("SmartHomeSystemv1", "Quit", None))

    # ACTION functions:
    def scanAction(self):
        global devicesList
        global comms
        self.infoText.setText("Scanning ...")

        scan_output = comms.BLE_scan()
        devicesList = comms.get_found_devices(scan_output)
        for device in devicesList:
            self.devicesBox.addItem(device.get_MAC_ADDRESS())

        self.infoText.setText("Scanning complete.")

    def connectToSensorModule(self):
        global devicesList
        global deviceIndex

        deviceMAC = self.devicesBox.currentText()
        self.infoText.setText("Connecting ...")
        # Getting device index:
        for index in range(len(devicesList)):
            if devicesList[index].get_MAC_ADDRESS() == deviceMAC:
                connectedDeviceIndex = index

        device = comms.BLE_connect(deviceMAC)
        print "DeviceIndex: ", connectedDeviceIndex
        print "devicesList size: ", len(devicesList)
        devicesList[connectedDeviceIndex].print_BLE_device()
        device.subscribe (devicesList[connectedDeviceIndex].handle0x25_UUID, callback=comms.handle_data)
        self.infoText.setText("Connection complete.")

    def refreshData(self):
        global devicesList
        global connectedDeviceIndex
        global comms

        allHex = comms.lastValue
        hum = allHex[0] # + allHex[1]
        temp = allHex[1] # + allHex[3]
        gas = allHex[2] # + allHex[5]

        self.humidityLCD.display(hum)
        self.tempLCD.display(temp)
        self.airQualityLCD.display(gas)

        comms.print_buffer()

    def exitGUI(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SmartHomeSystemv1 = QtGui.QMainWindow()
    ui = Ui_SmartHomeSystemv1()
    ui.setupUi(SmartHomeSystemv1)
    SmartHomeSystemv1.show()
    sys.exit(app.exec_())
