def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
a=fact(eval(input("请输入数字计算阶乘：")))
print(a)
