import random
secret = random.randint(1,10)

temp = input("不妨猜一下我心里的数字：")
guess = int(temp)
while guess != secret:
    temp = input("输错了，重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("你是我的蛔虫么？")
        print("哼，猜中了也没有奖励！")
    else:
        if guess >= secret:
            print("大了")
        else:
            print("小了")
print("游戏结束，不玩了！")
