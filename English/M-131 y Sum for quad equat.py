Q, W, E , R = map(int,input().split())  
a, b = map(int,input().split())  
s = 0  
for i in range(a , b + 1 ):  
  s += W*i**Q + E*i + R  
print(s) 