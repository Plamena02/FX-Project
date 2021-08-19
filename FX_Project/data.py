import pandas as pd
import sqlite3, csv
from api.models import Forex_quotes


conn = sqlite3.connect('db-forex.sqlite3')
c = conn.cursor()

tables = pd.read_html('index.html')
print('Tables found:', len(tables))
df1 = tables[0]  

print('First Table')
print(df1)


conn.commit()
conn.close()

# 2, 1034, 62, 61, 75
# c.execute("DROP TABLE api_forex_quotes")
# c.execute("""CREATE TABLE api_forex_quotes
#              (start, end, score)""")

# currency = pd.read_csv("../currencies.csv")
# currency.to_sql('api_currency', conn, if_exists='append', index = False)

# with open('../forex_pairs.csv', newline='') as f:
#         reader = csv.reader(f)
#         data = list(reader)
#         data.pop(0)  

# c.execute("SELECT id, cr_short_name FROM api_currency")
# rows = c.fetchall()

# count=0
# for line in data:
#           cur1 = line[0]
#           cur2 = line[1]
#           forex = line[2]
#           id1 = ""
#           id2 = ""
#           for row in rows:
#                     id = row[0]
#                     name1 = row[1]
#                     if cur1 == name1:
#                               id1=id
#                     if cur2 == name1:
#                               id2=id
#         #   print(forex)  
#           if id1!="" and id2!="":
#                 c.execute("INSERT INTO api_forex (forex_id, from_currency_id_id, to_currency_id_id) VALUES (?, ?, ?)",(forex,id1,id2))

# c.execute("UPDATE api_currency SET cr_short_name = 'CLP' WHERE id = 27")