# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ble import *
from my_wifi import *

import sys
import requests
import threading
import time

ble = BLE_handler()

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

class Ui_SmartHomeSystem(object):
    def setupUi(self, SmartHomeSystem):
        SmartHomeSystem.setObjectName(_fromUtf8("SmartHomeSystem"))
        SmartHomeSystem.resize(850, 638)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SmartHomeSystem.sizePolicy().hasHeightForWidth())
        SmartHomeSystem.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(SmartHomeSystem)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 701, 481))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.InternetSetup = QtGui.QWidget()
        self.InternetSetup.setObjectName(_fromUtf8("InternetSetup"))
        self.gridLayoutWidget = QtGui.QWidget(self.InternetSetup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(39, 39, 611, 371))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ScanWiFi = QtGui.QPushButton(self.gridLayoutWidget)
        self.ScanWiFi.setObjectName(_fromUtf8("ScanWiFi"))
        self.gridLayout.addWidget(self.ScanWiFi, 1, 1, 1, 1)
        self.passwordField = QtGui.QLineEdit(self.gridLayoutWidget)
        self.passwordField.setObjectName(_fromUtf8("passwordField"))
        self.gridLayout.addWidget(self.passwordField, 6, 1, 1, 1)
        self.ConnectToWiFi = QtGui.QPushButton(self.gridLayoutWidget)
        self.ConnectToWiFi.setObjectName(_fromUtf8("ConnectToWiFi"))
        self.gridLayout.addWidget(self.ConnectToWiFi, 7, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.WiFiList = QtGui.QListWidget(self.gridLayoutWidget)
        self.WiFiList.setObjectName(_fromUtf8("WiFiList"))
        self.gridLayout.addWidget(self.WiFiList, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 5, 1, 1, 1)
        self.tabWidget.addTab(self.InternetSetup, _fromUtf8(""))
        self.ModuleSetup = QtGui.QWidget()
        self.ModuleSetup.setObjectName(_fromUtf8("ModuleSetup"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.ModuleSetup)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 611, 351))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.SensorModulesSelected = QtGui.QLabel(self.gridLayoutWidget_3)
        self.SensorModulesSelected.setObjectName(_fromUtf8("SensorModulesSelected"))
        self.gridLayout_3.addWidget(self.SensorModulesSelected, 1, 3, 1, 1)
        self.BLEList = QtGui.QListWidget(self.gridLayoutWidget_3)
        self.BLEList.setObjectName(_fromUtf8("BLEList"))
        self.gridLayout_3.addWidget(self.BLEList, 2, 1, 1, 1)
        self.ScanBLE = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.ScanBLE.setObjectName(_fromUtf8("ScanBLE"))
        self.gridLayout_3.addWidget(self.ScanBLE, 1, 1, 1, 1)
        self.SelectSensorModule = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.SelectSensorModule.setObjectName(_fromUtf8("SelectSensorModule"))
        self.gridLayout_3.addWidget(self.SelectSensorModule, 2, 2, 1, 1)
        self.ConnectToBLEDevices = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.ConnectToBLEDevices.setObjectName(_fromUtf8("ConnectToBLEDevices"))
        self.gridLayout_3.addWidget(self.ConnectToBLEDevices, 3, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.ModulesSelectedList = QtGui.QListWidget(self.gridLayoutWidget_3)
        self.ModulesSelectedList.setObjectName(_fromUtf8("ModulesSelectedList"))
        self.gridLayout_3.addWidget(self.ModulesSelectedList, 2, 3, 1, 1)
        self.tabWidget.addTab(self.ModuleSetup, _fromUtf8(""))
        self.LiveSensorData = QtGui.QWidget()
        self.LiveSensorData.setObjectName(_fromUtf8("LiveSensorData"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.LiveSensorData)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 611, 371))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sensor1Temp = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor1Temp.setObjectName(_fromUtf8("sensor1Temp"))
        self.gridLayout_2.addWidget(self.sensor1Temp, 1, 0, 1, 1)
        self.sensor1Label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor1Label.setObjectName(_fromUtf8("sensor1Label"))
        self.gridLayout_2.addWidget(self.sensor1Label, 0, 0, 1, 1)
        self.sensor2Label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor2Label.setObjectName(_fromUtf8("sensor2Label"))
        self.gridLayout_2.addWidget(self.sensor2Label, 0, 3, 1, 1)
        self.sensor2Temp = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor2Temp.setObjectName(_fromUtf8("sensor2Temp"))
        self.gridLayout_2.addWidget(self.sensor2Temp, 1, 3, 1, 1)
        self.sensor1Hum = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor1Hum.setObjectName(_fromUtf8("sensor1Hum"))
        self.gridLayout_2.addWidget(self.sensor1Hum, 2, 0, 1, 1)
        self.sensor1HumValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor1HumValue.setObjectName(_fromUtf8("sensor1HumValue"))
        self.gridLayout_2.addWidget(self.sensor1HumValue, 2, 1, 1, 1)
        self.sensor1Air = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor1Air.setObjectName(_fromUtf8("sensor1Air"))
        self.gridLayout_2.addWidget(self.sensor1Air, 3, 0, 1, 1)
        self.sensor2Hum = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor2Hum.setObjectName(_fromUtf8("sensor2Hum"))
        self.gridLayout_2.addWidget(self.sensor2Hum, 2, 3, 1, 1)
        self.sensor1AirValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor1AirValue.setObjectName(_fromUtf8("sensor1AirValue"))
        self.gridLayout_2.addWidget(self.sensor1AirValue, 3, 1, 1, 1)
        self.sensor2TempValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor2TempValue.setObjectName(_fromUtf8("sensor2TempValue"))
        self.gridLayout_2.addWidget(self.sensor2TempValue, 1, 4, 1, 1)
        self.sensor2AirValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor2AirValue.setObjectName(_fromUtf8("sensor2AirValue"))
        self.gridLayout_2.addWidget(self.sensor2AirValue, 3, 4, 1, 1)
        self.sensor2Air = QtGui.QLabel(self.gridLayoutWidget_2)
        self.sensor2Air.setObjectName(_fromUtf8("sensor2Air"))
        self.gridLayout_2.addWidget(self.sensor2Air, 3, 3, 1, 1)
        self.sensor1TempValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor1TempValue.setObjectName(_fromUtf8("sensor1TempValue"))
        self.gridLayout_2.addWidget(self.sensor1TempValue, 1, 1, 1, 1)
        self.sensor2HumValue = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.sensor2HumValue.setObjectName(_fromUtf8("sensor2HumValue"))
        self.gridLayout_2.addWidget(self.sensor2HumValue, 2, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.tabWidget.addTab(self.LiveSensorData, _fromUtf8(""))
        self.Settings = QtGui.QWidget()
        self.Settings.setObjectName(_fromUtf8("Settings"))
        self.tabWidget.addTab(self.Settings, _fromUtf8(""))
        self.InternetStatusLabel = QtGui.QLabel(self.centralwidget)
        self.InternetStatusLabel.setGeometry(QtCore.QRect(40, 520, 261, 17))
        self.InternetStatusLabel.setObjectName(_fromUtf8("InternetStatusLabel"))
        self.sensorModulesConnectedLabel = QtGui.QLabel(self.centralwidget)
        self.sensorModulesConnectedLabel.setGeometry(QtCore.QRect(370, 520, 241, 17))
        self.sensorModulesConnectedLabel.setObjectName(_fromUtf8("sensorModulesConnectedLabel"))
        SmartHomeSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartHomeSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SmartHomeSystem.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartHomeSystem)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartHomeSystem.setStatusBar(self.statusbar)

        self.retranslateUi(SmartHomeSystem)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SmartHomeSystem)

        # ACTIONS CONFIGURATION:
        self.ScanBLE.clicked.connect(self.scanBLEAction)
        self.SelectSensorModule.clicked.connect(self.selectSensorMac)
        self.ConnectToBLEDevices.clicked.connect(self.connectToBLE)
        self.ScanWiFi.clicked.connect(self.scanWifi)

    def retranslateUi(self, SmartHomeSystem):
        SmartHomeSystem.setWindowTitle(_translate("SmartHomeSystem", "SmartHomeSystem v1.0", None))
        self.ScanWiFi.setText(_translate("SmartHomeSystem", "Scan WiFi Networks", None))
        self.ConnectToWiFi.setText(_translate("SmartHomeSystem", "Connect", None))
        self.passwordLabel.setText(_translate("SmartHomeSystem", "Enter password:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InternetSetup), _translate("SmartHomeSystem", "Internet Setup", None))
        self.SensorModulesSelected.setText(_translate("SmartHomeSystem", "Sensor Modules Selected", None))
        self.ScanBLE.setText(_translate("SmartHomeSystem", "Scan Sensor Modules", None))
        self.SelectSensorModule.setText(_translate("SmartHomeSystem", ">>", None))
        self.ConnectToBLEDevices.setText(_translate("SmartHomeSystem", "Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModuleSetup), _translate("SmartHomeSystem", "Module Setup", None))
        self.sensor1Temp.setText(_translate("SmartHomeSystem", "Temperature", None))
        self.sensor1Label.setText(_translate("SmartHomeSystem", "Sensor Module 1", None))
        self.sensor2Label.setText(_translate("SmartHomeSystem", "Sensor Module 2", None))
        self.sensor2Temp.setText(_translate("SmartHomeSystem", "Temperature", None))
        self.sensor1Hum.setText(_translate("SmartHomeSystem", "Humidity", None))
        self.sensor1Air.setText(_translate("SmartHomeSystem", "AirQuality", None))
        self.sensor2Hum.setText(_translate("SmartHomeSystem", "Humidity", None))
        self.sensor2Air.setText(_translate("SmartHomeSystem", "AirQuality", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LiveSensorData), _translate("SmartHomeSystem", "Live Sensor Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("SmartHomeSystem", "Settings", None))
        self.InternetStatusLabel.setText(_translate("SmartHomeSystem", "Internet Connection Status:", None))
        self.sensorModulesConnectedLabel.setText(_translate("SmartHomeSystem", "Sensor Modules Connected: ", None))


    ############### ACTION FUNCTIONS ##########################################
    def scanBLEAction(self):
        global ble
        ble.scan()

        self.BLEList.clear()

        for mac in ble.bleDevices:
            self.BLEList.addItem(mac.addr)

    def selectSensorMac(self):
        self.ModulesSelectedList.addItem(self.BLEList.currentItem().text())
        # print(self.BLEList.currentItem().text())

    def connectToBLE(self):
        global ble

        items = []
        for index in range(self.ModulesSelectedList.count()):
             items.append(self.ModulesSelectedList.item(index).text())

        for mac in items:
            print("Adding " + mac)
            ble.addModuleMAC(mac)

        ble.connect()
        # if ble.connect():
        newText = "Sensor Modules Connected: " + str(len(ble.connected_modules))
        self.sensorModulesConnectedLabel.setText(newText)


    def scanWifi(self):
        list = Search()
        for item in list:
            self.WiFiList.addItem(item)

    def exitGUI(self):
        sys.exit()


if __name__ == "__main__":


    app = QtGui.QApplication(sys.argv)
    SmartHomeSystem = QtGui.QMainWindow()
    ui = Ui_SmartHomeSystem()
    ui.setupUi(SmartHomeSystem)
    SmartHomeSystem.show()
    sys.exit(app.exec_())
