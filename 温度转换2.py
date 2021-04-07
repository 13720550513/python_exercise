S=input("请输入带有符号的温度值:")
if S[0] in ['F','f']:
   C=(eval(S[1:])-32)/1.8
   print("转换后的温度是{:.3f}C".format (C))
elif S[0] in ['C','c']:
   F=1.8*eval(S[1:])+32
   print("转换后的温度是{:.3f}F".format (F))
else:
   print('输入格式错误')
