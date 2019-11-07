/*
    This Lambda function is triggered by a Write Action at the SHS-API/sensordata endpoint.
    The input has the following format:
    {
        "sensorID": 5,
        "humidity": 5,
        "airQuality": 200,
        "temperature": 5
    }

    Steps executed by the function:
    1. Read current configuration from DynamoDB table.
    2. Extract sensor data from function input.
    3. If Notifications are enabled according to the extracted current configuration:
        3.1) Check threshold values.
        3.2) Build alert message body.
        3.3) Publish alert to SNS Topic.
    4. Write sensor data to DynamoDB table.

*/


console.log('starting writeData function');
const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({region: 'us-west-1'});

exports.handle = function(e, ctx, cb) {

    //////// 1. Extracting current configuration \\\\\\\\\\\\\\\\\\\\\\\\
    let configurationParams = {
        TableName: 'SHS-Configuration',
        Key: {
            "User": "Default"
        }
    };

    docClient.get(configurationParams, function(err, data){
        if(err){
            cb(err, null);
        }else{

            var configuration = data;
            console.log('Configuration received.\n');

            //////// 2. Extracting sensor data from API call \\\\\\\\\\\\\\\\\\\

            // Getting current date:
            var usaTime = new Date().toLocaleString("en-US", {timeZone: "America/Phoenix"});
            var today = new Date(usaTime);
            var date = (today.getMonth()+1) + '-' + today.getDate() + '-' + today.getFullYear();
            var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
            var today = date + ' ' + time;

            var sensorsDetails = ``;
            var alert = false;

            //
            var sensorsParams = {
                Item: {
                    EntryID: Date.now(),
                    Date: today,
                    SensorID: e.sensorID,
                    Humidity: e.humidity,
                    Temperature: e.temperature,
                    AirQuality: e.airQuality,
                    Label: e.label
                },

                TableName: 'SHS-SensorData'
            };


            ////// Checking Thresholds if needed \\\\\\\\\\\\\\\\\\\\\\\\\

            if (configuration.Item.NotificationsEnabled == true){
                console.log('Notifications Enabled.\n');

                // Temperature:
                if (e.temperature < configuration.Item.TemperatureThreshold){
                    console.log('Temperature Level OK.\n');
                }else{
                    console.log('Temperature Level ALERT!!!\n');
                    alert = true;
                    sensorsDetails += `Temperature: ${e.temperature}\n`;
                }

                // Humidity:
                if (e.humidity < configuration.Item.HumidityThreshold){
                    console.log('Humidity Level OK.\n');
                }else{
                    console.log(`Humidity Level ALERT!!! ${e.humidity} \n`);
                    alert = true;
                    sensorsDetails += `Humidity: ${e.humidity}\n`;
                }

                // AirQ:
                if (e.airQuality > configuration.Item.AirQualityThreshold){
                    console.log('AirQ Level OK.\n');
                }else{
                    console.log('AirQ Level ALERT!!!\n');
                    alert = true;
                    sensorsDetails += `AirQuality: ${e.airQuality}\n`;
                }

                if (alert){
                    // Building Notification Body with sensor details
                    var notificationBody = `SHS-ALERT:\nOne or more of your sensor values is greater than the configured threshold (See details below).\nDate: ${today}\n${sensorsDetails} `;

                    //////// Sending SNS Notification \\\\\\\\\\\\\\\\\\\\\\\
                    var message_params = {
                        Message: notificationBody, /* required */
                        TopicArn: 'arn:aws:sns:us-west-1:136159130349:SHS-Alerts'
                    };
                    // Create promise and SNS service object
                    var publishTextPromise = new AWS.SNS({apiVersion: '2010-03-31'}).publish(message_params).promise();
                    console.log(`sending ALERT!!!`);

                    // Disabling notifications to avoid consecutive alerts:
                    var writeConfigParams = {
                        Item: {
                            User: configuration.Item.User,
                            Email: configuration.Item.Email,
                            TemperatureThreshold: configuration.Item.TemperatureThreshold,
                            HumidityThreshold: configuration.Item.HumidityThreshold,
                            AirQualityThreshold: configuration.Item.AirQualityThreshold,
                            NotificationsEnabled: false
                        },

                        TableName: 'SHS-Configuration'
                    };

                    docClient.put(writeConfigParams, function(err, data){
                        if(err){
                            cb(err, null);
                        }else{
                            cb(null, data);
                            console.log('Notications disabled.');
                        }
                    });


                }


            }

            ////////  Writing sensor data to DynamoDB \\\\\\\\\\\\\\\\\\\\
            docClient.put(sensorsParams, function(err, data){
                if(err){
                    cb(err, null);
                }else{
                    cb(null, data);
                    console.log('Data written to DB.');
                }
            });





        }
    });

}
