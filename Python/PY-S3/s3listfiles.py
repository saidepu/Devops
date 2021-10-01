from boto.s3.connection import S3Connection
 
AWS_KEY = ''
AWS_SECRET = ''
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)
bucket = aws_connection.get_bucket('apple123')
for file_key in bucket.list():
    print file_key.name
