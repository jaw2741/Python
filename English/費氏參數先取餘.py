a , b  = map(int,input().split())  
def mul(A, B, Q):  
  
    return ( ( A[0]*B[0] + A[1]*B[2])%Q , ( A[0]*B[1] + A[1]*B[3] ) %Q ,     
             (A[2]*B[0] + A[3]*B[2]) %Q, ( A[2]*B[1] + A[3]*B[3] ) %Q  )    
def fib(n,Q):    
    if n==1: return (1, 1, 1, 0)    
    A = fib((n>>1),Q)    
    A = mul(A, A ,Q)    
    if n&1: A = mul(A, fib(1,Q),Q)    
    return A    
try :  
  print(fib(a,b)[1])    
except :  
  print(fib(a,b)[1])