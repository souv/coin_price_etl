#計算筆數(13,395筆)
SELECT count(*) from coin_price;

# 抓的時間個數（97個）
SELECT distinct datetime from coin_price;

# btc
select * from coin_price
where coin_name ='BTC'
order by `datetime` ;

# 數據存在哪
select @@datadir;
