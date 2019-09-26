console.log('starting readConfig function')

const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({region: 'us-west-1'});

exports.handle = function(e, ctx, cb) {

    let scanningParameters = {
        TableName: 'SHS-Configuration',
        Limit: 10
    };

    docClient.scan(scanningParameters, function(err, data){
        if(err){
            cb(err, null);
        }else{
            cb(null, data);
        }
    });


}
