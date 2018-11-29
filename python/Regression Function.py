def refunc():
    import num # Customized module.
    x=num.num(input("The x values are: "))
    y=num.num(input("The y values are: "))
    xsep=x.sep()
    ysep=y.sep()
    n=len(xsep)
    xavg=sum(xsep)/n
    yavg=sum(ysep)/n
    xiyi=0
    xi2=0
    for i in range(n):
        xiyi=xsep[i]*ysep[i]+xiyi
        xi2=xsep[i]**2+xi2
    brd=(xiyi-n*xavg*yavg)/(xi2-n*xavg**2)
    b=round(brd,2)
    a=round(ysep[0]-xsep[0]*brd,2)
    if a>0:
        print("The regression function is y={1}x+{0}".format(a,b))
    if a<0:
        print("The regression function is y={1}x{0}".format(a,b))
    if a==0:
        print("The regression function is y={0}x".format(b))
