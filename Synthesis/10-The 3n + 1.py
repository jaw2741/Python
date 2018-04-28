def f(n):  
  c = 1  
  while n != 1 :  
        if n % 2 == 1 :  
            n = 3 * n + 1  
        else :  
            n /= 2  
        c = c + 1  
  return c  
while True :  
  x,y = input().split()  
  x=int(x)  
  y=int(y)  
  if x>y :  
    x ,y = y, x  
  max = 0  
  for i in  range(x,y+1) :  
      if f(i) > max :  
        max = f(i)  
  print( x, y, max);  