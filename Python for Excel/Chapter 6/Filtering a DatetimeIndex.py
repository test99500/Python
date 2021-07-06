import pandas as pd

url = 'https://raw.githubusercontent.com/fzumstein/python-for-excel/1st-edition/csv/MSFT.csv'
microsoft = pd.read_csv(url, parse_dates=['Date'])
print(microsoft)
print(microsoft.info())
print(microsoft.describe())

microsoft = microsoft.sort_values(by='Date')
print(microsoft)
