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

    // SNS Notification test:
    // Set region
    AWS.config.update({region: 'us-west-1'});

    // Create publish parameters
    var message_params = {
      Message: 'This is a test from Lambda function shs_writeData. Thanks!', /* required */
      TopicArn: 'arn:aws:sns:us-west-1:136159130349:dynamodb'
    };

    // Create promise and SNS service object
    var publishTextPromise = new AWS.SNS({apiVersion: '2010-03-31'}).publish(message_params).promise();

    // Handle promise's fulfilled/rejected states
    publishTextPromise.then(
      function(data) {
        console.log("Message ${message_params.Message} send sent to the topic ${message_params.TopicArn}");
        console.log("MessageID is " + data.MessageId);
      }).catch(
        function(err) {
        console.error(err, err.stack);
      });


    docClient.put(params, function(err, data){
        if(err){
            cb(err, null);
        }else{
            cb(null, data);
        }
    });


}
