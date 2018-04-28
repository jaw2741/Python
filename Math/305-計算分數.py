def gcd(m, n):    
    return m if n == 0 else gcd(n, m % n)  
n = input()
while True :
  a, b = input().split(',')
  q, w = map(int,a.split('/'))
  e, r = map(int,b.split('/'))
  x=0
  y=0
  x += (q * r)
  x += (e * w)
  y = w * r
  z = gcd(x, y)
  x //=  z
  y //=  z
  print(str(x)+'/'+str(y))