import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price'] - btc['min_price'])

if float(btc['opening_price']) + 변동폭 > float(btc['max_price']):
    print('상승장')
else:
    print('하락장')