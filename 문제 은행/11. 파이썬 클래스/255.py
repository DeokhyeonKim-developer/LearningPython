class Human:
    def __init__(self, 이름, 나이, 성별):
        self.이름 = 이름
        self.나이 = 나이
        self.성별 = 성별
    
    def print_attr(self):
        print(self.이름, self.나이, self.성별)

areum = Human('아름', 25, '여자')
areum.print_attr()