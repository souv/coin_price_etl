## Data flow
1.get the coin list from coinbase.
2.extract coin price data from coinbase api.
3.calculate the coin diff price 
4.insert data into db
5.make flask app 
6.deploy to Heroku

## using skills:python web scraping, python db connect, crontab, python flask.


## Notice
1.base.csv必須有第一版資料，因為diff會需要吃基本資料才能算出價格變動差距



## Crontab settings
``` bash
*/1 * * * * /opt/anaconda3/bin/python3 /Users/lucaschang/Documents/ETL/coin_price_etl/src/extract_coin_data.py

*/2 * * * * /opt/anaconda3/bin/python3 /Users/lucaschang/Documents/ETL/coin_price_etl/src/coin_price_diff_plot.py

*/3 * * * * /opt/anaconda3/bin/python3 /Users/lucaschang/Documents/ETL/coin_price_etl/src/insert_to_db.py
```
