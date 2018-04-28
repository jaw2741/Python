while True :  
  N = int(input()) - 1  
  def comb(n,r):   
      p = 1;  
      for i in range(1,r+1):  
          p = p * (n-i+1) // i     
      return p  
  def PASSCA():  
      for n in range(0,N+1):     
          for r in range(0,n+1):    
              if(r == 0):  
                  for i in range(0,(N-n+1)):  
                      print ("", end = '')  
              else:  
                  print ("",end = '')          
              print ("%d"  % comb(n,r) , end = '')  
          print ("\n",end= '')  
  PASSCA()  