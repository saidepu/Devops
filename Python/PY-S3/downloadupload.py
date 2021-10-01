#!/usr/bin/python3.4
import urllib2
import glob
import os

ret = urllib2.urlopen('web server URL/path')
if ret.code == 200:
    print "Exists!"
	
timestr = time.strftime("%d%m%Y")
url = "web server URL/path"

file_name = filename.startswith("example_") and timestr in filename
print filename
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()
print "Download Successful!"