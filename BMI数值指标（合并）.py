try:
    height,weight=eval(input("请输入身高（米）和体重（公斤）[用逗号隔开]："))
    bmi=weight/pow(height,2)
    print("BMI数值为：{:.1f}".format(bmi))
    x,y="",""
    if bmi<18.5:
       x,y="偏瘦","偏瘦"
    elif 18.5<=bmi<24:
       x,y="正常","正常"
    elif 24<=bmi<25:
       x,y="正常","偏胖"
    elif 25<=bmi<28:
       x,y="偏胖","偏胖"
    elif 28<=bmi<30:
       x,y="偏胖","肥胖"
    else:
       x,y="肥胖","肥胖"
    print("BMI(国际)指标为：{0}\nBMI(国内)指标为：{1}".format(x,y))
except:
    print("输入格式有问题")
