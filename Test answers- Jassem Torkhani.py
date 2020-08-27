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
def div_3(x):
    while True :
        res = 0
        for i in str(x):
            res += int(i)
        x = res
        
        if len(str(res)) == 1:
            if res == 0 or res ==3 or res == 6 or res == 9:
                return True
            else :
                return False

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
    cases = list(chain.from_iterable(voisinsCases( plateau , voisinsCase(plateau,case) )))
    while True :
        flag = False
        for c in cases:
            for cc in voisinsCase(plateau,c):
                if cc not in cases :
                    cases.append(cc)
                    flag = not flag

        if flag == False:
            break


    cases = list(set(cases))
    return cases
    
def chemin(plateau,cased ,casef):
    return (casef in accessibles(plateau,cased))
