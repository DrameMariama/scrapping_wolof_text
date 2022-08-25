from  urllib import request
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
def scrape_bible(url):


    s = requests.Session()
    r = s.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    divs = soup.find_all("div", class_="m")+ soup.find_all("div", class_="p") 
    return divs
if __name__=="__main__":
    base_url = "http://currah.download/pages/wolof/bible/"
    urls = [base_url+"kyg/KYG-42-LUK-{0:03}.html".format(i) for i in range(1, 25)]
    filenames = ["bible-{0:03}.txt".format(i) for i in range(1, 25)]
    for i, url in enumerate(urls):
        filename = filenames[i]
        print(f"scraping url {url}")
        divs = scrape_bible(url)
        with open("wolof/"+filename, "w") as file:
            for div in divs:
                text = div.text
                text = re.sub("\d", "", text).strip()
                file.write(text)
                file.write("\n")
        print(f"Done with {url}")



# while True:
#     iframe_url = urljoin(url, iframe_src)
#     r = s.get(iframe_url)
#     soup = BeautifulSoup(r.content, "html.parser")
#     #print(soup)
#     spans = soup.find_all('span', class_="button")
#     if spans and len(spans) > 2:
#         print(spans)
#         next_page = spans[2]
#         next_page_link = next_page.find('a').attrs["href"]
#         iframe_url = urljoin(url, next_page_link)
#         print(url)
#         print("++"*30)
#     else:
#         break
