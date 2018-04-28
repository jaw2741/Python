import math
"""
    ��o�h�Ӽƪ��̤p������
    isPrime(n)
    getMutiPrime(n)
    getLeastCommonMutible(numList)
"""

def isPrime(n):
    """
    �P�_�@�ӼƬO�_�����
    """
    if n==2:
        return True
    if n==1 or n%2==0:
        return False
    p = int(math.sqrt(n))+1
    i = 3
    while i<p:
        if n%i==0:
            return False
        i+=2
    return True

def getMutiPrime(n):
    """get muti num of n
    n=num1*num2...*numx for num1...numx are all prime numbers
    �N�� n �i���]�Ƥ��� prime factorization
    """
    if n==2:
        resultlist = [2]
    else:
        list1 = [i for i in range(2,int(math.sqrt(n))+1) if isPrime(i)]
        #print(list1)
        resultlist=[]
        tmp = n
        while not isPrime(tmp) and tmp!=1:
            for i in list1:
                if tmp%i==0:
                    resultlist.append(i)
                    tmp=tmp//i
                    #print(tmp)
                    #print(resultlist)
        if tmp!=1:
            resultlist.append(tmp)
    return resultlist

def isMutillistFill(mutilLsit):
    """
        �P�_�@�G�C�����C�@�C��O�_������
        mutilLsit=[[],[],[]] ��^False
        mutilLsit=[[1],[],[]] ��^True

"""
    for row in mutilLsit:
        if len(row)>0:
            return True
    return False
def getLeastCommonMutible(numList):
    """
    numList �ݨD�ƪ��C��A
    ��^�����̤p�����ƪ���]�ƦC��
    """
    primelists=[]
    set1=set({})
    mutilResult = []
    for i in numList:
        primelists.append(getMutiPrime(i))
        set1.update(set(i1 for i1 in getMutiPrime(i)))
    #print(primelists)
    flag = True
    flag1 = False
    while flag:
        for i in set1:
            for row in primelists:
                if i in row:
                    row.remove(i)
                    flag1 = True
            if flag1:
                mutilResult.append(i)
                flag1 = False
        flag = isMutillistFill(primelists)
    #print(mutilResult)        
    return mutilResult

def getMutil(numList):
    result = 1
    for i in numList:
        result*=i
    return result

if __name__=='__main__':
  while True :
    n = list(map(int,input().split()))
    print("Lowest common multiple: " + str(getMutil(getLeastCommonMutible( n ))))
