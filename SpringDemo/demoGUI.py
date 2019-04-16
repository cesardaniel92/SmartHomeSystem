# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGUI.ui'
#
# Created: Tue Apr 16 11:01:03 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


import sys
sys.path.append('../BLEcomms')
from helperClasses import *

comms = BLE_comms()

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
        SmartHomeSystemv1.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(SmartHomeSystemv1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pressureLabel = QtGui.QLabel(self.centralwidget)
        self.pressureLabel.setObjectName(_fromUtf8("pressureLabel"))
        self.gridLayout.addWidget(self.pressureLabel, 4, 1, 1, 1)
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
        self.pressureLCD = QtGui.QLCDNumber(self.centralwidget)
        self.pressureLCD.setObjectName(_fromUtf8("pressureLCD"))
        self.gridLayout.addWidget(self.pressureLCD, 4, 3, 1, 1)
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
        SmartHomeSystemv1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartHomeSystemv1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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

    def retranslateUi(self, SmartHomeSystemv1):
        SmartHomeSystemv1.setWindowTitle(_translate("SmartHomeSystemv1", "SmartHomeSystem v1.0", None))
        self.pressureLabel.setText(_translate("SmartHomeSystemv1", "Pressure", None))
        self.scanButton.setText(_translate("SmartHomeSystemv1", "Scan BLE devices", None))
        self.disconnectButton.setText(_translate("SmartHomeSystemv1", "Disconnect", None))
        self.tempLabel.setText(_translate("SmartHomeSystemv1", "Temperature", None))
        self.humidityLabel.setText(_translate("SmartHomeSystemv1", "Humidity", None))
        self.connectButton.setText(_translate("SmartHomeSystemv1", "Connect", None))

        # ACTION functions:
    def scanAction(self):
        scan_output = comms.BLE_scan()
        devicesList = comms.get_found_devices(scan_output)
        for device in devicesList:
            self.devicesBox.addItem(device.get_MAC_ADDRESS())


    def connectToSensorModule(self):
        deviceMAC = self.devicesBox.getValue()
        deviceIndex = self.deviceBox.
        device = comms.BLE_connect(deviceMAC)
        device.subscribe (devicesList[connect_selection].handle0x25_UUID, callback=comms.handle_data)
        print "Listening to device data ..."

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SmartHomeSystemv1 = QtGui.QMainWindow()
    ui = Ui_SmartHomeSystemv1()
    ui.setupUi(SmartHomeSystemv1)
    SmartHomeSystemv1.show()
    sys.exit(app.exec_())
