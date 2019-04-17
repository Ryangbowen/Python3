def count(temp_1,temp_2):
    temp = [str(temp_1),str(temp_2)]
    print(temp)
    length1 = len(temp)
    data = '1234567890'
    
    for each1 in range(length1):
        a = 0
        d = 0
        s = 0
        o = 0
        length2 = len(temp[each1])
        for each2 in temp[each1]:
            if each2.isalpha():
                a += 1
                print('打印字母：',each2)
            elif each2 in data:
                d += 1
            elif  each2.isspace():
                s += 1
                print('打印空格：',each2)
            else:
                o += 1
                print('打印其他：',each2)
        print('第',each1 + 1,'个字符串共有：英文字母',a,'个','数字',d,'个','空格',s,'个','其他字符',o,'个')


count('I love fishc.com','I love you, you love me.')
            
