import pandas as pd 
import mysql.connector

df = pd.read_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/base.csv')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="zzzaaa999",
  database="crawler_db"
)

mycursor = mydb.cursor()

df['coin_price'] = df['coin_price'].astype('object')

records = df.to_records(index=False)

result = list(records)

#drop old version table
mycursor.execute("""drop table coin_price""")

mycursor.execute("CREATE TABLE coin_price (datetime datetime, coin_name VARCHAR(255), coin_price int)")

#insert data into mysql db
mySql_insert_query = """INSERT INTO coin_price (datetime,coin_name,coin_price) VALUES (%s, %s, %s) """

mycursor.executemany(mySql_insert_query, result)

mydb.commit()