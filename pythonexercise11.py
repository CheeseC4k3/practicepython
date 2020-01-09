#input
num = input("please enter a number")

#remainers function
def remainers(a):
    return [int(a) % f for f in range(2, int(a))]

#function multiplying all ints in a list, returns "0" if list contains at least one "0"
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

#if funtion output is "0", num has to be a prime number
if multiplyList(remainers(num)) == 0:
    print("dis no prime")
else:
    print("dis prime")
