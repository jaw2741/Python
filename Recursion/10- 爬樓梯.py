def f(n , fib = [0, 1]):  
    if n >= len(fib):  
        for i in range(len(fib), n + 1):  
            fib.append(fib[i - 1] + fib[i - 2])  
    return fib[n]  
while True :    
  i=int(input())  
  print(f(i+1))  