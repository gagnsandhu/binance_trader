from binance.client import Client
import api
client= Client(api_key=api.api_key,api_secret=api.api_secret)

info = client.get_all_tickers()


fh=open('Info.json','w')

fh.write(str(info))
fh.close()
s="BTCUSDT"
for i in info:
    if(str(i["symbol"]) == s):
        print("BTCUSDT :",i["price"])

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "10 day ago UTC")
# print(klines)

f=open('historic.json','w')
f.write(str(klines))
f.close()
