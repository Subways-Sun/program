def poly(x):
    ply=input("The polynominal is: ")
    power=[]
    root=[]
    multiply=[]
    divide=[]
    plusminus=[]
    symbol=[]
    every=[]
    plmi=-1
    i=0
    # x^2+x+1, x+2x*x+2*3
    while True:
        a=ply[i]
        i=i+1pok
        try:
            aint=int(a)
        except ValueError:
            symbol.append(a)
        pl=ply.find('+')
        mi=ply.find('-')
        plmi=min(list(pl,mi))
        everystr=ply[
