print('----------十进制转换二进制----------')
def BC(x):
    m = []
    while 1:
        temp = x % 2
        if temp == 0:
            m.append(0)
        else: 
            m.append(1)
        if x != 1:
            x = x // 2
        elif x == 1 and temp == 1:
            break
        else:
            x = x
            
    for each in range(len(m)):
        print(m[each],end='')
