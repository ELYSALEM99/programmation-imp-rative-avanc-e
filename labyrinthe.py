# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 17:44:42 2021

@author: Utilisateur
"""

import numpy as np
import copy

solution=[]
trajectoire=[]
trouver=False

def lireTerrain():
    Terrain=np.loadtxt("terrain.txt",dtype=str)
    cheminPo_NoPo=[]
    for i in range(len(Terrain)):
        for j in range(len(Terrain[0])):
            cheminPo_NoPo.append("L"+str(i)+"C"+str(j))
    return Terrain,cheminPo_NoPo

Terrain,cheminPo_NoPo=lireTerrain()

print(Terrain)
print(cheminPo_NoPo)

def cheminEau(d,a):
    global solution,trajectoire,trouver
    if d==a:
        #trouver=True
        solution=copy.deepcopy(trajectoire)
        return 
    indd=cheminPo_NoPo.index(d)
    for v in [S for S in cheminPo_NoPo if S not in trajectoire] :
        indv=cheminPo_NoPo.index(v)
        if Terrain[indv//len(Terrain[0])][indv % len(Terrain[0])]=='1' :
            if (indv//len(Terrain[0])-1==indd//len(Terrain[0]) and indv%len(Terrain[0])==indd%len(Terrain[0])) or (indv//len(Terrain[0])+1==indd//len(Terrain[0]) and indv%len(Terrain[0])==indd%len(Terrain[0])) or (indv//len(Terrain[0])==indd//len(Terrain[0]) and indv%len(Terrain[0])-1==indd%len(Terrain[0])) or (indv//len(Terrain[0])==indd//len(Terrain[0]) and indv%len(Terrain[0])+1==indd%len(Terrain[0])):
                trajectoire.append(v)
                cheminEau(v,a)
               # if trouver:
                #    return 
                del trajectoire[-1]

def voirTrajectoire():
    for i in range(len(solution)):
        indi=cheminPo_NoPo.index(solution[i])
        Terrain[indi//len(Terrain[0])][indi % len(Terrain[0])]='E'
    return Terrain
        

d="L0C1"
a="L9C10"
trajectoire.append(d)
cheminEau(d, a)
print("\ntrajectoire\n")
print(solution)
print(voirTrajectoire())