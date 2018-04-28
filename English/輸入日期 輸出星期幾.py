from datetime import datetime,date  
x = input()  
while True:  
  a, b, c = map(int,input().split())  
  n = datetime( a ,b ,c ).strftime("%w")  
  print ( int(n) + 1  )  