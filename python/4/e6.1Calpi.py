#e6.1Calpi.py
from random import random
from math import sqrt
from time import clock
DARTS = pow(2,eval(input("请输入整数:")))
hits = 0.0
clock()
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1.0:
        hits = hits +1
pi = 4 * (hits/DARTS)
print("Pi的值是{}.".format(pi))
print("运行时间是:{:.5f}".format(clock()))
