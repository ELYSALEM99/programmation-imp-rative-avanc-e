# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:30:26 2022

@author: Utilisateur
"""

import sys
import copy

N=30
add=0


def compte(ele1,L):
    global N,add
    if add==N:
        solution.append(copy.deepcopy(lt))
        return
    for V in[S for S in L if S not in lt]:
        if add+V<=N:
            add+=V
            lt.append(V)
            compte(V,L)
            del lt[-1]
            add-=V


L=[2,3,7,8,11,13,8,9,9,21]
lt=[]
i=0
ele1=sys.maxsize

while ele1 > N :
    ele1=L[i]
    i=i+1
solution=[]
lt.append(ele1)
add=ele1
compte(ele1,L)
print()
    