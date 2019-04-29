def huiwenlian(temp):
    s = 0 
    temp_h = list(temp)
    print(temp_h)
    temp_f = []
    length_1 = len(temp_h)
    print(length_1)
    for each_1 in range(length_1):
        length = len(temp_h[each_1])
        if length % 2 == 0: 
            temp_f.append('不是回文联！')
        else:
            for each in range((length - 1) // 2):
                if (temp_h[each_1][each] == temp_h[each_1][-(each + 1)]): 																					# 进行反向取数组和正向数组对比。
                    s += 1
            if s == ((length - 1) //2):
                temp_f.append('不是回文联！')
            else:
                temp_f.append('不是回文联！')
    #print(temp_f)

print('请输入一句话:',end = ' ')
temp_1 = input()
huiwenlian(temp_1)
