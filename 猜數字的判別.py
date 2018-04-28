n = input()
while True:
  Answer = int(input().strip())
  A = 0
  B = 0
  Number = int(input().strip())
  for i in range(4): #
    if ( (Answer//(10**i))%10 == (int(Number)//(10**i))%10 ):
      A += 1
  for j in range(4): #
    for k in range(4):
        if ( (Answer//(10**j))%10 == (int(Number)//(10**k))%10 ):
          B += 1
  B -= A # 
  print("%da%db" % (A, B))