#!/usr/bin/env python


##################################################
#################SUJET 1##########################
##################################################
def upperCaser(string):
    m=""
    for x in string:
        if ord(x)>=97 and ord(x)<=122:
            m+=chr(ord(x)-32)
        else: 
            m+=x
    return m
    
##################################################
#################SUJET 2##########################
##################################################
def isMultiply(x):
    b=False
    i=1
    while i<x:
        if i*3==x:
            b=True 
            break
        else:
            i+=1
    return b

##################################################
#################SUJET 3##########################
##################################################

def voisinsCase(plateau , case):
    results = []
    x = case[0]
    y = case[1]
    try :
        if plateau[x][y-1]:
            raise Exception
        results.append((x,y-1))
    except:
        pass

    try :
        if plateau[x][y+1]:
            raise Exception
        results.append((x,y+1))
    except:
        pass

    try :
        if plateau[x-1][y]:
            raise Exception
        results.append((x-1,y))
    except:
        pass

    try :
        if plateau[x+1][y]:
            raise Exception
        results.append((x+1,y))
    except:
        pass

    results = [ x for x in results if -1 not in x ]
    return results


def voisinsCases(plateau , cases):
    results = []

    for case in cases :
        results.append(voisinsCase(plateau,case))

    return results

from itertools import chain
def accessibles(plateau,case):
    x=[]
    h= voisinsCase(plateau,case)
    for l in h:
        a=voisinsCase(plateau,l)
    #unnesting the nested list for better manipulation
    b=list(chain.from_iterable(voisinsCases(plateau,a)))
    x=a+b
    #removing duplicates
    x=list(set(x))
    #removing base case
    x.remove(case)
    return x
    
def chemin(plateau,cased ,casef):
    return (casef in accessibles(plateau,cased))