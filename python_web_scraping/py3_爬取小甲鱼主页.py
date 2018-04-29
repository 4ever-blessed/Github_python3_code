# conda_python3_code

import urllib.request

reponse = urllib.request.urlopen('http://www.fishc.com')
html = reponse.read()
html = html.decode('utf-8')
print(html)

