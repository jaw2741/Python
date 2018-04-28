k = list(input().split() ) 
R = []
for i in k :
  R.append(i)
w = []
for i in k :
  if i == "NA":
    k.remove(i) 
for i in k :
  w.append(int(i))

sum = 0
for i in w :
	sum += i
Q = str(sum//len(w))

R = [y.replace('NA', Q ) for y in R]
for i in range(len(R)):  
      if i != len(R)-1 :  
          print( "%s "% R[i],end='')  
      else:  
          print ("%s" % R[i],end='')  
print()