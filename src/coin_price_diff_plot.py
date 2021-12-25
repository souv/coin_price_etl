import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    diff_pct = (test.iloc[1]-test.iloc[0])/test.iloc[0]
    diff = "%0.2f" % diff
    diff_pct ="%0.2f" % diff_pct
    #print(i,diff)
    tup = (i,diff,diff_pct)
    df4.append(tup)

diff = pd.DataFrame (df4, columns = ['coin_name','coin_diff','coin_diff_pct'])
diff['coin_diff']= diff['coin_diff'].astype('str').astype('float')
diff['coin_diff_pct']= diff['coin_diff_pct'].astype('str').astype('float')

print(diff.info())

diff_desc = diff.sort_values(by=['coin_diff'], ascending=False)

# output the diff table 
diff.to_csv('/Users/lucaschang/Documents/ETL/coin_price_etl/result/coin_diff.csv',index=False)

top_tail_diff = pd.concat([diff_desc.head(5), diff_desc.tail(5)], ignore_index=True)

# ploting
coin = top_tail_diff['coin_name']
coin_diff = top_tail_diff['coin_diff']
fig2 = plt.figure()
x = np.arange(len(coin))
plt.bar(x,coin_diff)
plt.xticks(x, coin) # 刻度
plt.xlabel('coin')
plt.ylabel('coin_diff')
plt.title('coin diff plot')
#plt.show()
fig2.savefig('/Users/lucaschang/Documents/ETL/coin_price_etl/result/coin_diff.png')

diff_desc_pct = diff.sort_values(by=['coin_diff_pct'], ascending=False)
top_tail_diff_pct = pd.concat([diff_desc_pct.head(5), diff_desc_pct.tail(5)], ignore_index=True)

# plotting
coin = top_tail_diff_pct['coin_name']
coin_diff_pct = top_tail_diff_pct['coin_diff_pct']
fig3 = plt.figure()
x = np.arange(len(coin))
plt.bar(x,coin_diff_pct)
plt.xticks(x, coin)
plt.xlabel('coin')
plt.ylabel('coin_diff_pct')
plt.title('coin diff plot %')
#plt.show()
fig3.savefig('/Users/lucaschang/Documents/ETL/coin_price_etl/result/coin_diff_pct.png')
