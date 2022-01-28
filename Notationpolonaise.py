# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:04:04 2021

@author: Utilisateur
"""





def operande(o):
    result=False
    if(o=="+" or o=="-" or o=="*" or o=="/"):
       result=True
    return result

def opperation(opperande_,a,b):
    res=0
    if opperande_=="+":
        res=int(a)+int(b)
    elif opperande_=="-":
        res=int(a)-int(b)
    elif opperande_=="*":
        res=int(a)*int(b)
    else:
        res=int(a)/int(b)
    return res
    

def evalExpression(expression):
    global trouver
    cpt=0
    if operande(expression[0])==False:
        trouver=True
        return expression[0]
    for i in range(len(expression)):
        if operande(expression[i])==False:
            cpt+=1
        else:
            cpt=0
        if cpt==2:
            expression[i-2]=opperation(expression[i-2], expression[i-1], expression[i])
            del expression[i]
            del expression[i-1]
            evalExpression(expression)
            if trouver:
                return expression[0]

trouver=False

NotationPolonaise="*2+34"
Expression=NotationPolonaise.split()
lt=[]

for i in range(len(Expression[0])):
    lt.append(Expression[0][i])

print(lt)

print(evalExpression(lt))