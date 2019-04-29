def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd((x % y),(y % (x % y)))

temp_x = int(input('输入最大 x ：'))
temp_y = int(input('输入最小 y ：'))
temp = gcd(temp_x, temp_y)
print('%d 和 %d 的最大公约数为：%d'% (temp_x, temp_y, temp))
