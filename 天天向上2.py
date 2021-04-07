
def b(a):
    
    b=1
    for i in range(365):
       if i%7 in [6,0]:
        b=b*(1-0.01)
       else :
        b=b*(1+a)
    return b
a=0.01
while b(a)<37.78:
    a+=0.001
print("工作日的努力参数是：{:.2f}".format(a))
