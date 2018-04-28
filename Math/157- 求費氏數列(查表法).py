def fib(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]
while True :
  n=int(input())
  n=n+1
  for i in range(0, n):
      if i!=n-1 :
        print("%d,"%fib(i),end="")
      else :
        print(fib(i))