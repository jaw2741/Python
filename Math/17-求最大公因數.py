def gcd(m, n):    
    return m if n == 0 else gcd(n, m % n)    
import sys     
for line in sys.stdin:     
       a,b=map(int,line.split())     
       print(gcd(a,b))