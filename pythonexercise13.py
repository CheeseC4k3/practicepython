#input int for how many fibonucci numbers are to be displayed
num = int(input("how many fibonucci numbers do you want to be generated?"))

#function that finds as many fibonucci numbers as passed
def fibo(top):
    ff = 1
    fff = 0
    l = [1]
    i = 0
    for i in range(0, top - 1):
        f = ff + fff
        l.append(f)
        fff = ff
        ff = f
        i += 1
    return (l)


print(fibo(num))
