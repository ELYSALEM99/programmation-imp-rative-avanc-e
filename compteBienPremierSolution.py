# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 12:56:42 2021

@author: Utilisateur
"""
import sys

N=30
trouve=False
add=0


def compte(ele1,L):
    global N,trouve,add
    if add==N:
        trouve=True
        return lt
    for V in[S for S in L if S not in lt]:
        if add+V<=N:
            add+=V
            lt.append(V)
            compte(V,L)
            if trouve:
                return lt
            del lt[-1]
            add-=V


L=[2,3,7,8,11,13,8,9,9,21]
lt=[]
i=0
ele1=sys.maxsize

while ele1 > N :
    ele1=L[i]
    i=i+1
    
lt.append(ele1)
add=ele1
#compte(ele1,L)
print(compte(ele1,L))
    
    