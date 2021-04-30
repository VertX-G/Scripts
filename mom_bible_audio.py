import requests
from bs4 import BeautifulSoup
from os import path
import wget


url = "https://www.ccontario.com/thru-the-bible"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, "html.parser")
test_string = "https://www.ccontario.com/"
# with open("C:\Users\geral\Downloads\Audio.txt","w") as text_file

urls = []
for link in soup.find_all("a"):
    url_text = link.get("href")
    if url_text.startswith(test_string):
        x = (url_text[len(test_string) :]).strip()
        # text_file.write(x)
        print(x)
        try:
            src = f"https://www.calvarychapelontario.com/teaching/{x}/{x}.zip"
            save_path = f"C:\MotherBibleAudio\{x}.zip"
            if not path.exists(save_path):

                wget.download(src, save_path)
                print(f"\n---------- Completed download {x} ----------")
            else:
                print(f"\n---------- {x} already exists ----------")
        except:
            print(f"---------- Could not download {x} ----------")


"""
import bs4
import requests

url = "https://www.ccontario.com/"
r = requests.get(url)
data = bs4.BeautifulSoup(r.text, "html.parser")
for l in data.find_all("a"):
    r = requests.get(url + l["href"])
    print(r.status_code)
"""
