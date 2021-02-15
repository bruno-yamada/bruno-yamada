import boto3
from botocore.config import Config

client = boto3.client('ses', config=Config(region_name='us-east-1'))
toAddress = 'to@email.com'
sourceAddress = 'from@email.com'
sourceArn = 'arn:aws:ses:us-east-1:some-acc-id:identity/my-email.com'

response = client.send_email(
    Source=sourceAddress,
    Destination={
        'ToAddresses': [ toAddress ],
        'CcAddresses': [ toAddress ],
        'BccAddresses': [ toAddress ]
    },
    Message={
        'Subject': {
            'Data': 'Test Subject',
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': 'Message body in text format',
                'Charset': 'UTF-8'
            },
            'Html': {
                'Data': 'Message body in <b>html</b> format',
                'Charset': 'UTF-8'
            }
        }
    },
    Tags=[
        {
            'Name': 'SomeTag',
            'Value': 'SomeValue',
        },
    ],
    # ConfigurationSetName='string'
)

print(response)
