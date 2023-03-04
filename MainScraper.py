import requests
from bs4 import BeautifulSoup

""""
You give this function the link to a news page of GameSpot (something like [https://www.gamespot.com/news/?page=110])
and it will return URLs of all the news in that page. 

"""


def getArticleUrls(url):
    newsPage = requests.get(url)
    soup = BeautifulSoup(newsPage.content, "html.parser")
    articleUrls = soup.find_all("a", class_="card-item__link")  # bs4.element.ResultSet

    articleUrlsList = []

    for link in articleUrls:
        articleUrl = link["href"]
        articleUrlsList.append(f"https://www.gamespot.com{articleUrl}")

    return articleUrlsList
