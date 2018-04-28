while True :    
  n=list(map(int,input().split()[::-1]))  
  for k in range(len(n)):  
      if k!=len(n)-1:  
          print( "%d "% n[k],end='')  
      else:  
          print ("%d" % n[k],end='')  
  print ('')