while True :    
  a , b  = map(int,input().split())  
  x = pow(a, b, 10)    
  if a == 0 and b == 0 :    
      break    
  print(x) 