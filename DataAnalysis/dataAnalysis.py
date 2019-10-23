
import json
import datetime
import pandas as pd
from matplotlib import pyplot as plt
#module for plotting the data
from dataAnalysis import*
#Module to get the canvas to draw the polt on
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


file_name = 'sensorData.json'

#This funcion takes the json file and return it as a dictionary 
def read_JSON(file_name):
    # function to read data from a JSON file
    with open(file_name, 'r') as file:
        dataInfo = json.load(file)
    # return data as a dictionary
    return dataInfo


data = read_JSON(file_name)

#This fucntion takes the data as a dictionary and return it as a data frame to be easily poltted 
def analyze(data, days):
    # determine the current date
    now = datetime.datetime.now()
    # create lists of date, temperature, airquality and humidity 
    date = []
    temperature = []
    airquality = []
    humidity = []
    for item in data["Items"]:
        # convert date from text format to datetime format
        item_date = datetime.datetime.strptime(item["Date"], '%m-%d-%Y %H:%M:%S')        
        # determine the difference between the dates
        delta = now - item_date
        if delta.days <= days:
            # only select data for which the date difference does not exceed the specified number of days
            date.append(item_date)
            temperature.append(int(item["Temperature"]))
            airquality.append(int(item["AirQuality"]))
            humidity.append(int(item["Humidity"]))
    # create a data frame. pd takes data and creates a Python object with rows and columns called data frame
    d = {"Date": date, "Temperature": temperature, "AirQuality": airquality, "Humidity": humidity}
    df = pd.DataFrame(data=d) 
    return df



# collect the data from 4 different periods as objects(week, month, 3 months, year)
dataFrameWeek = analyze(data,7)
dataFrameMonth = analyze(data,31)
dataFrame3Months = analyze(data,90)
dataFrameYear = analyze(data,364)


#take the data in the last 24 and plot it
def plot1():
    p1 = dataFrameWeek
    plt.cla()
    #pg1 = figure.add_subplot(111)   
    pg1 = plt.plot(p1.Date, p1.AirQuality)
    pg1 = plt.plot(p1.Date, p1.Temperature)
    pg1 = plt.plot(p1.Date, p1.Humidity)
    pg1 = plt.xlabel('Date')
    pg1 = plt.ylabel('Data')
    pg2 = plt.title('Last 24 hours')
    return pg1

#take the data in the last month and return a plot of it
def plot2():
    p2 = dataFrameMonth
    plt.cla()
    pg2 = plt.plot(p2.Date, p2.AirQuality, label='Air Quality')
    pg2 = plt.plot(p2.Date, p2.Temperature, label='Temperature')
    pg2 = plt.plot(p2.Date, p2.Humidity, label='Humidity')
    pg2 = plt.xlabel('Date')
    pg2 = plt.ylabel('Data')
    pg2 = plt.title('Last month')
    return pg2

#take the data in the last 3 months and return a plot of it
def plot3():
    p3 = dataFrame3Months
    plt.cla()
    pg3 = plt.plot(p3.Date, p3.AirQuality)
    pg3 = plt.plot(p3.Date, p3.Temperature)
    pg3 = plt.plot(p3.Date, p3.Humidity)
    pg3 = plt.xlabel('Date')
    pg3 = plt.ylabel('Data')
    pg2 = plt.title('Last 3 months')
    return pg3

#take the data in the last year and return a plot of it
def plot4():
    p4 = dataFrameYear
    plt.cla()
    pg4 = plt.plot(p4.Date, p4.AirQuality)
    pg4 = plt.plot(p4.Date, p4.Temperature)
    pg4 = plt.plot(p4.Date, p4.Humidity)
    pg4 = plt.xlabel('Date')
    pg4 = plt.ylabel('Data')
    pg2 = plt.title('Last Year')
    return pg4
    
