ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

open_index = ohlc[0].index('open')
close_index = ohlc[0].index('close')

for price in ohlc[1:]:
    if price[close_index] >= price[open_index]:
        print(price[close_index])