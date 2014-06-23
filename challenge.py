import math
def nCr(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)
def is_range(n,low,up):
    return n if low<=n<=up else exit(1)

t = input()
T = is_range(t,1,100)
for i in range(T):
    s,n,m,k = map(int,raw_input().split())
    s = is_range(s,1,1000)
    n = is_range(n,1,s)
    m = is_range(m,1,s)
    k = is_range(k,0,m)
    probability = 0.000000

    if s == n:
        probability = 1.000000
        
    else:
        favorable = 0
        total = nCr(s,n)
        while(k<=m and k<=n):
            favorable += nCr(m,k)*nCr((s-m),(n-k))
            k += 1
        probability = (favorable/float(total))
    print '{0:.6f}'.format(probability)