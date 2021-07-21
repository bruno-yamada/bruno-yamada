## AWS cli
```
aws sts get-caller-identity
```

## NodeJS
```
var AWS = require("aws-sdk")
var sts = new AWS.STS();
sts.getCallerIdentity({}, function (err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
});
```

## Python
```
import boto3
client = boto3.client("sts")
client.get_caller_identity()
```
