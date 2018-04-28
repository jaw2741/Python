def fun(n) :
    x = 2
    y = 6
    for i in range(0,n,1) :
        t = y*1000000
        y = (6 * y + 10000 - 4 * x) % 1000;
        x = t/1000000
    #x = (x == 0)? 999: x - 1;
    if (x==0):
      return 999
    else :
      return x-1
    print("%03d \n" %x);

while True :    
  a,b=input().split()
  a=int(a)
  b=int(b)
  
  for i in range (a,b+1) :
    print("n=%d: %%03d" %i %fun(i) )