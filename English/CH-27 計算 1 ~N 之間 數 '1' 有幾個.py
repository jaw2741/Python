def fib(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(i)
    return fib[n]

n=int(input())
while True :
  a = int(input())
  b = int(input())
  c = []
  for i in range(a, b+1 ):
      c.append(str(i))
        
  s = 0    
  for k in c : 
    s  += (k.count('1'))
  print(s) 