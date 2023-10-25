"""
while문

    while 조건식:
      조건식의 결과가 참(True)인 동안 반복적으로 실행되는 명령문

조건식의 결과가 언제나 참이라면 무한 루프에 빠질 수 있습니다.
"""

# while 문으로 1~10 까지의 합을 구해봅시다.

sum = 0
n = 1
while n <= 10:
    sum += n
    n += 1
print(sum)

sum = 0
while(True):
    sum += 1
    if sum == 10:
     break
print(sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum2 = 0
for i in numbers:
    sum2 += i
    
print(sum2)

# range(시작, 끝)를 쓰면 for(int i = 0; i <= 10; i++) 하듯이 사용이 가능함
sum3 = 0
for j in range(1, 11):
    sum3 += j
print(sum3)

# range(끝)를 쓰면 for(int i = 0; i <= 10; i++) 하듯이 사용이 가능함 
sum4 = 0
for j in range(11):
    sum4 += j
print(sum4)