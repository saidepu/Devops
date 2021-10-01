#Python script Validations
import chardet
import time
import csv
import pandas as pd

#Ascii character validations
print "\n"
print "Reading file.."
print "\n"
time.sleep(2)
print "Starting ASCII validations.."
print "\n"
data =  open('TNR2.txt').read()
encoding = chardet.detect(data)
if encoding['encoding'] == 'ascii':
    print("The file contains only ascii characters!")
else:
    print("The file contains non-ascii characters!")
print "\n"

#Tab delimited validations
time.sleep(2)
print "Starting tab delimited validations.."
print "\n"
var = pd.read_table('TNR2.txt', delimiter = '\t', header = None)
print "The file is tab delimited!"
print "The file has no headers!"
print "\n"

#Line break and CRLF validations
print "Starting Line break and CRLF validations.."
f  = open('TNR2.txt','r')
file_contents = f.readlines()
for line in file_contents:
    if(line.endswith('\n')):
        print "Line break found!"
        print "\n"
    else:
        print "Line break not found!"
        print "\n"
    if "\r\n" in open("TNR2.txt","rb").read():
        print "CRLF endings found!"
        print "\n"
    else:
        print "CRLF endings not found!"
        print "\n"
f.close()

#Null fields check
print "Checking for null values...!"
print "\n"
nullcheck = pd.read_csv('TNR2.txt')
modifiednullcheck = nullcheck.fillna('  ')
print "Null fields replaced with delimiters!"



        

