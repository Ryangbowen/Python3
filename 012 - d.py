list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Imposssible is Nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = []

for slogan in list1:
    for name in list2:
        if slogan[0] == name[0]:
            list3.append(name + ':' + slogan[2:])

for each in list3:
    print(each)
