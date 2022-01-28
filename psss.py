# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:40:48 2021

@author: Utilisateur
"""
mot1='detentes'
mot2='distances'



def plss(mot1,mot2):
    tab=[]
    for i in range(len(mot1)+1):
        tab.append([0]*(len(mot2)+1))
    for i in range(1,len(mot1)+1):
        for j in range(1,len(mot2)+1):            
                val=[tab[i-1][j]]
                val.append(tab[i][j-1])
                val.append(tab[i-1][j-1]+(1 if mot1[i-1]==mot2[j-1] else 0))
                tab[i][j]=max(val)
    return tab

print(plss(mot1,mot2))