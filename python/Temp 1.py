import random
c=0
for i in range(500000):
    a=random.randint(650,750)
    b=random.randint(700,800)
    if a>b:
        c=c+1
print(c/500000)
