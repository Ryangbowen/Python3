print('----------查找单词出现次数----------')
def findstr(t,t1):
    i = 0
    m = 0
    for each in t:
        print('字母运行位置：',each)
        if each == t1[0]:
            i = 1
            print('第一个字母相等：',i)
        if each == t1[1] and i == 1:
            m += 1
            i = 0
            print('第二个字母相等：',m)
    print('子字符串在目标字符串中共出现',m,'次')

print('请输入目标字符串：',end=' ')
temp = input() 
print('请输入子字符串(两个字符)：',end=' ')
temp1 = list(input())
findstr(temp,temp1)


