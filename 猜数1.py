import random
secter = random.randint(1,10)
loop = 3

while not loop == 0:
    print("请输入我想数字是多少？有",loop,"次机会：",end = " " )
    temp = input()
    number = int(temp)
    if secter == number and loop == 3:
        print("你是我的蛔虫吧！一次猜对！")
        break
    
    elif secter == number:
        print("猜对了！")
        loop = 0
        break
    
    elif number >= secter:
        print("大了")
        loop -= 1
    elif number <= secter:
        print("大了")
        loop -= 1
print("游戏结束！")
        
