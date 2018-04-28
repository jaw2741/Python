a, b = input().split()
try:
  c = 0
  for i in range(len(b)):
    s = 0
    for j in range(len(a)):
      if b[i+j] == a[j] and i+j < len(b) :  
          s += 1
      else : break  
    if s == len(a):
      c += 1
  print(c)
except:
  print(c)