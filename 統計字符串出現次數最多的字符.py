import collections
n = input()
while True:
  
  s = input()

  s = ' '.join(s)
  li = s.split(' ')

  from collections import Counter



  items =li

  counters = {}
  for item in items:
      if item in counters:
          counters[item] += 1
      else:
          counters[item] = 1
  print (sorted([(counter,word) for word,counter in counters.items()],reverse=True)[0][1])

