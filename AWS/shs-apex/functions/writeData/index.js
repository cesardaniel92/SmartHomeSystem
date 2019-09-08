console.log('starting writeData function')

const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({region: 'us-west-1'});

exports.handle = function(e, ctx, cb) {

    var today = new Date();
    var date = (today.getMonth()+1) + '-' + today.getDate() + '-' + today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var today = date + ' ' + time;

    today.get

    var params = {
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

    docClient.put(params, function(err, data){
        if(err){
            cb(err, null);
        }else{
            cb(null, data);
        }
    });


}
