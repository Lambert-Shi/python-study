###############################循环和分支#################################
#while循环
# while True:
#     print(1)

#for循环
#for 目标 in 表达式:
#循环体
temp = 'Fishc'
for i in temp:
    print(i,end=' ')

member = ['石魁','渣渣','星光']
for i in member:
    print(i,len(i))

#range(start,end,step)
#start:开始数字
#end：结束数字
#step：步长
print(range(5))
print(list(range(5)))

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(2,5,2):
    print(i)

#python中的break和java中的break一样
#python中的continue和java中的continue一样

#学到P10