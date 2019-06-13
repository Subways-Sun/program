def poly(a,b):
    n=len(a)
    if n==0:
        return
    value=0
    for i in range(0,n):
        value=value+a[i]*b**(n-1-i)
    return value

coeff=[2.0, 3.0, 2.0, 0, 4.0]
x=3
resu=poly(coeff,x)
print(resu)
