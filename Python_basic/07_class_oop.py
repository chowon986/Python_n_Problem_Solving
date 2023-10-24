"""
# 클래스 선언

class 클래스명():
    변수1
    변수2

    def 함수1(self, ):
        실행할 코드

    def 함수2(self, ):
        실행할 코드


# 객체 선언
객체명 = 클래스명()

# 객체의 메소드 호출
# 메소드명은 클래스에서 정의한 함수명입니다.
# 객체에서 메소드를 호출핳 때 인자는 클래스에서 정의한 함수의 인자만큼 필요합니다.
# 단 클래스를 선언할 때 추가했던 함수의 인자 self는 필요하지 않습니다.
객체명.메소드명()
"""


class Car():
    pass

my_car = Car()

my_car.color = 'blue'

print(my_car.color)



"""
# 상속코드
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):      # Person 클래스 상속받음(name 변수를 파라미터로 재사용)
    def study(self):
        print (self.name + " studies hard")

class Employee(Person):     # Person 클래스 상속받음(name 변수를 파라미터로 재사용)
    def work(self):
        print (self.name + " works hard")

# object 생성
s = Student("Dave")
e = Employee("David")

# object 실행
s.study()
e.work()
"""