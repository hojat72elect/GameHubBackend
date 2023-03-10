import pandas as pd

"""
I didn't manage to clean telegram accounts database with other tools; hence, I'm going to do it here with Pandas.
"""

# read the DB

df = pd.read_csv('telegram_accounts.csv')
print("The head of the dataframe is as follow:\n", df.head())
print("the columns of our dataframe:\n", df.columns)

# find the duplicate rows.
duplicateRows = df[df.duplicated()]
print("\nDuplicate Rows except first occurrence based on all columns are :")
print(duplicateRows)

# get the cleaned dataframe
cleanedDataframe = df.drop_duplicates(keep='first')
print(type(cleanedDataframe))
print("Cleaned dataframe is :\n", cleanedDataframe)

# save the result as another CSV
cleanedDataframe.to_csv('cleanedDB.csv')
