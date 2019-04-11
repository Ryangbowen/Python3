print('----------寻找水仙花----------')
temp = []
temp1 =[]
for frequency in range(100,1000):
    #print(frequency)
    temp = frequency
    #print(temp)
    #print(type(temp))
    for each in range(temp):	#这里报错，
        #print(each)
        temp1.append(temp[0][each])
    if temp1[0][0]**3 + temp1[0][1]**3 + temp1[0][2]**3 == frequency:
        print(frequency)
