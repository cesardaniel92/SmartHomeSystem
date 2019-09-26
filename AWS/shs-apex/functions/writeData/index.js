console.log('starting writeData function')

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

            //
            var sensorsParams = {
                Item: {
                    EntryID: Date.now(),
                    Date: today,
                    SensorID: e.sensorID,
                    Humidity: e.humidity,
                    Temperature: e.temperature,
                    AirQuality: e.airQuality
                },

                TableName: 'SHS-SensorData'
            };


            ////// Checking Thresholds if needed \\\\\\\\\\\\\\\\\\\\\\\\\

            if (configuration.Item.NotificationsEnabled == true){
                console.log('Notifications Enabled.\n');

                var sensorsDetails = ``

                // Temperature:
                if (e.temperature < configuration.Item.TemperatureThreshold){
                    // console.log('Temperature Level OK.\n');
                }else{
                    // console.log('Temperature Level ALERT!!!\n');
                    sensorsDetails += `Temperature: ${e.temperature}\n`;
                }

                // Humidity:
                if (e.humidity < configuration.Item.HumidityThreshold){
                    // console.log('Humidity Level OK.\n');
                }else{
                    // console.log(`Humidity Level ALERT!!! ${e.humidity} \n`);
                    sensorsDetails += `Humidity: ${e.humidity}\n`;
                }

                // AirQ:
                if (e.airQuality < configuration.Item.AirQThreshold){
                    // console.log('AirQ Level OK.\n');
                }else{
                    // console.log('AirQ Level ALERT!!!\n');
                    sensorsDetails += `AirQuality: ${e.airQuality}\n`;
                }

                // Building Notification Body with sensor details
                var notificationBody = `SHS-ALERT:\nOne or more of your sensor values is greater than the configured threshold (See details below).\nDate: ${today}\n${sensorsDetails} `;

                //////// Sending SNS Notification \\\\\\\\\\\\\\\\\\\\\\\
                var message_params = {
                    Message: notificationBody, /* required */
                    TopicArn: 'arn:aws:sns:us-west-1:136159130349:dynamodb'
                };
                // Create promise and SNS service object
                var publishTextPromise = new AWS.SNS({apiVersion: '2010-03-31'}).publish(message_params).promise();

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
