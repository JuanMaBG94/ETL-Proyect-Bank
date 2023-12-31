from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Rank", "Bank name", "Market cap"]


page = requests.get(url).text
data = BeautifulSoup(page,'html.parser')
df = pd.DataFrame(columns=table_attribs)
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')
#print(rows)
for row in rows:
    col = row.find_all('td')
    if len(col)!=0:
        #if col[0].find('a') is not None and '—' not in col[2]:
        data_dict = {"Rank": int(col[0].text.strip()),
                             "Bank name": col[1].text.strip(), 
                             "Market cap": float(col[2].text.strip())}
        df1 = pd.DataFrame(data_dict, index=[0])
        df = pd.concat([df,df1], ignore_index=True)
    
print(df)