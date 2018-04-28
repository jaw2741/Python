while True:           
    n = int(input())  
    f = [0 for i in range(100)] 
    f[0] = 1
    f[1] = 1
    for i in range(2,100):
      for j in range(i) :
         f[i] += f[j] * f[i - j]
    print("f(%d)=%d"  %( n, f[n+1] )  )