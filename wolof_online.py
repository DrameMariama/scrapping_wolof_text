from isort import file
import requests
from bs4 import BeautifulSoup
import os

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    div_links = soup.find_all("div", class_="alignleft th_shadow")
    urls = [div.a.attrs.get("href") for div in div_links]
    for url in urls:
        print(url)
        filename = url.split("=")[-1]+".txt"
        if filename != "1821.txt":
            filename = os.path.join("wolof_online", filename)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            div = soup.find("div", class_="entry")
            with open(filename, "w") as file:
                file.write(div.text)



if __name__=="__main__":
    url = "http://www.wolof-online.com/"
    scrape(url)