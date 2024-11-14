import random
def addType(v,typenum):
    for i in range(0,len(v)-1):
        v[i]['type']=random.randint(1,typenum)
    return v