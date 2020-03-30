def fib(n):
    a=[0,1]
    if n==0:
        return a[0]
    elif n==1:
        return a[1]
    else:
        for i in range(2,n):
            a.insert(i,a[i-1]+a[i-2])
        return a[i]
