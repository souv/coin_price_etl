import pandas as pd
df = pd.read_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/base.csv')

df['datetime'] = pd.to_datetime(df['datetime'])

tail1 = df.groupby(['coin_name']).tail(1).reset_index()
tail2 = df.groupby(['coin_name']).nth(1).reset_index()

df3= pd.concat([tail1.reset_index(drop=True),
                tail2.reset_index(drop = True)],
                axis = 0)


tail = df.groupby(['coin_name']).tail(2).reset_index()
tail = tail.sort_values(by=['datetime', 'coin_name'])

df4 = []
for i in tail['coin_name'].unique():
    test = tail[tail['coin_name'] == i]['coin_price'] 
    diff = test.iloc[1]-test.iloc[0]
    print(i,diff)
    tup = (i,diff)
    df4.append(tup)

diff = pd.DataFrame (df4, columns = ['coin_name','coin_diff'])

diff.to_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/coin_diff.csv',index=False)
