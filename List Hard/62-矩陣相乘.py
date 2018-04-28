n ,m = map(int,input().split())  
k = [0]*n  
  
for i in range(0,n):  
    k[i] = [0]*m  
    k[i] = list(input().split() )  

a, b = map(int,input().split())  
S = [0]*a  
  
for i in range(0, a):  
    S[i] = [0]*b  
    S[i] = list(input().split() )  
    
import numpy as np  
   
k = np.matrix(k)  
k = k.astype('int')  
  
S = np.matrix(S)  
S = S.astype('int')  
 
#k.shape = (n,m)  
#S.shape = (a,b)  
A = k * S
#A = str(A).strip('[')
for k in range(len(A)) :
  #T = str(A[0]).strip(' ')
  X = str(A[k]).strip('[]')
  X = X.lstrip()
  Y = X.replace('  ',' ')
  Y = Y.replace('   ',' ')
  Y = Y.replace('    ',' ')
  print(Y)
    #print('{:s}'.format( Y ))
  #else :
    #print('{:s}'.format( Y ))
print(A)