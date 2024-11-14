import getopt
import sys
import expandtaskseriesparallel
import assignWCETs
import makeItDag
import addType
from globalVar import gloVal


def main():
    gloVal.maxCondBranches = 2
    gloVal.maxParBranches = 6
    gloVal.p_cond = 0
    gloVal.p_par = 0.8
    gloVal.p_term = 0.2
    rec_depth = 4
    typeNum=3
    Cmin=1
    Cmax = 100
    addprob=0.3
    v={}
    v=expandtaskseriesparallel.expandTasksSeriesParallel(v,[],[],rec_depth,0,0,0)
    #print(len(v))
    v=assignWCETs.assignWCETs(v,Cmin,Cmax)
    v=makeItDag.makeItDAG(v,addprob)
    v=addType.addType(v,typeNum)
    print(v)
if __name__=="__main__":
    main()