while True:             
    a=str(input())      
    if (len(a)%2 == 0) or (a.count('0')) or (a.isalpha())  :        
      print('FALSE')      
    elif a==a[::-1]:      
      print('TRUE')      
    else :      
      print('FALSE')  

#####################################

#isalnum()耞琌ダ┪计

#isalpha()耞琌常琌ダ

#istitle()耞–虫迭ダ琌琌糶

#isspace()耞琌琌

#islower()耞ダ琌常琌糶

#isupper()耞ダ琌常琌糶

#isdigit()耞琌常琌计

#s.isspace()┮Τ才常琌フ才\t\n\r 

#耞琌俱计临琌疊翴计
#a=123 
#b=123.123 

# >>>isinstance(a,int) 
# True 
# >>>isinstance(b,float) 
# True 
# >>>isinstance(b,int) 
# False