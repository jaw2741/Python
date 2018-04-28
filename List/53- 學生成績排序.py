while True :
  n = int(input())
  k = []
  for i in range (n):
    i = int(input())
    k.append(i)
  k.sort()
  for s in k:
    print(s)