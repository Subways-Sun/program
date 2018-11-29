def rstat(possibility,every,true):
    import random
    li=list(range(1,101))
    yes=li[0:possibility]
    poss=0
    index=0
    print("Please wait...")
    while True:
        l=[]
        for i in range(every):
            a=random.randint(1,100)
            l.append(a)
        count=0
        for j in range(len(l)):
            if l[j] in yes:
                count=count+1
        if count==true:
            poss=poss+1
        index=index+1
        if index==500000:
            break
    possb=round(poss/500000,2)
    print("The possibility is approximately {}".format(possb))
