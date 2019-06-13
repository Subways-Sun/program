number=int(input('请输入班级人数:'))
Acount=0
Bcount=0
Ccount=0
Fcount=0
for i in range(number):
    grade=float(input('请输入地理成绩:'))
    if grade>=85:
        Acount+=1
    elif grade>=70:
        Bcount+=1
    elif grade>=60:
        Ccount+=1
    else:
        Fcount+=1
print('不及格人数:',Fcount)
print('及格人数:',Ccount)
print('良好人数:',Bcount)
print('优秀人数:',Acount)
