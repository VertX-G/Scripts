import requests
from bs4 import BeautifulSoup
import re
import wget
import os.path
from os import path
 
 
url = 'https://www.ccontario.com/thru-the-bible'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
test_string = 'https://www.ccontario.com/'
#text_file = open("C:\Users\geral\Downloads\Audio.txt","w")
 
urls = []
for link in soup.find_all('a'):
    url_text = link.get('href')
    if url_text.startswith(test_string):
        x = (url_text[len(test_string):]).strip()
        print(x)
        try:
            #r = requests.get(f'https://www.calvarychapelontario.com/teaching/{x}/{x}.zip')
            src = (f'https://www.calvarychapelontario.com/teaching/{x}/{x}.zip')
            save_path = (f'C:\MotherBibleAudio\{x}.zip')
            if not path.exists(save_path):
                
                wget.download(src, save_path)
                print(f'\n---------- Completed download {x} ----------')
            #else:
                #print(f'\n---------- {x} already exists ----------')
        except:
            print(f'---------- Could not download {x} ----------')
            #print(f'---------- Error: {error} ----------')
    #x = re.search("^\https://www.ccontario.com/", url_text)
    #text_file.write()

# if () exists
#    wget.download(url,/downloads)

#text_file.close()

# wget.download(url,filepath)

# https://www.calvarychapelontario.com/teaching/genesis/genesis.zip
# https://www.calvarychapelontario.com/teaching/2peter/2peter.zip
#f'hanning{num}.pdf'
'''

'''




'''
import bs4
import requests

url = "https://www.ccontario.com/"
r = requests.get(url)
data = bs4.BeautifulSoup(r.text, "html.parser")
for l in data.find_all("a"):
    r = requests.get(url + l["href"])
    print(r.status_code)
'''



'''
import re
def getFilename_fromCd(cd):


"""
Get filename from content-disposition
"""
if not cd:
return None
fname = re.findall('filename=(.+)', cd)
if len(fname) == 0:
return None
return fname[0]


url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
filename = getFilename_fromCd(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)
'''