import subprocess
#download from s3
subprocess.call(['aws', 's3', 'cp', 's3://yours3bucket/yourzip.zip', 'C:\Users\srinivasanravi\Desktop'])
#upload to s3
subprocess.call(['aws', 's3', 'cp', 'C:\Users\srinivasanravi\Desktop\file.txt', 's3://yours3bucket/path'])

