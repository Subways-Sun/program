#统计化学成绩
a=0
b=0
c=0
d=0
for i in range(6):
    x=float(input('请输入同学成绩:'))
    if x>=85:
        a+=1
    elif x>=75:
        b+=1
    elif x>=60:
        c+=1
    else:
        d+=1
print('不及格',d,'人')
print('及格',c,'人')
print('良',b,'人')
print('优',a,'人')
