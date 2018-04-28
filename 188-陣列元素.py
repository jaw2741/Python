a = list(map(int,input().split())) 
times = []  
for i in a :  
  times.append(a.count(i))  
if max(times) > (len(a)//2) :
  k = []
  for n in a:
      old = a.count(n)
      num = max(a.count(m) for m in a)
      if num == old:
        k.append(n)
  print(*k[-1:])
else :
  print('n/a')