while True:
    n=int(input())
    s=0
    for i in range(n):
      string=str.lower(input()) 
      if string==string[::-1] :     
           s+=1      
    print(s)