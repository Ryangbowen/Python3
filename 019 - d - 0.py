def huiwenlian(temp):
    s = 0
    temp_h = temp
    length = len(temp_h)
    if length % 2 == 0:
        print('不是回文联！')
    else:
        for each in range((length - 1) // 2):
            if (temp_h[each] == temp_h[-(each + 1)]):
                s += 1
        if s == ((length - 1) //2):
            print('是回文联！')
        else:
            print('不是回文联！')

print('请输入一句话:',end = ' ')
temp_1 = list(input())
huiwenlian(temp_1)



                
