"""
Don't run this file again, it will crash the IDE.
"""

from csv import writer

import requests
from bs4 import BeautifulSoup


def writeToGithubDb(GithubUserName):
    """
   You give it a GitHub user name and it will be stored in a CSV file.
    """
    with open("github1.csv", mode="a") as db:
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
reposList1 = ["https://github.com/freeCodeCamp/freeCodeCamp/stargazers",
              "https://github.com/sindresorhus/awesome/stargazers",
              "https://github.com/jwasham/coding-interview-university/stargazers",
              "https://github.com/996icu/996.ICU/stargazers",
              "https://github.com/EbookFoundation/free-programming-books/stargazers"
              ]

reposList2 = ["https://github.com/godotengine/godot/stargazers",
              "https://github.com/cocos2d/cocos2d-x/stargazers",
              "https://github.com/stride3d/stride/stargazers",
              "https://github.com/blender/blender/stargazers",
              "https://github.com/libgdx/libgdx/stargazers"]

reposList3 = ["https://github.com/apache/echarts/stargazers",
              "https://github.com/apache/superset/stargazers",
              "https://github.com/apache/dubbo/stargazers"]

reposList4 = ["https://github.com/apache/spark/stargazers",
              "https://github.com/justjavac/free-programming-books-zh_CN/stargazers"]

reposList5 = ["https://github.com/square/okhttp/stargazers",
              "https://github.com/square/leakcanary/stargazers"]

reposList6 = ["https://github.com/JetBrains/kotlin/stargazers",
              "https://github.com/NativeScript/NativeScript/stargazers"]

reposList7 = ["https://github.com/google/iosched"]


def extractAllStarGazers():
    try:
        for baseUrl in reposList7:
            for pageNumber in range(1, 100):
                extractSinglePage(page=f"{baseUrl}?page={pageNumber}")
    except:
        extractAllStarGazers()


try:
    extractAllStarGazers()
except:
    extractAllStarGazers()
