def gray_code(g,n):
    k=len(g)
    if n<=0:
        return

    else:
        for i in range (k-1,-1,-1):
            char='1'+g[i]
            g.append(char)
        for i in range (k-1,-1,-1):
            g[i]='0'+g[i]

        gray_code(g,n-1)

def f (n, s):
    g=['0','1']
    gray_code(g,n-1)
    if n>=1:
        for i in range (len(g)):
            #print (g[i])
            return g[s]
while True:
  a, b=map(int,input().split())
  print( f(a, b) )
  c = int(input())
  if c == -1 :
    break