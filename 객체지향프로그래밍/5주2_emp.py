class Employee:
    num_of_emps = 0
    rate = 0.1

    def __init__(self, name, pay):
        self.__name = name
        self.__pay = pay
        Employee.num_of_emps += 1

    @property
    def name(self):
        return self.__name

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, rate):
        Employee.rate = rate
        self.__pay = int(self.__pay *(1+Employee.rate))

    def __str__(self):
        return f'이름: {self.__name}, 급여: {self.__pay}'

def main():
    emps = []
    emps.append(Employee('홍길동', 3200))
    emps.append(Employee('임나라', 3300))

    print(f'직원의 수: {Employee.num_of_emps}')
    print(f'급여 인상율: {Employee.rate}')

    for emp in emps: #각각 직원마다 인상을 하기 위해서
        emp.pay = float(input('각 직원의 인상율을 입력하시오: ')) #위의 pay.setter 사용 값을 임의로 설정해보기
        print(emp)


main()