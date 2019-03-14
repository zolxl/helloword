#温度转换
TempStr = input("请输入摄氏度或者华氏度:")
if TempStr[-1] in ["F","f"]:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转换后的摄氏度为{;.2f}C".format(C))
if TempStr[-1] in ["C","c"]:
    F = eval(TempStr[0:-1])*1.8 + 32
    print("转换后的华氏度为{:.2f}F".format(F))
else:
    print("请检查输入的温度格式")
