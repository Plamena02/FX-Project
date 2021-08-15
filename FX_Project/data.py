import pandas as pd
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

conn.commit()
conn.close()


# currency = pd.read_csv("../currencies.csv")
# currency.to_sql('api_currency', conn, if_exists='append', index = False)
# c.execute("DROP TABLE Currency")
# currency.to_sql('ap_currency', conn, if_exists='append', index = False)
# #Commit your changes in the database
# conn.commit()
# currency = pd.read_csv("output.csv")
# #Closing the connection
# conn.close()