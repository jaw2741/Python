#####################################
def countchar(str):
	alist = []
	for i in range(26):	
		alist.append(0)
	str = str.lower()

	for i in str:
		if i.isalpha():		
			alist[ord(i)-97] += 1
	return alist
while True :
  X =  countchar(input())
  for k in range(len(X)):  
      if k!=len(X)-1:  
          print( "%d "%X[k],end='')  
      else:  
          print ("%d" % X[k],end='')  
  print()
##############################################
while True :
  a = input()
  print(a.count('a') + a.count('A'),end=' ')
  print(a.count('b') + a.count('B')  ,end=' ')
  print(a.count('c') + a.count('C'),end=' ')
  print(a.count('d') + a.count('D'),end=' ')
  print(a.count('e') + a.count('E'),end=' ')
  print(a.count('f') + a.count('F'),end=' ')
  print(a.count('g') + a.count('G'),end=' ')
  print(a.count('h') + a.count('H'),end=' ')
  print(a.count('i') + a.count('I'),end=' ')
  print(a.count('j') + a.count('J'),end=' ')
  print(a.count('k') + a.count('K'),end=' ')
  print(a.count('l') + a.count('L'),end=' ')
  print(a.count('m') + a.count('M'),end=' ')
  print(a.count('n') + a.count('N'),end=' ')
  print(a.count('o') + a.count('O'),end=' ')
  print(a.count('p') + a.count('P'),end=' ')
  print(a.count('q') + a.count('Q'),end=' ')
  print(a.count('r') + a.count('R'),end=' ')
  print(a.count('s') + a.count('S'),end=' ')
  print(a.count('t') + a.count('T'),end=' ')
  print(a.count('u') + a.count('U'),end=' ')
  print(a.count('v') + a.count('V'),end=' ')
  print(a.count('w') + a.count('W'),end=' ')
  print(a.count('x') + a.count('X'),end=' ')
  print(a.count('y') + a.count('Y'),end=' ')
  print(a.count('z') + a.count('Z') )