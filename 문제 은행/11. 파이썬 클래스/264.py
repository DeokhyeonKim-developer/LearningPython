class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

stock = Stock(None, None)
stock.set_name('삼성전자')
stock.set_code('005930')
print(stock.name, stock.code)