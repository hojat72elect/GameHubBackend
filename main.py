from getArticleUrls import getArticleUrls

if __name__ == '__main__':
    # first provide the number of pages you want to parse
    numberOfNewsPages = 5
    for pageNumber in range(1, numberOfNewsPages):
        pageArticles = getArticleUrls(f"https://www.gamespot.com/news/?page={pageNumber}")
        print(pageArticles)


