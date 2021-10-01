import glob
import os
import time

list_of_files = glob.glob('C:/Users/Srinivasanravi/Desktop/*.txt') # * means all if need specific format then *.csv
latest = max(list_of_files, key=os.path.getctime)
print "Fetching the latest file from local....\n"
time.sleep(5)
print latest

#Removing time stamp and renaming the file in local
latest_without_extension = latest[:-4]
latest_without_timestamp = latest_without_extension[:-6]
print "\nRemoving time stamp before upload to bucket...\n"
time.sleep(5)
uploadfile = latest_without_timestamp + ".xml"
os.rename(latest, uploadfile)
print "Renaming successful!"
print uploadfile
