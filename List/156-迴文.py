while True:             
    a=str(input())      
    if (len(a)%2 == 0) or (a.count('0')) or (a.isalpha())  :        
      print('FALSE')      
    elif a==a[::-1]:      
      print('TRUE')      
    else :      
      print('FALSE')  

#####################################

#isalnum()�P�_�O�_�]�t�r���Ϊ̼Ʀr

#isalpha()�P�_�O�_���O�r��

#istitle()�P�_�C�ӳ�����r���O�_�O�j�g

#isspace()�P�_�O�_�O�Ů�

#islower()�P�_�r���O�_�����O�p�g

#isupper()�P�_�r���O�_���O�j�g

#isdigit()�P�_�O�_�����O�Ʀr

#s.isspace()�Ҧ��r�ų��O�ťզr�šB\t�B\n�B\r 

#�P�_�O����٬O�B�I��
#a=123 
#b=123.123 

# >>>isinstance(a,int) 
# True 
# >>>isinstance(b,float) 
# True 
# >>>isinstance(b,int) 
# False