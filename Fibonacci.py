# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 12:02:39 2021

@author: Utilisateur
"""

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)


print(fib(4))


Tab=[0]*100
Tab[0]=Tab[1]=1 
def Fibonacci ( n ) :
   for i in range (2, n+1) :
       Tab[i]= Tab[i-1] + Tab[i-2]
   return Tab[n-1]+Tab[n-2]
print(Fibonacci ( 4 ) )