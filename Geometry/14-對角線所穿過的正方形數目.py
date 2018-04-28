def gcd(m, n):    
    return m if n == 0 else gcd(n, m % n)    
import sys     
for line in sys.stdin:     
       a,b=map(int,line.split(","))     
       if gcd(a,b)>1:    
        print(a+b-gcd(a,b))    
       else:    
        print((a+b)-1)  