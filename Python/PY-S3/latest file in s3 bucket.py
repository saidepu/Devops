import boto3
import time
from pprint import pprint

s3 = boto3.resource('s3',region_name='us-east-2')
bucket='bucket-name'
key='samplepath/files/' + uploadfile
summaryDetails=s3.ObjectSummary(bucket,key)
timeFormat=summaryDetails.last_modified
formatedTime=timeFormat.strftime("%Y-%m-%d %H:%M:%S")
pprint( 'Bucket name is '+ bucket + ' and key name is ' + key + ' and last modified at time '+ formatedTime)
