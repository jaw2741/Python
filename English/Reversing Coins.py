def f(A):  
  count_times = []       
  for i in A :       
    count_times.append(A.count(i))  
  if min(count_times) == len(A):  
    return 0  
  return ( min(count_times) )  
A = list(map(int,input().split()))  
print(f(A))

######################################

k= list(map(int,input().split())) 
times = []  
for i in k :  
  times.append(k.count(i))  
if min(times) == len(k):
  print('0')
else :
  print( (min(times) ) )  