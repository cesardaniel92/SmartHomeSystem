console.log('starting writeConfiguration function')

const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({region: 'us-west-1'});

exports.handle = function(e, ctx, cb) {

    // Populating Configuration Fields:
    var today = new Date();
    var date = (today.getMonth()+1) + '-' + today.getDate() + '-' + today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var today = date + ' ' + time;

    var writeConfigParams = {
        Item: {
            User: e.user,
            Email: e.email,
            TemperatureThreshold: e.tempT,
            HumidityThreshold: e.humT,
            AirQualityThreshold: e.airQT
        },

        TableName: 'SHS-Configuration'
    };

    // SNS Notifications Configuration:
    var sns = new AWS.SNS({apiVersion: '2010-03-31'});
    var myTopicArn = 'arn:aws:sns:us-west-1:136159130349:SHS-Alerts';
    var topicParams = {
        TopicArn: myTopicArn /* required */
    };

    // Getting current subscriptions:
    sns.listSubscriptionsByTopic(topicParams, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else{

            var currentSubscriptions = data.Subscriptions;
            var endpointFound = false;

            // Modifying Topic subscriptions if needed:
            currentSubscriptions.forEach(function(subscription){
                if (e.email != subscription.Endpoint){

                    if (subscription.SubscriptionArn == 'PendingConfirmation'){
                        console.log(`${subscription.Endpoint} still pending...`)
                    }else{
                        var subsParams = {
                          SubscriptionArn: subscription.SubscriptionArn /* required */
                        };
                        sns.unsubscribe(subsParams, function(err, data) {
                          if (err) console.log(err, err.stack); // an error occurred
                          else     console.log(data);           // successful response
                        });
                        console.log(`Subscription ${subscription.Endpoint} was removed.`)
                    }

                }else{
                    console.log(`${subscription.Endpoint} already active.`)
                    endpointFound = true;
                }
            });

            // Adding subscription if not found:
            if (endpointFound == false){
                var subscribeParams = {
                    Protocol: 'email',
                    TopicArn: myTopicArn,
                    Endpoint: e.email,
                    ReturnSubscriptionArn: false
                };
                sns.subscribe(subscribeParams, function(err, data) {
                  if (err) console.log(err, err.stack); // an error occurred
                  else  console.log(`Subscription ${e.email} was added.`)
                });
            }


        }
    });

    // Writing Configuration into DynamoDB table:
    docClient.put(writeConfigParams, function(err, data){
        if(err){
            cb(err, null);
        }else{
            cb(null, data);
        }
    });


}
