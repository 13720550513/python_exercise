s=input("请输入：")
def rvs(s):
    if s=="":
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs(s))
