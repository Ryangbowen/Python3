def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)

temp_x = int(input("请输入x: "))
temp_y = int(input("请输入y: "))
temp = power(temp_x, temp_y)
print("%d 的 %d 次方为：%d"% (temp_x, temp_y, temp))
