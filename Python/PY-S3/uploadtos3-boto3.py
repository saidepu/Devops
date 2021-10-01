#!/usr/bin/python3.4
import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'apple123'

data = open('data123.txt', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
    )
s3.Bucket(BUCKET_NAME).put_object(Key='data123.txt', Body=data) #Upload the file to the s3 bucket
import time
time.sleep(5)
print("Upload completed successfully")
time.sleep(2)
print("Opening web page...")
time.sleep(3)

#Open IE and showcase the deployed file in the bucket
import webbrowser

ie = webbrowser.get(webbrowser.iexplore)
ie.open('s3 bucket URL') #Put your bucket display page URL here

#Get Last Modified file

