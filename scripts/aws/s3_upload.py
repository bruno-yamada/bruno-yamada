import boto3

s3 = boto3.client('s3')

filename = '/path/to/file'
bucket = 'mybucket'
key = 'myfile.txt'

r = s3.upload_file(Filename=filename,
        ExtraArgs={'ServerSideEncryption': 'aws:kms'}, # if using this policy
        Bucket=bucket,
        Key=key)

print(r)
