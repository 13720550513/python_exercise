try:
    score=eval(input("请输入成绩："))
    if 0<=score<60:
      grade="不及格"
    elif 60<=score<70:
      grade="D"
    elif 70<=score<80:
      grade="C"
    elif 80<=score<90:
      grade="B"
    elif 90<=score<=100:
      grade="A"
    print("输入的成绩级别是:"+grade)
except:
    print("输入错误")
else:
    print("结束")
finally:
    print("欢迎下次使用！")
