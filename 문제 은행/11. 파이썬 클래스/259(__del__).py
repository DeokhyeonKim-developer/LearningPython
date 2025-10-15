class Human:
    def __init__(self, 이름, 나이, 성별):
        self.이름 = 이름
        self.나이 = 나이
        self.성별 = 성별
    
    def __del__(self):
        print('나의 죽음을 알리지 말라')

    def who(self):
        print(f'이름: {self.이름}, 나이: {self.나이}, 성별: {self.성별}')

    def setInfo(self, 이름, 나이, 성별):
        self.이름 = 이름
        self.나이 = 나이
        self.성별 = 성별

areum = Human('아름', 25, '여자')
del areum