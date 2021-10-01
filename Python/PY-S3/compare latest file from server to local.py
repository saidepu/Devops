import os, datetime, time
import urllib2
u = urllib2.urlopen('web server URL/path')
meta = u.info()
print("Last Modified: " + str(meta.getheaders("Last-Modified")))

meta_modifiedtime = time.mktime(datetime.datetime.today().timetuple())

file = 'C:\users\srinivasanravi\desktop\sample.txt'
if os.path.getmtime(file) > meta_modifiedtime: #change > to <
   print("CPU file is older than server file.")
else:
   print("CPU file is NOT older than server file.")
