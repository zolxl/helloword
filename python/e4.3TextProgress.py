#e4.3TextProgress.py
import time
scale = 50
print("执行开始".center(scale//2,'-'))
'''for i in range(scale+1):
    a,b = '**' * i,'..' * (scale-1)
    c = (i/scale) *100
    print("%{:^3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")

for i in range(101):
    print("\r{:2}%".format(i),end="")
    time.sleep(0.05)'''

t = time.clock()
for i in range(scale+1):
    a = '*'*i
    b = '.'* (scale-i)
    c = (i/scale)*100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end = '')
    time.sleep(1)
print("\n"+"执行结束".center(scale//2,'-'))

