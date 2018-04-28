while True:           
    n = int(input())  
    f = [0 for i in range(100)] 
    f[0] = 1
    f[1] = 2
    f[2] = 2
    for i in range(2,100):
        f[i] += f[i-1]//4 + f[i-2]//2 + f[i-3]
    print( f[n]  )