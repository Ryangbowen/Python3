def base(*x):
    temp = 0
    for each in x:
        print('每一个值',each)
        temp += each
        print('和',temp)
    y = temp * 5
    print(y)
