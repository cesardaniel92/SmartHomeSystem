# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ble import *
from my_wifi import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import requests
import threading
import time
import json

ble = BLE_handler()
api = API_handler()

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
        SmartHomeSystem.resize(810, 608)
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
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 695, 351))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelValue = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.labelValue.setObjectName(_fromUtf8("labelValue"))
        self.gridLayout_3.addWidget(self.labelValue, 4, 1, 1, 1)
        self.SensorModulesSelected = QtGui.QLabel(self.gridLayoutWidget_3)
        self.SensorModulesSelected.setObjectName(_fromUtf8("SensorModulesSelected"))
        self.gridLayout_3.addWidget(self.SensorModulesSelected, 1, 5, 1, 1)
        self.BLEList = QtGui.QListWidget(self.gridLayoutWidget_3)
        self.BLEList.setObjectName(_fromUtf8("BLEList"))
        self.gridLayout_3.addWidget(self.BLEList, 2, 1, 1, 1)
        self.ScanBLE = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.ScanBLE.setObjectName(_fromUtf8("ScanBLE"))
        self.gridLayout_3.addWidget(self.ScanBLE, 1, 1, 1, 1)
        self.SelectSensorModule = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.SelectSensorModule.setObjectName(_fromUtf8("SelectSensorModule"))
        self.gridLayout_3.addWidget(self.SelectSensorModule, 2, 3, 1, 1)
        self.ModulesSelectedList = QtGui.QListWidget(self.gridLayoutWidget_3)
        self.ModulesSelectedList.setObjectName(_fromUtf8("ModulesSelectedList"))
        self.gridLayout_3.addWidget(self.ModulesSelectedList, 2, 5, 1, 1)
        self.ConnectToBLEDevices = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.ConnectToBLEDevices.setObjectName(_fromUtf8("ConnectToBLEDevices"))
        self.gridLayout_3.addWidget(self.ConnectToBLEDevices, 4, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.setLabelButton = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.setLabelButton.setObjectName(_fromUtf8("setLabelButton"))
        self.gridLayout_3.addWidget(self.setLabelButton, 4, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 4, 4, 1, 1)
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
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        self.RefreshButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.RefreshButton.setObjectName(_fromUtf8("RefreshButton"))
        self.gridLayout_2.addWidget(self.RefreshButton, 4, 0, 1, 5)
        self.tabWidget.addTab(self.LiveSensorData, _fromUtf8(""))
        self.Settings = QtGui.QWidget()
        self.Settings.setObjectName(_fromUtf8("Settings"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.Settings)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(60, 20, 581, 391))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.SaveButton = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.gridLayout_4.addWidget(self.SaveButton, 8, 0, 1, 2)
        self.TempLabel = QtGui.QLabel(self.gridLayoutWidget_4)
        self.TempLabel.setObjectName(_fromUtf8("TempLabel"))
        self.gridLayout_4.addWidget(self.TempLabel, 2, 0, 1, 1)
        self.EmailLabel = QtGui.QLabel(self.gridLayoutWidget_4)
        self.EmailLabel.setObjectName(_fromUtf8("EmailLabel"))
        self.gridLayout_4.addWidget(self.EmailLabel, 6, 0, 1, 1)
        self.HumLabel = QtGui.QLabel(self.gridLayoutWidget_4)
        self.HumLabel.setObjectName(_fromUtf8("HumLabel"))
        self.gridLayout_4.addWidget(self.HumLabel, 3, 0, 1, 1)
        self.AirQLabel = QtGui.QLabel(self.gridLayoutWidget_4)
        self.AirQLabel.setObjectName(_fromUtf8("AirQLabel"))
        self.gridLayout_4.addWidget(self.AirQLabel, 4, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 7, 0, 1, 1)
        self.tempInput = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.tempInput.setObjectName(_fromUtf8("tempInput"))
        self.gridLayout_4.addWidget(self.tempInput, 2, 1, 1, 1)
        self.emailInput = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.emailInput.setObjectName(_fromUtf8("emailInput"))
        self.gridLayout_4.addWidget(self.emailInput, 6, 1, 1, 1)
        self.HumInput = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.HumInput.setObjectName(_fromUtf8("HumInput"))
        self.gridLayout_4.addWidget(self.HumInput, 3, 1, 1, 1)
        self.AirQInput = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.AirQInput.setObjectName(_fromUtf8("AirQInput"))
        self.gridLayout_4.addWidget(self.AirQInput, 4, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 5, 0, 1, 1)
        self.thresholdLabel = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.thresholdLabel.setFont(font)
        self.thresholdLabel.setObjectName(_fromUtf8("thresholdLabel"))
        self.gridLayout_4.addWidget(self.thresholdLabel, 1, 0, 1, 1)
        self.notificationRadioButton = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.notificationRadioButton.setObjectName(_fromUtf8("notificationRadioButton"))
        self.gridLayout_4.addWidget(self.notificationRadioButton, 0, 0, 1, 2)
        self.tabWidget.addTab(self.Settings, _fromUtf8(""))
        self.InternetStatusLabel = QtGui.QLabel(self.centralwidget)
        self.InternetStatusLabel.setGeometry(QtCore.QRect(40, 520, 261, 17))
        self.InternetStatusLabel.setObjectName(_fromUtf8("InternetStatusLabel"))
        self.sensorModulesConnectedLabel = QtGui.QLabel(self.centralwidget)
        self.sensorModulesConnectedLabel.setGeometry(QtCore.QRect(370, 520, 241, 17))
        self.sensorModulesConnectedLabel.setObjectName(_fromUtf8("sensorModulesConnectedLabel"))
        SmartHomeSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartHomeSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SmartHomeSystem.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartHomeSystem)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartHomeSystem.setStatusBar(self.statusbar)

        self.retranslateUi(SmartHomeSystem)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(SmartHomeSystem)


        # Autopopulating Current Settings:
        config_response = api.read_configuration()
        config_json = json.loads(config_response)
        item = config_json['Items'][0]

        self.tempInput.setText(str(item['TemperatureThreshold']))
        self.HumInput.setText(str(item['HumidityThreshold']))
        self.AirQInput.setText(str(item['AirQualityThreshold']))
        self.emailInput.setText(item['Email'])
        self.notificationRadioButton.setChecked(item['NotificationsEnabled'])

        # ACTIONS CONFIGURATION:
        self.ScanBLE.clicked.connect(self.scanBLEAction)
        self.SelectSensorModule.clicked.connect(self.selectSensorMac)
        self.ConnectToBLEDevices.clicked.connect(self.connectToBLE)
        self.ScanWiFi.clicked.connect(self.scanWifi)
        self.ConnectToWiFi.clicked.connect(self.connectToWifiAction)
        self.SaveButton.clicked.connect(self.saveConfiguration)
        self.RefreshButton.clicked.connect(self.getLiveData)
        self.ModulesSelectedList.itemClicked.connect(self.getLabel)
        self.setLabelButton.clicked.connect(self.setLabel)

        # Setting password mode in text field to use * and hide characters:
        self.passwordField.setEchoMode(QtGui.QLineEdit.Password)


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
        self.setLabelButton.setText(_translate("SmartHomeSystem", "Set Label", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModuleSetup), _translate("SmartHomeSystem", "Module Setup", None))
        self.sensor1Temp.setText(_translate("SmartHomeSystem", "Temperature", None))
        self.sensor1Label.setText(_translate("SmartHomeSystem", "Sensor Module 1", None))
        self.sensor2Label.setText(_translate("SmartHomeSystem", "Sensor Module 2", None))
        self.sensor2Temp.setText(_translate("SmartHomeSystem", "Temperature", None))
        self.sensor1Hum.setText(_translate("SmartHomeSystem", "Humidity", None))
        self.sensor1Air.setText(_translate("SmartHomeSystem", "AirQuality", None))
        self.sensor2Hum.setText(_translate("SmartHomeSystem", "Humidity", None))
        self.sensor2Air.setText(_translate("SmartHomeSystem", "AirQuality", None))
        self.RefreshButton.setText(_translate("SmartHomeSystem", "Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LiveSensorData), _translate("SmartHomeSystem", "Live Sensor Data", None))
        self.SaveButton.setText(_translate("SmartHomeSystem", "Save", None))
        self.TempLabel.setText(_translate("SmartHomeSystem", "Temperature (F)", None))
        self.EmailLabel.setText(_translate("SmartHomeSystem", "Email:", None))
        self.HumLabel.setText(_translate("SmartHomeSystem", "Humidity ", None))
        self.AirQLabel.setText(_translate("SmartHomeSystem", "Air Quality", None))
        self.thresholdLabel.setText(_translate("SmartHomeSystem", "Threshold Values:", None))
        self.notificationRadioButton.setText(_translate("SmartHomeSystem", "Get instant notifications", None))
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
        global ble

        newMac = self.BLEList.currentItem().text()
        self.ModulesSelectedList.addItem(newMac)
        ble.addModuleMAC(newMac)

        newIndex = len(ble.modules_MACs) - 1
        newLabel = "default" + str(newIndex)
        ble.modules_labels.append(newLabel)

    def connectToBLE(self):
        global ble

        ble.connect()
        newText = "Sensor Modules Connected: " + str(len(ble.connected_modules))
        self.sensorModulesConnectedLabel.setText(newText)

    def getLabel(self):
        global ble

        itemIndex = int(self.ModulesSelectedList.currentRow())
        itemLabel = ble.modules_labels[itemIndex]
        self.labelValue.setText(itemLabel)

    def setLabel(self):
        global ble

        newLabel = self.labelValue.text()
        itemIndex = int(self.ModulesSelectedList.currentRow())
        ble.modules_labels[itemIndex] = newLabel

    def showdialog(self, title, messageText):
        msg = QMessageBox()

        if (title == "Critical"):
            msg.setIcon(QMessageBox.Critical)
        else:
            msg.setIcon(QMessageBox.Information)

        msg.setText(messageText)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def scanWifi(self):
        if check_connection():
            self.showdialog ("Information", "Device is already online.")
        else:

            list = scan_wifi()
            for item in list:
                self.WiFiList.addItem(item)


    def connectToWifiAction(self):

        ssid = self.WiFiList.currentItem().text()
        password = self.passwordField.text()

        if check_connection():
            newText = "Internet Connection Status: ONLINE"
        else:
            connect_to_wifi(ssid, password)
            time.sleep(15) # Waiting for connection to estabilize
            if check_connection():
                newText = "Internet Connection Status: ONLINE"
            else:
                newText = "Internet Connection Status: OFFLINE"
                self.showdialog ("Critical", "Could not connect to WiFi. Try again.")

        self.InternetStatusLabel.setText(newText)


    def saveConfiguration(self):
        notifications = self.notificationRadioButton.isChecked()
        tempT = self.tempInput.text()
        humT = self.HumInput.text()
        airQT = self.AirQInput.text()
        newEmail = self.emailInput.text()

        api.write_configuration('Default', newEmail, tempT, humT, airQT, notifications)


    def getLiveData(self):

        # Checking for Sensor modules connection:
        if (len(self.BLEList) == 0):
            self.showdialog ("Critical", "No Sensor Module currently connected.")
        else:
            data_response = api.read_data()
            data_json = json.loads(data_response)
            sensor1 = data_json['Items'][0]
            sensor2 = data_json['Items'][1]

            print(sensor1)
            print(sensor2)
            self.sensor1Label.setText(sensor1['Label'])
            self.sensor1TempValue.display(sensor1['Temperature'])
            self.sensor1HumValue.display(sensor1['Humidity'])
            self.sensor1AirValue.display(sensor1['AirQuality'])

            self.sensor2Label.setText(sensor2['Label'])
            self.sensor2TempValue.display(sensor2['Temperature'])
            self.sensor2HumValue.display(sensor2['Humidity'])
            self.sensor2AirValue.display(sensor2['AirQuality'])

    def exitGUI(self):
        sys.exit()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    SmartHomeSystem = QtGui.QMainWindow()
    ui = Ui_SmartHomeSystem()
    ui.setupUi(SmartHomeSystem)
    SmartHomeSystem.show()
    sys.exit(app.exec_())
