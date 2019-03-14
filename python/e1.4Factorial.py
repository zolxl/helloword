#斐波那契数列
a,b = 0,1
while b < 1000:
    a,b = b,a+b
    print("{}".format(a),end=",")
