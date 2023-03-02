import requests
from bs4 import BeautifulSoup


def parseGameSpotUrl(url):
    requestedPage = requests.get(url)
    soup = BeautifulSoup(requestedPage.content, "html.parser")

    newsTitles = soup.find_all("h4", class_="card-item__title")
    for title in newsTitles:
        print(title.text, end="\n" * 2)
