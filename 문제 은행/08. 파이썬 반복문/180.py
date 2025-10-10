low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []

for i in range(0, len(high_prices)):
    volatility.append(high_prices[i] - low_prices[i])
    print(volatility[i])