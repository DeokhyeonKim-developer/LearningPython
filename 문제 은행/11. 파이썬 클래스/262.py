class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

stock = Stock('삼성전자', '005930')
print(stock.name, stock.code)