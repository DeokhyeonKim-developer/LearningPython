ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []
high_index = ohlc[0].index('high')
low_index = ohlc[0].index('low')

for price in ohlc[1:]:
    volatility += [price[high_index] - price[low_index]]

print(volatility)