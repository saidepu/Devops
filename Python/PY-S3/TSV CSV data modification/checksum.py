#Python script to validate checksum using md5 values
import hashlib #If thrown an "no module found" error, please install this package from your command prompt using 'pip install hashlib' command
import time

f = open('tnr2.md5') #Rename the file for the original TNR2.md5 file
for line in f:
    print "\n"
    print "The original md5 value for the file is.."
    print line[:32]
    print "\n"
    # File to check
    file_name = line[34:]
    file_name = file_name.strip("\n")
    # Correct original md5 goes here
    original_md5 = line[:32]
    # Open,close, read file and calculate MD5 on its contents 
    with open(file_name,'rb') as file_to_check:
      # read contents of the file
      data = file_to_check.read()    
      # pipe contents of the file through
      md5_returned = hashlib.md5(data).hexdigest()
      print "The calculated md5 value for the same file is.."
      print md5_returned    
    # Finally compare original MD5 with freshly calculated
    print "\n"
    time.sleep(2)
    if original_md5 == md5_returned:
       print "MD5 verified! File is matching"
    else:
       print "MD5 verification failed! Please download a new file"
    print "\n"
    print "**************************************************"
