"""
재귀 (Recursion)

재귀는 함수가 자기 자신을 다시 호출하는 방식으로 문제를 해결하는 기법입니다.

재귀 호출은 스택의 개념이 적용되며, 함수의 내부는 스택처럼 관리된다. (LIFO, 후입선출)

단점 : 재귀를 사용하면 함수를 반복적으로 호출되는 상황이 벌어지므로, 메모리를 더 많이 사용한다.
"""

# 일반적인 반복문
# 1~5까지의 합
# def sum_list(items):
#     sum = 0
#     for i in items:
#         sum += i
#     return sum
# my_list = [1,2,3,4,5]
# print(sum_list(my_list)) # 15


"""
재귀의 조건
1. base case (기본 케이스 또는 조건)가 있어야 한다.
2. 추가 조건과 기본 케이스의 차이를 확인한다.
3. 반드시 자기 자신(함수)를 호출해야 한다.
"""

# def sum_list(items):
#     if len(items) == 1: # 조건 1. Base Case
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:])   # 조건 3. 반드시 자기 자신(함수)를 호출해야 한다.

"""
조건 2. 추가 조건과 기본 케이스의 차이를 확인한다.
# 1 + sumlist([2,3,4,5])
# 2 + sumlist([3,4,5])
# 3 + sumlist([4,5])
# 4 + sumlist([5])
"""

# def star_print(n):
#     if n == 0: return 
#     star_print(n - 1)
#     return print(n * "*")

# star_print(8)

# def gugu(n):
#     if(n == 0) : return
#     gugu(n - 1)
#     for i in range(1, 10):
#         print("{} * {} = {}".format(n, i, n * i))

# gugu(9)

# def count_down(n):
#     if n == 0:
#         return print("발사")
#     print(n, end=" ")
#     count_down(n - 1)


# count_down(5)

def solution(n):
    if n > 100 :
        return
    if n % 2 == 0:
        print(n, end=" ")
        solution(n + 2)
    else:
        solution(n + 1)

solution(85)

a = [[] for _ in range(5) for _ in range(5)]
print(a)