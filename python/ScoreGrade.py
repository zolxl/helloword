#ScoreGrade.py
try:
    Score = eval(input("请输入成绩"))
    ScoreGrade = ['A','B','C','D']

    if Score >= 60 and Score < 70:
        print("学生成绩为：",ScoreGrade[3])
    elif Score >=70 and Score < 80:
        print("学生成绩为：",ScoreGrade[2])
    elif Score >=80 and Score < 90:
        print("学生成绩为：",ScoreGrade[1])
    elif Score >=90:
        print("学生成绩为：",ScoreGrade[0])
except NameError:
    print("输入成绩格式有误")
