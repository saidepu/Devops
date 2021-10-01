import urllib.request
import re

xml_data = urllib.request.urlopen('http://static.cricinfo.com/rss/livescores.xml').read()
#print (xml_data)

pattern = "<item>(.*?)</item>"
xml_data = xml_data.decode('ISO-8859-1')
for i in re.findall(pattern, xml_data, re.DOTALL):
    result = re.split('<.+?>',i)
    #print (result)
    print(result[1], result[3])