#########        --   兩種方法      -   ############
def f(a): 
  res = 0  
  counts = [0]*(len(a)+1)  
  rank = { v : i+1 for i, v in enumerate(sorted(a)) }  
  for x in reversed(a):  
    i = rank[x] - 1  
    while i:  
      res += counts[i]  
      i -= i & -i  
    i = rank[x]  
    while i <= len(a):  
      counts[i] += 1  
      i += i & -i  
  return res        
  
s = input()  
while True :  
  n = int(input())  
  k  = list(map(int, input().split()))   
  print( f(k) )  
############################################

def binarySearch(alist, item):  
    first = 0  
    last = len(alist) - 1  
    found = False  
  
    while first <= last and not found:  
        midpoint = (first + last)//2  
        if alist[midpoint] == item:  
            return midpoint  
        else:  
            if item < alist[midpoint]:  
                last = midpoint - 1  
            else:  
                first = midpoint + 1  
def f(A):  
    B = list(A)  
    B.sort()  
    inversion_count = 0  
    for i in range(len(A)):  
        j = binarySearch(B, A[i])  
        while B[j] == B[j - 1]:  
            if j < 1:  
                break  
            j -= 1  
  
        inversion_count += j  
        B.pop(j)  
  
    if inversion_count > 1000000000:  
        return -1  
    else:  
        return inversion_count  
  
s = input()  
while True :  
  n = int(input())  
  k  = list(map(int, input().split()))   
  print( f(k) )  