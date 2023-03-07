from csv import writer

import requests
from bs4 import BeautifulSoup


def writeToGithubDb(GithubUserName):
    """
   You give it a GitHub user name and it will be stored in a CSV file.
    """
    with open("github_handles.csv", mode="a") as db:
        writerObj = writer(db)
        writerObj.writerow([GithubUserName])
        db.close()


def extractSinglePage(page):
    """
    You give it a single web page of GitHub which contains star gazers; and it will extract and
    save all those star gazer users into a CSV file.
    """
    startGazersPage = requests.get(page)
    soup = BeautifulSoup(startGazersPage.content, "html.parser")
    parentTag = soup.find("ol", class_="d-block d-md-flex flex-wrap gutter list-style-none")
    counter = 0

    for a in parentTag.find_all('a', ):
        counter = counter + 1
        if counter == 1:
            writeToGithubDb(a['href'][1:])
        if counter == 3:
            counter = 0


# pay attention that this list should only contain
reposList = ["https://github.com/freeCodeCamp/freeCodeCamp/stargazers",
             "https://github.com/sindresorhus/awesome/stargazers",
             "https://github.com/jwasham/coding-interview-university/stargazers",
             "https://github.com/996icu/996.ICU/stargazers",
             "https://github.com/EbookFoundation/free-programming-books/stargazers"
             ]


def extractAllStarGazers():
    try:
        for baseUrl in reposList:
            for pageNumber in range(1, 100):
                extractSinglePage(page=f"{baseUrl}?page={pageNumber}")
    except:
        extractAllStarGazers()
