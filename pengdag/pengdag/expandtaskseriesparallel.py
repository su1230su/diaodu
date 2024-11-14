import random
from globalVar import gloVal



#     v=expandtaskseriesparallel.expandTasksSeriesParallel(v,[],[],rec_depth,0,0,0)
#     rec_depth = 4
#     gloVal.maxCondBranches = 2
#     gloVal.maxParBranches = 6
#     gloVal.p_term = 0.2
#     gloVal.p_cond = 0
#     gloVal.p_par = 0.8
def expandTasksSeriesParallel(v,source,sink,depth,numBranches,ifcond,condAllow):
    v_curent1={'pred':[], 'succ':[], 'cond':[], 'depth':[], 'width':[], 'C':[], 'accWorkload':[], 'condPred':[], 'branchList':[],'type':[]}
    v_curent2={'pred':[], 'succ':[], 'cond':[], 'depth':[], 'width':[], 'C':[], 'accWorkload':[], 'condPred':[], 'branchList':[],'type':[]}
    if not source and not sink:
        v_curent1['pred']=[]
        v_curent2['succ']=[]
        v_curent2['cond']=0
        v_curent1['depth']=depth
        v_curent2['depth']=-depth
        if condAllow==1:
            if random.randint(1,100)<=50:
                v_curent1['cond']=1
                condBranches=random.randint(1,gloVal.maxCondBranches)
                v[0] = v_curent1
                v[1] = v_curent2
                v=expandTasksSeriesParallel(v,0,1,depth-1,condBranches,1,1)
                return v
        else:
            v_curent1['cond']=0
            parBranches=random.randint(1,gloVal.maxParBranches)
            v[0]=v_curent1
            v[1]=v_curent2
            v=expandTasksSeriesParallel(v,0,1,depth-1,parBranches,0,0)
            return v
    else:
        for i in range(1,numBranches):
            current=len(v)
            if depth==0:
                x=3
            else:
                r=random.random()
                # gloVal.p_par = 0.8
                if r<gloVal.p_par:
                    x=2
                # gloVal.p_term:0.2 + gloVal.p_par:0.8
                elif r<gloVal.p_par+gloVal.p_term:
                    x=3
                else:
                    x=1
            if x==3:                                 # terminal vertex：终端节点
                v_curent1['pred']=[source]
                v_curent1['succ']=[sink]
                v_curent1['cond']=0
                v_curent1['depth']=depth
                v[source]['succ']=v[source]['succ']+[current]
                v[sink]['pred']=v[sink]['pred']+[current]
                v[sink]['cond']=0

                if v[source]['cond']==1:
                    v_curent1['condPred']=v_curent1['condPred']+[source]
                    v_curent1['branchList']=v_curent1['branchList']+[i]
                v_curent1['condPred']=v_curent1['condPred']+v[source]['condPred']
                v_curent1['branchList']=v_curent1['branchList']+v[source]['branchList']
                v[current]=v_curent1

            elif x==2:                              # parallel subgraph：并行子图
                v_curent1['pred']=[source]
                v_curent1['depth']=depth
                v[source]['succ']=v[source]['succ']+[current]
                v[source]['cond']=ifcond
                v_curent2['succ']=[sink]
                v_curent2['depth']=-depth
                v[sink]['pred']=v[sink]['pred']+[current+1]
                v[sink]['cond']=0
                parBranches=random.randint(1,gloVal.maxParBranches)

                if v[source]['cond']==1:
                    v_curent1['condPred']=v_curent1['condPred']+[source]
                    v_curent2['condPred'] = v_curent2['condPred'] + [source]
                    v_curent1['branchList'] = v_curent1['branchList'] + [i]
                    v_curent2['branchList'] = v_curent2['branchList'] + [i]
                v_curent1['condPred'] = v_curent1['condPred'] + v[source]['condPred']
                v_curent1['branchList'] = v_curent1['branchList'] + v[source]['branchList']
                v_curent2['condPred'] = v_curent2['condPred'] + v[source]['condPred']
                v_curent2['branchList'] = v_curent2['branchList'] + v[source]['branchList']
                v[current]=v_curent1
                v[current+1]=v_curent2
                v=expandTasksSeriesParallel(v,current,current+1,depth-1,parBranches,0,condAllow)

            elif x==1:                          # conditional subgraph：条件子图
                v_curent1['pred'] = [source]
                v_curent1['depth'] = depth
                v[source]['succ'] = v[source]['succ'] + [current]
                v[source]['cond'] = ifcond
                v_curent2['succ'] = [sink]
                v_curent2['depth'] = -depth
                v[sink]['pred'] = v[sink]['pred'] + [current + 1]
                v[sink]['cond'] = 0
                condBranches=random.randint(1,gloVal.maxCondBranches)
                if v[source]['cond']==1:
                    v_curent1['condPred']=v_curent1['condPred']+[source]
                    v_curent2['condPred'] = v_curent2['condPred'] + [source]
                    v_curent1['branchList'] = v_curent1['branchList'] + [i]
                    v_curent2['branchList'] = v_curent2['branchList'] + [i]
                v_curent1['condPred'] = v_curent1['condPred'] + v[source]['condPred']
                v_curent1['branchList'] = v_curent1['branchList'] + v[source]['branchList']
                v_curent2['condPred'] = v_curent2['condPred'] + v[source]['condPred']
                v_curent2['branchList'] = v_curent2['branchList'] + v[source]['branchList']
                v[current]=v_curent1
                v[current+1]=v_curent2
                v=expandTasksSeriesParallel(v,current,current+1,depth-1,condBranches,1,condAllow)
        return v



