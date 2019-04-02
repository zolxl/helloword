#a4.5GuessDigitV3.py
from random import *

digit = randint(0,9)
N=0
while True:
    try:
        user = input("请输入猜测的整数:")

    userDigit = eval(user)
    if digit < userDigit:
        print("遗憾，太大了")
        N +=1
    elif digit > userDigit:
        print("遗憾，太小了")
        N +=1
    else:
        print("预测{}次，你猜中了".format(N))
        break
