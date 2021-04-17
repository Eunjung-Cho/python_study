# 객체 속성 공개
'''
class Robot:
    def __init__(self, name, madeYear =2018):
        self.name = name
        self.madeYear = madeYear
'''


# 객체 속성 캡슐화

class Robot:
    def __init__(self, name, madeYear =2018):
        self.__name = name
        self.__madeYear = madeYear
    #getter
    def get_name(self):
        return self.__name
''
    def get_madeYear(self):
        return self.__madeYear
    #setter -> 값을 세팅해준다
    def set_name(self, name):
        self.__name = name

    def set_madeYear(self, year):
        self.__madeYear = year

def main():
    samBot= Robot('Sambot')
    samBot.set_name('MontBot')
    print(f'My name is {samBot.get_name()}')


main()

