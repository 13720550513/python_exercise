import time
s=10
print("------执行开始------")
for i in range(s+1):
    a="*"*i
    b="."*(s-i)
    c=(i/s)*100
    print("{:3.0f}%[{}->{}]".format(c,a,b))
    time.sleep (1)
print("------执行结束------")
