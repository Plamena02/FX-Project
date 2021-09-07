from os import name
import pandas as pd
import sqlite3, csv
import js2py

# help("modules")

usecols = ['forex_id','date','rate']
forex_quotes = pd.read_csv("../output.csv")
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

final_list = list(set(usecols) & set(forex_quotes.columns))
forex_quotes = forex_quotes[final_list]
forex_quotes.to_sql('api_forex_quotes', conn, if_exists='append', index = False)

conn.commit()
conn.close()

# c.execute("DROP TABLE api_forex_quotes")
# c.execute("""CREATE TABLE api_forex_quotes
#              (start, end, score)""")
# c.execute(f'SELECT cr_short_name FROM api_currency')
# cur = c.fetchall()
# c.execute("UPDATE api_currency SET cr_country = ? WHERE id = ?", ("ax", 44))

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