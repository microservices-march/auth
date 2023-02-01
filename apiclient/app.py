import urllib.request
import urllib.error
import os

jwt="Bearer " + os.environ['JWT']
req = urllib.request.Request('http://docker.host.internal')
req.add_header("Authorization", jwt)
try:
      with urllib.request.urlopen(req) as response:
         the_page = response.read()
         message = response.getheader('X-MESSAGE')
         print("200  " + message)
except urllib.error.URLError as e:
      print(str(e.code) + "  " + e.msg) 