def f(x):
    seq = [x]
    if x == 1 :
      return 1
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x // 2
       else:
         x = 3 * x + 1 
       seq.append(x)    ##--
    return len(seq) - 1
a = input()
while True:
  n =int(input())
  print(f(n))