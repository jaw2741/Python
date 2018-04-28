import operator
import functools 
def f(k):
        a = functools.reduce(operator.xor, k)
        b = functools.reduce(operator.xor, range(len(k) + 1))
        return a ^ b
n=input()
k = list(map(int,input().split()))
k.append(0)
print(f(k))

###########################################
def f(n):
        return sum (range(len(n)+1)) - sum(n)
a = input()
k = list(map(int,input().split()))
k.append(0)
print(f(k))