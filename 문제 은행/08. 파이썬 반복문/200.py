ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

total = 0
for price in ohlc[1:]:
    total += (price[3] - price[0])
print(total)