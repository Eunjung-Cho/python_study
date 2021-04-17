class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return'('+str(self.__x)+', '+str(self.__y)+')'  #ex: '(x.y)'


def main():
    p1 = Point()
    p2 = Point(1.0, 1.0)

    print(p1)
    print(p2)


main()