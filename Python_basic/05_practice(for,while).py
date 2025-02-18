"""
출력예시를 보고 다음 반복문들을 완성해보세요.
"""

""" 출력예시
★
★★
★★★
★★★★
★★★★★
★★★★★★
★★★★★★★
"""
# 출력 예시 반복문
for i in range(1,8):
    print(i * "★")

""" 문제 1
구구단 2단
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6 
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
"""

# 반복문
for i in range(1, 10):
    print("2 * ", i, " = ", 2 * i)

n = int(input())
for i in range(1,10):
    print("{} * {} = {}".format(n, i, n * i))


""" 문제 2
5 4 3 2 1 발사
"""

# 반복문
for i in range(5, -1, -1):
    if(i == 0):
        print("발사")
    else:
        print(i, end=" ")

# 함수생성
# def prac():
#   for i in range(1, 8):
#       print(i)