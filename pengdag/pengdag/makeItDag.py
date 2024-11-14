import operator
import random
def makeItDAG(v,prob):
    for i in range(0,len(v)-1):
        for j in range(0,len(v)-1):
            if v[i]['depth']>v[j]['depth'] and \
                    v[i]['cond']==0 and \
                    operator.eq(v[i]['condPred'],v[j]['condPred']) and \
                    operator.eq(v[i]['branchList'],v[j]['branchList']) and \
                    j not in v[i]['succ'] and \
                    random.randint(1,100)<=prob*100:
                v[i]['succ']=v[i]['succ']+[j]
                v[j]['pred']=v[j]['pred']+[i]
    return v
