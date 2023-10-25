"""
파이썬 함수 만들기

def 함수명():
    수행문장

def 함수이름(매개변수1, 매개변수2):
    수행문장1
    수행문장2
"""

# 예시 1
def func1():
    print("func1 출력")

# 예시 2
def func2(n):
    for i in range(n):
        print("{} 번째 출력".format(i))

# 구구단 함수 변환
def gugudan():
    for i in range(1, 10):
        print("2 * ", i, " = ", 2 * i)

gugudan()

def CountDown(a,b,c):
    for i in range(a, b, c):
        if(i == 0):
            print("발사")
        else:
            print(i, end=" ")

CountDown(5, -1, -1)

# .format
# print("{} 번째 {} 출력".format(i, i +1))