S=input("请输入带格式的温度值:")
if S[0] in ['y','Y']:
    M=eval(S[1:])*8
    print("得到的转换值为{:.2f}M".format(M))
elif S[0] in ['M']:
    Y=eval(S[1:])/8
    print("得到的转换值为{:.2f}Y".format(Y))
else:
    print("输入错误")