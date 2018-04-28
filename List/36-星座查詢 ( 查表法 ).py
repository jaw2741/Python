def f(month, date):  
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)  
    AR36 = ("Capricorn", "Aquarius", "Pisces", "Aries",   
              "Taurus", "Gemini", "Cancer", "Leo", "Virgo",   
              "Libra", "Scorpio", "Sagittarius", "Capricorn")  
    if date < dates[month-1]:  
        return AR36 [month-1]  
    else:  
        return AR36 [month]  
while True :  
  a, b = map (int,input().split())  
  print( f(a,b) ) 