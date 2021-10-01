import urllib
import lxml.html
import os
import shutil
import time

# index page
pattern_files_url = "web server URL/files path"
# relative url references based here
pattern_files_base = '/'.join(pattern_files_url.split('/')[:-1])

# scrape the index page for latest file list
doc = lxml.html.parse(pattern_files_url)
timestr = time.strftime("%d%m%Y")
pattern_files = [ref for ref in doc.xpath("//a/@href") if timestr in ref and ref.endswith('.xml')]
if pattern_files:
    pattern_files.sort()
    newest = pattern_files[-1]
    local_name = newest.split('/')[-1]
    # grab it if we don't already have it
    if not os.path.exists(local_name):
        url = pattern_files_base + '/' + newest
        print("downloading %s to %s" % (url, local_name))
        remote = urllib.urlopen(url)
        print dir(remote)
        with open(local_name, 'w') as local:
            shutil.copyfileobj(remote, local, length=16*1024*1024)
