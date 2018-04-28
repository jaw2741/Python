from functools import lru_cache
from collections import Counter
import copy

def dissect(n):
    if n == 1:
        return Counter([1]),
    else:
        result = []
        for i in range(1, n):
            ret = copy.deepcopy(dissect(n - i)) 
            for counter in ret:
                counter.update([i])  
                if counter not in result:
                    result.append(counter)  
        result.append(Counter([n]))
        return tuple(result)

def prn(n, tup, k):
    for counter in tup:
        items = []
        for num, times in counter.items():
            items.extend([str(num)] * times)
        if len(items) == k :
          print(''.format(n) + ''.join(items)[::-1])
        # print('+'.join(items))


if __name__ == '__main__':
  while True:
    f = int(input())
    n = int(input()) 
    prn(n, dissect(n), f)