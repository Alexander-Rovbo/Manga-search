import pandas as pd

df = pd.read_excel('manga.xlsx')

df['title'] = df['title'].str.lower()


a = ["магия"]
b = df['title'].str.contains('|'.join(a), case=False, na=False)

s = df[b]['Name']
print(s.head(100))
