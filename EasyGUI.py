import random, sys
import easygui as g

secret = random.randint(1, 10)
g.msgbox('**********现在开始我们的猜数字游戏吧**********','猜数字游戏', ok_button='确定')
try:
    temp = g.integerbox('不妨猜下我心里想的数字吧(1-10)：',lowerbound=0, upperbound=9)
    print(temp)
    guess = int(temp)
    while guess != secret:
        temp = g.integerbox('哎呀，猜错了，请从新输入吧：',lowerbound=0, upperbound=9)
        guess = int(temp)
        if guess == secret:
            g.msgbox('恭喜，你猜对了！', ok_button='确定')
        else:
            if guess > secret:
                g.msgbox('猜的有点儿大了！', ok_button='确定')
            else:
                g.msgbox('小了，小了', ok_button='确定')
except (ValueError, EOFError, KeyboardInterrupt) as reason:
    print('值输入错误！' + str(reason))
    
g.msgbox('游戏结束，不玩啦！', ok_button='确定')
sys.exit()
