def f(a, n) : 
        XOR = a[0]
        for i in range(1, n-2):
          XOR ^= a[i]
        for i in range(1, n+1):
          XOR ^= i
 
        bit = XOR & ~ (XOR-1)
        x = 0
        y = 0
        for i in range(0, n-2):
            if a[i] &  bit :

                x = x ^ a[i]
            else :
                y = y ^ a[i]
        
        for i in range(1, n+1 ):
            if i & bit  :
                x = x ^ i
            else :
                y = y ^ i 
        if x < y :
          print(x, y,end='')
        else :
          print(y, x,end='')
          
        return ''
while True:
  
  n = int(input())
  k = list(map(int,input().split()))
  print( f(k, n) )