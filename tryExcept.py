import random

secret = random.randint(1, 10)
print('------猜数字游戏------')
try:
    temp = input('不妨猜下我心里想的数字：')
    guess = int(temp)
    while guess != secret:
        temp = input('哎呀，猜错了，请从新输入吧：')
        guess = int(temp)
        if guess == secret:
            print('恭喜，你猜对了！')
        else:
            if guess > secret:
                print('猜的有点儿大了')
            else:
                print('小了，小了')
except (ValueError, EOFError, KeyboardInterrupt) as reason:
    print('值输入错误！' + str(reason))
    
print('游戏结束，不玩啦！')
