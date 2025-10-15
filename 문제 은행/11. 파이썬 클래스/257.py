class Human:
    def __init__(self, 이름, 나이, 성별):
        self.이름 = 이름
        self.나이 = 나이
        self.성별 = 성별
    
    def who(self):
        print(f'이름: {self.이름}, 나이: {self.나이}, 성별: {self.성별}')

areum = Human('조아름', 25, '여자')
areum.who()