from random import random
D=1000*1000
hits=0
for i in range(1,D+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/D)
print("圆周率的值是：{}".format(pi))
