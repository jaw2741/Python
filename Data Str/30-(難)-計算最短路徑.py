while True :
  n  = int(input())
  CLK320 = [0]*n  
  for i in range(0,n):  
      CLK320[i] = [0]*n  
      CLK320[i] = list(map(int,input().split() ) ) 


###########################################################################################
## -- 常數宣告
  SIZE = len(CLK320)
  INFINITY = 999999

## -- 全域常數
  Visit = [False] * SIZE
  cost = [INFINITY] * SIZE
  pre  = [None] * SIZE

  def Path():
      for i in range(SIZE):
          print ("%d"   %(cost[i] + 1) )

  def search(start):
      cost [start] = 0
      pre  [start] = start
##########################################################
      while True:
          min = INFINITY
          next = -1
          Visit [start] = True
          #####----------------- 篩選 -----------------#######################################
          for i in range(SIZE):
              if Visit [i]: continue
              if CLK320 [start][i]:
                  d = cost[start] + CLK320 [start][i]
                  if d < cost[i]:
                      cost[i] = d
                      pre[i] = start
              if min > cost[i]:
                  min = cost[i]
                  next = i
          start = next
          if next == -1: break
      Path()

#####################################################################
  if __name__ == '__main__':  
     search(0)