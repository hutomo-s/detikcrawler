__author__ = 'hutomo'

import requests
from bs4 import BeautifulSoup
import urllib

url = raw_input("Please enter the url with http (eg: http://detik.com) : ")
# check if the given input is not null
if url:
    pass
else:
    url = "http://www.detik.com"

# request to the given url
r = requests.get(url)

# parse and get all img tag in r.text
soup = BeautifulSoup(r.text, 'html.parser')
img_array = soup.find_all("img")

# count the number of images in img_array
count = len(img_array)
print 'img tag count: ', count

# iterative for all images found
for one_img in soup.find_all('img'):
    src = one_img.get('src')
    if src.startswith('//'):
        file_img = 'http:%s' % src
    elif src.startswith('http://') or src.startswith('https://'):
        file_img = src
    else:
        file_img = url +'/'+ src

    # get file size of each image and print
    file_size_img = urllib.urlopen(file_img).info()['Content-Length']
    print 'Size image %s = %s bytes' % (one_img.get('src'), file_size_img)
