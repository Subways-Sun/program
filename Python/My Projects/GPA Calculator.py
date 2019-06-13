def GPA():
    import num # Customized module.
    try:
        full=[]
        eachScore=[]
        subjectName=input("The subject is: ")
        numberOfCategories=int(input("The number of categories is: "))
        eachCategory=[]
        for i in range(numberOfCategories):
            a=int(input("The percent of category {0} is: ".format(i+1)))
            scorelist=num.string(input("The scores and each full score of category {0} are: ".format(i+1))).sep()
            x=0
            y=1
            for sc in range(len(scorelist)//2):
                eachScore.append(scorelist[x])
                full.append(scorelist[y])
                x=x+2*sc
                y=y+2*sc
            b=len(eachScore)
            if b==0:
                raise ValueError
            gpaForEachScore=[k*a/100 for k in eachScore]
            gpaForIndex=sum(gpaForEachScore)/b
            eachCategory.append(gpaForIndex)
        totalGpa=round(sum(eachCategory),2)
        print("\nThe GPA of {0} is {1}".format(subjectName,totalGpa))
    except ValueError:
        print("\nPlease enter a number")
    except KeyboardInterrupt:
        print("\nAborted manually.")
    except IndexError:
        print("\nPlease enter equal number of scores and full scores.")
