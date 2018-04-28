def fib (n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]
a=input()
while True :
  n = int(input())
  for i in range(1, n+1):
      if i == n :
        print(fib (i))
      else:
        print(fib (i), end=' ')