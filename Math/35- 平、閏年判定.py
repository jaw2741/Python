while True:     
  try:
      n = input().strip()     
      if int(n)%4 == 0 and int(n)%100 != 0 :     
          print("Bissextile Year")     
      elif int(n)%400 == 0 :     
          print('Bissextile Year')     
      else:     
          print('Common Year')     
  except :     
        break 