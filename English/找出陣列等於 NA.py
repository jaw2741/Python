k= list(input().split() ) 
c = 0
for i in k :  
  if i == 'NA' :
    c += 1
print(c)
for i in range(len(k)) :
  if k[i] == 'NA':
    print(i)