print('----------最大公约数----------')
def MCD(x,y):
    if x / y >= 1:
        while 1:
            m = x % y
            if m == 0:
                break
            else:
                temp = m
                m = y % temp
                if m == 0:
                    break
                else:
                    x = temp
                    y = m
        print(y)
    else:
        while 1:
            m = x % y
            if m == 0:
                break
            else:
                temp = m
                m = y % temp
                if m == 0:
                    break
                else:
                    x = temp
                    y = m
        print(y)
        
