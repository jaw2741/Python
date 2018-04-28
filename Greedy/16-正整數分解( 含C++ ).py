def q(n, m):    
   if m==1 or n==1 :  return 1    
   if n<m :     return q(n,n)    
   if n==m :    return q(n,m-1)+1   
   if n>m :     return q(n,m-1)+q(n-m,m)   
import sys  
while True:  
    x=int(input())  
    print(q(x,x))  
############################################
#include <iostream>  
#include <string.h>  
#include <stdio.h>  
  
using namespace std;  
  
const int N=10005;  
  
int c1[N],c2[N];  
  
int main()  
{  
    int n,i,j,k;  
    while(cin>>n)  
    {  
        if(n==0) break;  
        for(i=0;i<=n;i++)  
        {  
            c1[i]=1;  
            c2[i]=0;  
        }  
        for(i=2;i<=n;i++)  
        {  
            for(j=0;j<=n;j++)  
                for(k=0;k+j<=n;k+=i)  
                    c2[k+j]+=c1[j];  
            for(j=0;j<=n;j++)  
            {  
                c1[j]=c2[j];  
                c2[j]=0;  
            }  
        }  
        cout<<c1[n]<<endl;  
    }  
    return 0;  
}  

##############################################

#include <iostream>  
#include <algorithm>   
using namespace std;    
    
int q(int n,int m){    
    if(n==1||m==1){    
        return 1;    
    }    
    if(n<m)  return q(n,n);    
    if(n==m){    
        return q(n,m-1)+1;    
    }    
    if(n>m)    
        return q(n,m-1)+q(n-m,m);    
}    
    
int main(){    
    int n;    
    while(scanf("%d",&n)!=EOF){    
        printf("%d\n",q(n,n));   
    }    
    return 0;  
}  