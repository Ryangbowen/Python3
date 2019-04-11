list1 = ['0','1','2','3','4','5','6','7','8','9']
temp = 0
while not temp == 'Q':
    i = 0
    temp = input('请输入一个整数：')
    number = str(temp)
    for j in number:
        #print('在list1下面的：',j)
        if j in list1:
            #print('在number下面的：',j)
            i += 1
            #print(i)
        else:
            print('请输入数字或者按Q退出')
            break
    #print('相同字符串宽度：',i)
    #print('字符串宽度：',len(number))
    if i == len(number):
        print('十进制 -> 十六进制：',int(number),'->',hex(int(number)))
        print('十进制 -> 八进制：',int(number),'->',oct(int(number)))
        print('十进制 -> 二进制：',int(number),'->',bin(int(number)))
