#a3.13DayDayUpV2.py
def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 30 in [ 1,2,3,4,5,6,8,9,10]:
            dayup = dayup * (1+df)
        else:
            dayup = dayup
    return dayup

##dayfactor = [0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010]
##for i in range(10):
##    dayUP(dayfactor[i])
##    print(dayUP(dayfactor[i]))
N = 0
while N <=0.01:
    N=N+0.001
    print("{:.2f}".format(dayUP(N)))
##N=0
##while N<=0.01:
##    N=N+0.001
##    dayup=1.0
##    for i in range(365):
##        if i % 7 in ( 5, 6, 0):     #同上相比，变化了5
##            # print("i")
##            dayup = dayup
## 
##        else:
##            dayup = dayup * (1 + N)
##            #print("{:.2f}".format(dayup))
##    print("{:.2f}".format(dayup))

