def C(n,r):  
    f = lambda n,r:n*f(n-1,r) if n>r else 1  
    return f(n,n-r)//f(r,0)  
while True :  
  n,m =input().split('=')  
  x = int(n.count('+')) + int(n.count('-')) 
  m = int(m)  
  print (x+1)  
  print ( C( x + m, m ) ) 