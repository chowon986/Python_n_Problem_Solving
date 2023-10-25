"""
for문

    for 변수 in 문자열(or 튜플 or 리스트):
      반복적으로 실행하고자 하는 명령문
"""

# for 문으로 1~10까지의 합을 구해봅시다.

# for문을 쓸 때 변수가 필요 없는 경우 아래와 같이 사용 가능
# for _ in range(11):
# for i in range(6, 1, -1): 뒤에 -1을 붙이면 역순으로 됨

sum = 0
for i in range(11):
    sum += i
print(sum)

sum1 = 0
for i in range(1, 11):
    sum1 += i
print(sum1)

sum2 = 0
for i in range(10, 0, -1):
    sum2 += i
print(sum2)