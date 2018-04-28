import math 
from sys import stdout 
while True : 
   
  number = int(input()) 
  print ("%d=" %number , end='')  
   
  list = []   
   
  def getChildren(num):   
 
      isZhishu = True   
      i = 2   
      square = int(math.sqrt(num)) + 1   
      while i <= square:   
          if num % i == 0:   
              stdout.write(str(i)) 
              stdout.write('*')   
              isZhishu = False   
              getChildren(num // i)   
              i += 1   
              break   
          i += 1   
      if isZhishu:   
          stdout.write(str(num))   
   
  getChildren(number)  
 
  print ('')