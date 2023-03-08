from requests import get

"""
I don't know how, but GitHub has obfuscated the emails via a 
JS file in their page. I can't extract user emails.
"""

# def extractEmail(inputList):
#     githubHandle = inputList[0]
#     print(type(githubHandle), githubHandle)


# with open("github_users_db.csv", mode="r") as github_db:
#     readerObj = reader(github_db)
#     for line in readerObj:
#         extractEmail(line)


githubHandle = "hojat72elect"
githubPage = get(f"https://github.com/{githubHandle}").content
print(githubPage)