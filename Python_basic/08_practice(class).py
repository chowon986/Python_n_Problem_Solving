# 고릴라 클래스를 구현해서 고릴라 객체를 만드시오!

"""
소리 지를 때마다 바나나 하나씩 소진
바나나가 다 소진 되었는데 또 소리를 지르려고 하면
"배가고파 소리를 지를 수 없습니다." 메세지가 출력되게하시오~


명령예시
gorila_1 = Gorilla()gorila_1.eat(5)

출력예시
바나나를 5개를 먹었습니다.

명령예시
gorila_1.cry(3)

출력예시
우와 ~~~~우와 ~~~~우와 ~~~~
"""

class Gorilla():
    total_banana = 0
    def __init__(self):
        self.bananaCount = 0

    def eat(self, bananaCount):
        print("바나나를 {}개를 먹었습니다.", bananaCount)
        self.bananaCount += bananaCount
        self.total_banana += bananaCount

    def cry(self, cryCount):
        for i in range(cryCount):
            self.bananaCount -= 1
            if(self.bananaCount >= 0):
                print("우와 ~~~~", end="")
            else:
                print("\n배가고파 소리를 지를 수 없습니다.")
                return

gorilla_1 = Gorilla()
gorilla_1.eat(3)
gorilla_1.cry(3)
gorilla_1.cry(6)


"""
상속 및 메소드 오버라이딩 활용

고릴라 클래스 를 상속하여 킹콩 클래스 를 만들어봅니다.

킹콩은 바나나를 먹을때 2배의 효과를 냅니다.
"""

class Kingkong(Gorilla):
    def eat(self, bananaCount):
        print("바나나를 {}개를 먹었습니다.", bananaCount)
        self.bananaCount += bananaCount * 2
        self.total_banana += bananaCount

Kingkong_1 = Kingkong()
Kingkong_1.eat(5)
Kingkong_1.cry(6)
Kingkong_1.cry(5)
print(Kingkong_1.total_banana)
print(gorilla_1.total_banana)