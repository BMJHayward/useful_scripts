import shutil, os


for drctry in list(os.walk('.'))[0][1]:
    shutil.make_archive(drctry, 'zip', drctry)

'''
import requests  # pip install should be available
payload = {'access_token': ACCESS_TOKEN}
r = requests.put("http://onedrive_URL.com/endpoint", data=payload)
r.status_code  # should be 200
r.content  # have a look at this and see what it is
'''

'''
# this is the old way before requests lib
import urllib2
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://example.org', data='your_put_data')
request.add_header('Content-Type', 'your/contenttype')
request.get_method = lambda: 'PUT'
url = opener.open(request)
'''