def kill(people, M):  
    if people ==1: #--²×¤î±ø¥ó  
        return 0  
    return ((kill(people-1,M)+M) % people )  
while True:  
 people = 100  
  
 M = int(input())  
  
 winner = kill(people, M)-1  
 if winner < 0:  
    winner = people  
 print ((winner)+1)  