# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:37:40 2021

@author: Utilisateur
"""

mot1='detentes'
mot2='distances'

tab=[]
for i in range(len(mot1)+1):
    tab.append(['-']*(len(mot2)+1))

    
def plssRecursive(mot1,mot2):
    if len(mot1)==0: 
        tab[len(mot1)][len(mot2)]=0
        return 0
    if len(mot2)==0: 
        tab[len(mot1)][len(mot2)]=0
        return 0
    val=[plssRecursive(mot1[0:-1],mot2)]
    val.append(plssRecursive(mot1,mot2[0:-1]))
    val1=plssRecursive(mot1[0:-1],mot2[0:-1])+(1 if mot1[-1]==mot2[-1] else 0)
    val2=plssRecursive(mot1[0:-1],mot2)
    if val1!=val2:
        tab[len(mot1)][len(mot2)]=max(val1,val2)
        return max(val1,val2)
    val2=plssRecursive(mot1,mot2[0:-1])
    tab[len(mot1)][len(mot2)]=max(val1,val2)
    return(max(val))


print(plssRecursive(mot1,mot2))