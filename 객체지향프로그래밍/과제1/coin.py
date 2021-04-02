"""
과제 번호: 01
문제내용: 두 개의 동전을 던져 모두 같은 면이 나오면 이기고, 아니면 지는 게임
"""

import random


class Coin:
    def __init__(self):
        self.__face_value = random.randint(0, 1)

    def get_face_value(self):
        return self.__face_value

    def throw(self):
        self.__face_value = random.randint(0, 1)


class CoinGame:
    def __init__(self):
        self.coin1 = Coin()
        self.coin2 = Coin()

    def play1(self):
        self.coin1.throw()
        fav1 = self.coin1.get_face_value()

        self.coin2.throw()
        fav2 = self.coin2.get_face_value()

        if fav1 == fav2:
            print('You Win!')
        else:
            print('You lose')

