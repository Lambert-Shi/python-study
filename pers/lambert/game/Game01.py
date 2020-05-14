import random

count = 0
flag = random.randint(1,10)
temp = input('请输入一个1-10的数字,看你能猜到我心里像的数字吗')
guess = int(temp)

while guess != flag :
    count = count + 1
    if count == 3:
        print('你还菜不对，也太蠢了把')
        break
    temp = input('猜错啦，请重新输入把')
    guess = int(temp)
    if guess == flag:
        print('我草你怎么知道的？')
    else:
        if guess > flag:
            print('你输入的大了呀')
        else:
            print('你输入的小了呀')
print('游戏结束，不玩了~~~')