def f(x, y):    
    f = [[0 for i in range(16)] for j in range(16)]    
    for i in range(16):    
        f [15][i] = 1    
    for i in range(1,16):    
      for j in range(i,16):    
        f[15-i][j] = f[15-i][j-1] + f[16-i][j-1] + f[16-i][j]   
        
    return f[15 - x][y]    
a = input()    
while True:             
    n = int(input())      
    print(f(n, n))