def stat():
    from num import num # Customized module.
    l=[]
    form=input('The type of statistic number is: ')
    if form!='avg' and form!='average' and form!='med' and form!='mdn' and form!='median' and form!='mod' and form!='mode' and form!='var' and form!='variance' and form!='std' and form!='stdv' and form!='standard deviation':
        raise ReferenceError
    try:
        inp=string(input('The list of data is: '))
        l=inp.sep()
        avg=sum(l)/len(l)
        if form=='avg' or form=='average':
            print('The average is {0}'.format(avg))
        elif form=='med' or form=='mdn' or form=='median':
            l.sort()
            if len(l)%2==0:
                median1=l[len(l)//2-1]
                median2=l[len(l)//2]
                median=(median1+median2)/2
            elif len(l)%2==1:
                median=l[(len(l)-1)//2]
            print('The median is {0}'.format(median))
        elif form=='mod' or form=='mode':
            occur={}
            mode=[]
            for i in l:
                x=l.count(i)
                occur[i]=x
            md=max(occur.values())
            k=len(occur)
            for p in range(k):
                q=list(occur.popitem())
                r=q[0]
                s=q[1]
                if s==md:
                    mode.append(r)
            mode.sort()
            if len(mode)==1:
                print('The mode is {0}'.format(mode[0]))
            else:
                print('The modes are {0}'.format(mode))
        elif form=='var' or form=='variance' or form=='std' or form=='stdv' or form=='standard deviation':
            m=[]
            for j in range(len(l)):
                c=(l[j]-avg)**2
                m.append(c)
            s2=sum(m)/len(l)
            s1=s2**(1/2)
            if form=='var' or form=='variance':
                print('The variance is {0}'.format(s2))
            elif form=='std' or form=='stdv' or form=='standard deviation':
                print('The standard deviation is {0}'.format(s1))
    except ZeroDivisionError:
        print('Please enter a number.')
    except KeyboardInterrupt:
        print('Aborted manually.')
    except ReferenceError:
        print('Please choose from average, median, mode, variance, or standard deviation.')
    except Exception:
        print('Error occured.')
