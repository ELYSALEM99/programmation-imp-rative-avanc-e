# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 16:20:09 2021

@author: Utilisateur
"""

import sys
import copy

N=30
add=0
LengthSolution=sys.maxsize
meilleurSolution=[]


def compte(ele1,L):
    global N,trouve,add,LengthSolution,meilleurSolution
    if add==N:
        LengthSolution=len(lt)
        meilleurSolution=copy.deepcopy(lt)
        return
    for V in[S for S in L if S not in lt]:
        if add+V<=N and len(lt)<LengthSolution:
            add+=V
            print("add "+str(add))
            lt.append(V)
            print("listtemp "+str(lt))
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
    
lt.append(ele1)
add=ele1
compte(ele1,L)