num = input("please enter a number")


def remainers(a):
    return [int(a) % f for f in range(2, int(a))]


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


if multiplyList(remainers(num)) == 0:
    print("dis no prime")
else:
    print("dis prime")
