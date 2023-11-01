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


# class Car():
#     pass

# my_car = Car()

# my_car.color = 'blue'

# print(my_car.color)

# class netflix():
#     pass

# develsplan = netflix()
# develsplan.score = "3점"

# print(develsplan.score)

"""pass가 가능은 하지만 지양할 것"""

# class netflix:
#     def __init__(self, title):
#         self.title = title
    
#     def setScore(self, n):
#         print("{} 점".format(n))

# develsplan = netflix("devels")
# develsplan.setScore(3)

# onepiece = netflix("one")
# onepiece.setScore(4)

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

class Drama:
    def __init__(self, title):
        self.title = title

    def setOperatingTime(self, time):
        print(self.title + "는 {}시에 방영 될 예정입니다.".format(time))

class dramaA(Drama):
    def changeOperatingTime(self, time):
        print(self.title + "는 {}시로 방영 시간이 변경되었습니다.".format(time))

class dramaB(Drama):
    def changeDirector(self, name):
        print(self.title + "는 감독이 {} 으로 변경 되었습니다.".format(name))

d1 = dramaA("드라마 1")
d1.setOperatingTime(3)
d1.changeOperatingTime(5)

d2 = dramaB("드라마 2")
d2.setOperatingTime(4)
d2.changeDirector("새감독")