temp = [1,2,3,'a',8,8,'g',9,'y',True]
i = 0
for each in range(len(temp)):
    if isinstance(temp[each],int):
        #print(temp[each])
        i += temp[each]
        #print(i)
    else:
        continue
print(i)

