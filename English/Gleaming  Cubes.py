while True:
  x1 = 0
  y1 = 0
  z1 = 0
  x2 = 9999999999
  y2 = 9999999999
  z2 = 9999999999
  n = int(input())
  if n == 0 :
    break
  for i in range(n) :
    x, y, z, d = map(int,input().split())
    x1 = max(x1, x)
    y1 = max(y1, y)
    z1 = max(z1, z)

    x2 = min(x2, x+d )
    y2 = min(y2, y+d )
    z2 = min(z2, z+d )

  if  x1 >= x2 or y1 >= y2 or z1 >= z2 :
    print('0')
  else :
    r = 0
    r = max( r, abs(x2-x1) * abs(y2-y1) * abs(z2-z1))
    print(r)