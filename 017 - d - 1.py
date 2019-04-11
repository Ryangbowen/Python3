print('----------最大公约数----------')
def MaxCommonDicisor(x,y):
    if x > y:
        m1 = x % y
        if m1 == 0:
            print(y)
        else:
            m2 = y % m1
            M2 = y // m1
            print('第一次的第二余数',m2)
            print('第一次的最大公倍数',M2)
            if m2 == 0:
                print(M2)
            else:
                m3 = 1
                while m3 != 0:
                   m3 = m1 % m2
                   print('第二次m2',m2)
                   print('第二次m1',m1)
                   print('第一余数',m3)
                   if m3 == 0:
                       break
                   else:
                       temp = m3
                       m3 = m1 % temp
                       print('第二余数',m3)
                       if m3 == 0:
                           break
                       else:
                           m1 = temp
                           m2 = m3
                print(m1 // m2)
    else:
        m1 = y % x
        if m1 == 0:
            print(x)
        else:
            m2 = x % m1
            M2 = x // m1
            print('第一次的第二余数',m2)
            print('第一次的最大公倍数',M2)
            if m2 == 0:
                print(M2)
            else:
                m3 = 1
                while m3 != 0:
                   m3 = m1 % m2
                   print('第二次m2',m2)
                   print('第二次m1',m1)
                   print('第一余数',m3)
                   if m3 == 0:
                       break
                   else:
                       temp = m3
                       m3 = m1 % temp
                       print('第二余数',m3)
                       if m3 == 0:
                           break
                       else:
                           m1 = temp
                           m2 = m3
                print(m1 // m2)
        
