ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for price in ohlc[1:]:
    if price[3] > price[0]:
        print(price[1] - price[2])