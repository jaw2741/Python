import sys  
def comb(n,r):  
    f = lambda n,r:n*f(n-1,r) if n>r else 1  
    return f(n,n-r)//f(r,0)  
for line in sys.stdin:     
    a,b=map(int,line.split())    
    print (comb(a,b))