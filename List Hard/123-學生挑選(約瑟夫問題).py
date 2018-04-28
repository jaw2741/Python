def Win (n,k):    
    if k==1:    
        return   
    p=0    
    people=list(range(1,n+1))    
    while True:    
        if len(people)==1:    
            break    
        p=(p+(k-1))%len(people)    
        #print('kill:',people[p])    
        del people[p]    
    return people[0]  
while True :  
  a = int(input())  
  print( Win (a,5) ) 



############################################
#原本 C-Math-104 令解決方法

def Win (n,k):  
    p=0  
    people=list(range(1,n+1))  
    while True:  
        if len(people)==1:  
            break  
        p=(p+(k-1))%len(people)  
        #print('kill:',people[p])  
        del people[p]  
    print(people[0] - 1)
    
if __name__=='__main__':     
  while True :
    a = int(input())
    Win(100,a)