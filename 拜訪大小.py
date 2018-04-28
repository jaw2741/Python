n = input()   
while True :   
  k = list(map(int,input().split()))   
  s  = 0   
  s2 = 99999   
  a = []   
  b = []   
  max1 = 0   
  min1 = 0   
  for i in range(len(k)) :   
    if k[i] > s :   
      s = k[i]   
      max1 = i   
      a.append(i)   
         
  for j in range(len(k)) :   
    if k[j] <= s2 :   
      s2 = k[j]   
      min1 = j   
      b.append(j)   
      #print(min)   
  print(abs(s-s2) , end = ' ')   
  Q = 0   
  for i in range(len(a)):   
    for j in range(len(b)):   
      R = a[i] - b[j]   
      min(Q ,abs(R))   
  print( abs ( ( max(a) - max(b) ) ) )  