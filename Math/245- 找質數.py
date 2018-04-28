n = int(input())  
l = [x for x in range(2, n+1) if all(x % i for i in range(2, x))]  
for k in range(len(l)):    
    if k!=len(l)-1:    
        print( "%d "%l[k],end='')    
    else:    
        print ("%d" % l[k],end='\n')    
print(len(l))