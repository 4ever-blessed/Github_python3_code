# conda_python3_code

import urllib.request

reponse = urllib.request.urlopen('http://placekitten.com/g/200/300')
cat_img = reponse.read()
with open('cat.jpg','wb') as f:
    f.write(cat_img)

