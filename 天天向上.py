S=input("请输入\"百分比")
a=eval(S)
b=1
for i in range(365):
    if i%7 in [6,0]:
        b=b*(1-a)
    else :
        b=b*(1+a)
print("结果:\n{:.2f}".format (b))
