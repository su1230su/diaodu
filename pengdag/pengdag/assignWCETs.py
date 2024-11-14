import random
def assignWCETs(v,minWCET,maxWCET):
    for i in range(0,len(v)-1):
        v[i]['C']=random.uniform(minWCET,maxWCET)
    return v