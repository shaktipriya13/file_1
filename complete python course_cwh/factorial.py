def fac(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fac(n-1)
a=fac(6)
print(a)
print(fac(5))
print(fac(0))   #imp