console.log('starting writeConfiguration function')

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
            User: e.user,
            Email: e.email,
            TemperatureThreshold: e.tempT,
            HumidityThreshold: e.humT,
            AirQualityThreshold: e.airQT
        },

        TableName: 'SHS-Configuration'
    };

    docClient.put(params, function(err, data){
        if(err){
            cb(err, null);
        }else{
            cb(null, data);
        }
    });


}
