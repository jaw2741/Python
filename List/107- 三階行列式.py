while True:           
  a ,b ,c  = map(int,input().split())
  d ,e ,f  = map(int,input().split())
  g ,h ,i  = map(int,input().split())
  print( a * e * i + d * h * c + g * b * f - c * e * g - b * d * i - a * f * h )
 