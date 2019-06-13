import random

data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
numberList=[]
number=[]

l=len(data)
m=l//10+1
    
while True:
    randomNumber=random.randint(0,9)
    numberList.append(randomNumber)
    while len(number)<l:
        num=0
        for i in range(m):
            a=numberList[0]
            numberList.remove(a)
            num=num+a*(10**(i))
            number.append(num)
            print(num)
            print(number)
            if num>len(data) or num in number:
                number.remove(num)
                continue
            else:
                break
    if len(number)==len(data):
        break

print(number)
