"""
함수 호출의 원리

결과값이 어떻게 될까요?
"""
def func_C():
    print("C1")
    print("C2")

def func_B():
    print("B1")
    func_C()
    print("B2")

def func_A():
    print("A1")
    func_B()
    print("A2")

func_A()