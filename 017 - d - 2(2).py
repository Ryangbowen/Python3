print('----------十进制转换二进制----------')
def Fs(x):
    m = []
    while x:
        quo = x % 2
        x = x // 2
        m.append(quo)
        
    for each in range(len(m)):
        print(m[each],end='')
