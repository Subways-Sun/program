def eulerinput():
    return 0
def euler(x0,y0,x,h):
    
##    # derivative=eulerinput()
##    dydx=input("dy/dx=")
##    dydx1=dydx.split('^')
##    list1=[]
##    list11=[]
##    xPosition=0
##    for i in dydx1[0]:
##        list1.append(i)
##    for i in range(len(list1)-1,-1,-1):
##        try:
##            if list1[i]=='x':
##                
##                continue
##            list11.append(int(list1[i]))
##        except ValueError:
##            break
##    print(list11)

    # Recognition feature still developing
    
    from math import sin,cos
    if x-h<=x0:
        # return 0.5*(x-h)*(3-euler(x0,y0,x-h,h))*h+euler(x0,y0,x-h,h)
        # return sin(x-h)*cos(x-h)*h+euler(x0,y0,x-h,h)
        # return (5*(x-h)**2-6/(euler(x0,y0,x-h,h)-2))*h+euler(x0,y0,x-h,h)
        # return (euler(x0,y0,x-h,h)/8*(6-euler(x0,y0,x-h,h)))*h+euler(x0,y0,x-h,h)
        return euler(x0,y0,x-h,h)-(1-euler(x0,y0,x-h,h))*h
    return y0
