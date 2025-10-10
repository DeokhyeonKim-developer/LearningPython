ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

close_index = ohlc[0].index('close')

for close in ohlc[1:]:
    print(close[close_index])