def Fibonacci_1(i):
    if i == 1 or i == 2:
        return 1
    else:
        return Fibonacci_1(i - 1) + Fibonacci_1(i - 2)

temp = Fibonacci_1(20)
print(temp)

def Fibonacci_2():
    list_F = [1,1]
    length = len(list_F)
    for each in range(2,20):
        temp = list_F[each - 1] + list_F[each - 2]
        list_F.append(temp)
    print(list_F[19])
Fibonacci_2()
