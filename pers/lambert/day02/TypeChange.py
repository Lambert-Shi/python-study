print(15e2)
print(True)
print(False)

a = '520'
print(int(a))

b = 5.99
print(int(b))

c = '520'
print(float(c))

d = 2
print(str(d))

e = str(1.5e10)
print(e)

# str的身份被代替
# str = 'I Love You'
#
# print(str)

# 会出错
# print(str(c))
#---------------------------------------获得关于类型信息 type和isinstance方法-----------------------------------------

a = '520'
print(type(a))

print(type(5.2))

print(type(True))

print(type(5e15))

a = 'lambert.shi'
print(isinstance(a,str))