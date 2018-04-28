n = input()
def comb(n,r):  
    f = lambda n,r:n*f(n-1,r) if n>r else 1  
    return f(n,n-r)//f(r,0)  
while True :     
    a,b = map(int,input().split())    
    print (comb(a,b))