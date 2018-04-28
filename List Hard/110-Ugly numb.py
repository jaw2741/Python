def f(n):  
    if n <= 0:  
        return 0  
    if n == 1:  
        return 1  
    numbers = [1]  
    i2, i3, i5 = 0, 0, 0  
    for k in range(n-1):  
        n2, n3, n5 = numbers[i2] * 2, numbers[i3] * 3, numbers[i5] * 5  
        Min = min(n2, n3, n5)  
        numbers.append(Min)  
        i2 += (Min == n2)  
        i3 += (Min == n3)  
        i5 += (Min == n5)  
    return Min  
while True :
  n = int(input())
  print( f(n) )