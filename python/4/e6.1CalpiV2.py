#e6.1CalpiV2.py
from random import random
from math import sqrt
from time import clock
DARTS = pow(2,eval(input("请输入整数:")))
hits = 0.0
pi = 0
clock()
for i in range(0,DARTS):
    temp = pow(16,-i) * (4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    pi +=temp
print("Pi的值是{}.".format(pi))
print("运行时间是:{:.5f}".format(clock()))
