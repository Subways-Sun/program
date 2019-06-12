from math import factorial
a=0
for i in range(1000):
    a+=factorial(i)/i**i
print("i={0}".format(i+1))
print(a)
