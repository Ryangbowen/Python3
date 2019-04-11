def bases(*x):
    temp = []
    for each in x:
        temp.append(each)
    print('提取输入：',temp)
    temp1 = 0
    temp2 = temp.pop()
    for other in range(len(temp)):
        temp1 += temp[other]
        print(temp[other])
    print('除去最后一个的和：',temp1)
    y = temp1 * temp2
    print(y)
