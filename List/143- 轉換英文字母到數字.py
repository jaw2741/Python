import string
Dic = string.ascii_lowercase

while True:
  a = input()
  for i in range(len(a) ):
    print("(%d)"%Dic.find(a[i]),end='')
  print()