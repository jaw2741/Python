while True:
  try:
      x,y=str(input()).split() 
      print(pow(int(x),int(y)))
  except:
      break