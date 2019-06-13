n=int(input('请输入班级人数:'))
b=0
c=0
d=0
e=0
for i in range(n):
        a=float(input('请输入地理成绩:'))
if a>=85:
    b+=1
elif a>=70:
    c+=1
elif a>=60:
    d+=1
else:
    e+=1
print('不及格人数:',e)
print('及格人数:',d)
print('良好人数:',c)
print('优秀人数:',b)
