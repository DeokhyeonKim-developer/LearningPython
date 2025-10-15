'''
메서드를 정의할때 첫번째 파라미터는 클래스 자기자신이 들어갈 수 있는 파라미터가 지정되어야 하는데 지정되있지 않아서 에러가 난다.
'''

class OMG : 
    def print(self) :
        print("Oh my god")

myStock = OMG()
myStock.print()