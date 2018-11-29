def stat(start,stop,count,step,pt):
    try:
        l=[]
        ck=[]
        for i in [stop,count,step]:
            if i==None:
                j=1
                ck.append(j)
        if len(ck)>1 or start==None:
            print("Not enough arguments.")
        if step==None:
            a=stop-start
            step=a//count
        if stop==None:
            stop=start+count*step
        for i in range(start,stop,step):
            l.append(i)
        print("The statistic count is {0}".format(len(l)))
        if pt==None:
            return
        else:
            print("The list is {0}".format(l))
    except ValueError:
        print("Please enter a number.")
    except KeyboardInterrupt:
        print("Aborted manually.")
    except Exception:
        print("Error occured.")
    finally:
        print("Program ended.")
