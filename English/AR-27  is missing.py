def f(n):    
        return sum (range(len(n)+1)) - sum(n)    
a = input()    
k = list(map(int,input().split()))    
k.append(0)    
print(f(k)) 