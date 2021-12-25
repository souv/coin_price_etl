import pickle as pkl
from coinbase.wallet.client import Client
import requests
import datetime
import pandas as pd
from time import sleep

# load pickle
filename = '/Users/lucaschang/Documents/ETL/coin_price_etl/src/coin_list.pkl'
coin_list = pkl.load(open(filename,'rb'))

client = Client("KazHBMQ18dnkfdkF", "tvysDSfvAif0TePPxJiwU12HU24ZaTMB")

client.get_currencies()

client.get_exchange_rates()

datetime_dt = datetime.datetime.today()# 獲得當地時間
datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")

base_df = pd.read_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/base.csv')

coin_price_list = []
for coin_id in coin_list[0:141]: #[0:141]
    print(len(coin_price_list))
    coin_price = (datetime_str,coin_id,client.get_exchange_rates(currency=coin_id)['rates']['USDT'])
    sleep(3)    
    coin_price_list.append(coin_price)

df = pd.DataFrame (coin_price_list, columns = ['datetime','coin_name','coin_price'])

df3= pd.concat([base_df.reset_index(drop=True),
                df.reset_index(drop = True)],
                axis = 0)

df3.to_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/base.csv',index=False)
print(df3)
