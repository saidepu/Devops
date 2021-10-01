#New
f  = open('TNR2_WI_SAMPLE.txt','r')
file_contents = f.readlines()
for line in file_contents:
    if(line.endswith('\n')):
        print "Line break found!"
    else:
        print "Line break not found!"
    if "\r\n" in open("TNR2_WI_SAMPLE.txt","rb").read():
        print "CRLF endings found!"
    else:
        print "CRLF endings not found!"
    pieces = line.split('\t')
    print pieces
f.close()

import pandas as pd
nullcheck = pd.read_csv('TNR2_WI_SAMPLE.txt')
print nullcheck
modifiednullcheck = nullcheck.fillna('  ')
print modifiednullcheck
