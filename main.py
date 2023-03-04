from MainScraper import getArticleUrls


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    pageArticles= getArticleUrls("https://www.gamespot.com/news/?page=4")
    print(pageArticles)