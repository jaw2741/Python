def f(n):
  k = []
  n.sort()
  for i in range( len(n) - 1 ):
      L = i + 1
      R = len(n) - 1
      while L < R :
          sum = n[i] + n[L] + n[R]
          if sum == 0 and [ n[i], n[L], n[R] ] not in k:
              k.append( [ n[i], n[L], n[R] ] )
              L+=1
              R-=1
          elif sum < 0 :
                L += 1
          else:
                R -= 1
  return k

print(f(list(map(int,((input().strip('[')).strip(']')).split(',')))))
