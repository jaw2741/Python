while True:  
  import math  
  l=[]  
  def resolve(num):  
      do=0  
      if num<1:  
          return  
      elif num==1:  
          l.append(num)  
          return  
      for i in range(2,int(math.sqrt(num))+1):  
          if num%i==0:  
              do=1  
              l.append(i)  
              num=num/i  
              resolve(num)  
              break  
      if do==0:  
          l.append(num)  
  num=int(input())  
  resolve(num)  
  
  print ("%d="%num,end='')  
  for k in range(len(l)):  
      if k!=len(l)-1:  
          print( "%d*"%l[k],end='')  
      else:  
          print ("%d" % l[k],end='')  
  print ('')  