name = input('请输入待查找的用户名：')
score = [['迷途',85],['黑夜',80],['小布丁',65],['福禄娃娃',95],['怡静',90]]

for each in score:
    #print('score:',each)
    if each[0] == name:
        #print('name:',each)
        print(name + '的得分是：',each[1])
        break

if name != each[0]:
    print('查找的数据不存在！')
