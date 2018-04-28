import math  
s = input()  
while True :  
  n = int(input())  
  if n > 1:  
      square_n = math.floor( n ** 0.5 )  
      for i in range(2, (square_n+1)):  
          if (n % i) == 0:  
              break  
      else:  
          print(n)  