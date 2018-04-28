import sys   
n=input()   
for line in sys.stdin:   
    a,b=map(int,line.split())   
    print(a+b)

#################################

while True :
  n=int(input())   
  for i in range(n):   
      a,b=input().split()
      print(int(a)+int(b))