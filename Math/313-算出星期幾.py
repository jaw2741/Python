import datetime  
#if(__name__=="__main__"):  
  #today=int(time.strftime("%w"));  
n = input()  
while True :  
  a, b, c = map(int,input().split())  
  A = datetime.datetime(a ,b ,c).strftime("%w")  
  print( A ) 