def mul(A, B):  
    return ( ( A[0]*B[0] + A[1]*B[2] ) %1000000, ( A[0]*B[1] + A[1]*B[3] )%1000000,   
             (A[2]*B[0] + A[3]*B[2])%1000000, ( A[2]*B[1] + A[3]*B[3] )%1000000 )  
  
def fib(n):  
    if n==1: return (1, 1, 1, 0)  
    A = fib(n>>1)  
    A = mul(A, A)  
    if n&1: A = mul(A, fib(1))  
    return A  

n = int(input())  
print(fib(n)[1])  