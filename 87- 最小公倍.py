import math
"""
    莉眔计程そ计
    isPrime(n)
    getMutiPrime(n)
    getLeastCommonMutible(numList)
"""

def isPrime(n):
    """
    耞计琌借计
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
    盢计 n 秈︽借计だ秆 prime factorization
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
        耞い–琌常
        mutilLsit=[[],[],[]] False
        mutilLsit=[[1],[],[]] True

"""
    for row in mutilLsit:
        if len(row)>0:
            return True
    return False
def getLeastCommonMutible(numList):
    """
    numList ―计
    ウ程そ计借计
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
