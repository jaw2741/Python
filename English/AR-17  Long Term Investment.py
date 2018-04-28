n = input()
while True :
 j = input()
 s = 0
 max = 0
 k = list(map(int,input().split()))
 for i in range(len(k)):
	 if s < 0 :
		 s = k[i]
	 else :
		 s += k[i]
	 if s > max :
		 max = s
		
 print(max)