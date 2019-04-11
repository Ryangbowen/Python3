print('----------寻找水仙花----------')
for i in range(100,1000):
    temp = str(i)
    for j in temp:
        #print(j)
        temp1 = list(temp)
        #print(temp1)
    if (int(temp1[0])**3 + int(temp1[1])**3 + int(temp1[2])**3) == i:
        print(i)
