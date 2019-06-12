import random
count=0
for i in range(100000):
    a=random.randint(1,100)
    b=random.randint(1,100)
    if (a<=80 or b<=70) or (a<=80 and b<=70):
        count=count+1
print(count/100000)
