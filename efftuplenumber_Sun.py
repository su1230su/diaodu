#coding=utf-8
import randomDAG
import copy

# 用于比较两个节点集合的差异性
def refinefaV(task):
    anceV= randomDAG.findpcoDAG().findpa(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)
    # print('preV=',preV)
    faV=copy.deepcopy(preV)
    for i in range(0,lenV):
        for u in preV[i]:
            for v in preV[i]:
                if v !=u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break
    # print ("faV=",faV)
    return faV



def findRT(task,MS):
    Xuhao=0
    chV=randomDAG.findpcoDAG().findchild(task.V,task.E)
    # paV = randomDAG.findpcoDAG().findpa(task.V, task.E)
    # print (paV)
    paraV = randomDAG.findpcoDAG().findnorelationV(task.V, task.E, task.P)

    lenV = len(task.V)
    E = task.E
    FGtemp = [[] * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV=refinefaV(task)
    # preV = [[]]
    # for i in range(1, lenV):  # 每个结点的直接父亲节点parVset
    #     temp = []
    #     for j in range(0, i):
    #         if (j, i) in E:
    #             temp.append(j)
    #     preV.append(temp)
    # print ("preV=",preV)
    # tuopuO = randomDAG.findpcoDAG().BfsOrder(task)
    for i in range(lenV):
        # print ("calculating vertex ",i)
        if i==0:
        # if it is a source node
            rt=task.V[i]
            nn_set=[]
            for j in range(len(MS)):
                nn_set.append(-1)
            ty_i=task.P[i]-1
            nn_set[ty_i]=i
            FGtemp[i]=[[rt,nn_set]]
        else:
            # print("preV=",preV)
            for j in preV[i]:
                # print("the vertex %d is a father vertex of %d"%(j,i))
                # print("FGtemp[j]=", FGtemp)
                for k in FGtemp[j]:
                    wi = task.V[i] + k[0]
                    # print ("wi=",wi)
                    tmpp=[]

                    cori=task.P[i]-1
                    scv=k[1][cori]
                    # print("scv=", scv)

                    tmset=copy.deepcopy(k[1])
                    if scv!=-1:
                        tmpp = list(set(paraV[i]) - set(paraV[scv]))
                    else:
                        tmpp=paraV[i]
                    lenw=0.0
                    for p in range(len(tmpp)):
                        # print("i=%d,j=%d,p=%d" % (i, j, tmpp[p]))
                        lenw=lenw+task.V[tmpp[p]]
                    # print ("lenw=",lenw)
                    rt=wi+ lenw/MS[cori]
                    tmset[cori]=i
                    ntuple=[rt,tmset]
                    lenFg=len(FGtemp[i])
                    if lenFg==0:
                        FGtemp[i].append(ntuple)
                    else:
                        flagst = 1
                        for fgn in range(0, lenFg):
                            if ntuple == FGtemp[i][fgn][1]:
                                flagst = 0
                                if rt > FGtemp[i][fgn][0]:
                                    FGtemp[i][fgn][0] = rt
                            else:
                                ntuple2 = FGtemp[i][fgn]
                                flagst -= whether_to_switch(MS, ntuple, ntuple2, paraV, chV)
                                if (flagst == 0):
                                    FGtemp[i][fgn] = ntuple
                                    break
                                flagst -= wherher_to_delete(MS, ntuple, ntuple2, paraV, chV)
                                if (flagst == 0):
                                    break
                        if flagst==1:
                            FGtemp[i].append(ntuple)
                    # if ntuple not in FGtemp[i]:
                    #      FGtemp[i].append(ntuple)
        print("第", Xuhao, "个节点的FGtemp为: ", FGtemp[i])
        Xuhao += 1
    rtv = []
    mart = 0
    nt = 0
    for i in range(lenV):
        nt = nt + len(FGtemp[i])
    # print ("the number of all tuple is",nt)
    for k in FGtemp[lenV - 1]:
        # print ("k[0]=",k[0])
        rtv.append(k[0])
    if len(rtv) != 0:
        mart = max(rtv)
    # print("mart=", mart)
    RT = mart
    nume = len(task.E)
    pr = nume / (lenV * (lenV) / 2)
    # nt = len(FGtemp[lenV - 1])
    return RT, nt, pr

def whether_to_switch(MS,ntuple,ntuple2,paraV,chV):
    flag=1
    if ntuple[0] < ntuple2[0]:
        return 0
    for tmpv in range(len(MS)):
        tmpminV = ntuple2[1][tmpv]
        tmpmaxV = ntuple[1][tmpv]
        # 最大值和最小值不相等
        if tmpmaxV != tmpminV:
            if tmpmaxV == -1:
                flag=1
            elif (tmpmaxV != -1 and tmpminV != -1):
                tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                if (len(tmp)):
                    flag = 0
                    break
            else:
                flag = 0
                break
    if (flag):
        print("替换",ntuple2,"使用",ntuple)
    return flag


def wherher_to_delete(MS,ntuple,ntuple2,paraV,chV):
    flag=1
    if ntuple[0] > ntuple2[0]:
        return 0
    for tmpv in range(len(MS)):
        tmpminV = ntuple[1][tmpv]
        tmpmaxV = ntuple2[1][tmpv]
        if tmpmaxV != tmpminV:
            if tmpmaxV == -1:
                flag=1
            elif (tmpmaxV != -1 and tmpminV != -1):
                tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                if (len(tmp)):
                    flag = 0
                    break
            else:
                flag = 0
                break
    # 如果最大值和最小值不相等
    if (flag):
        print("删除", ntuple, "因为", ntuple2)
    return  flag



























if __name__ == '__main__':

    v=[1,3,4,5,6,10,1,11,15,2,1 ]
    e=[(0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,10),(5,10),(6,8),(7,9),(8,10),(9,10) ]
    type=[1,1,2,1,1,2,2,2,1,1,1]
    MS=[2,3]
#test1
    v = [0, 6.228144750378959, 11.854393845710266, 33.18986864032895, 16.72314913959317, 36.57983842554995,
              6.883061515922677, 12.690585350042639, 41.412152862200315, 6.830296739334428, 5.889877821288273,
              6.798050263083553, 17.30527470227729, 17.172379867494982, 47.21991597999763, 12.506874423001094,
              71.42694037408671, 0.33712161355116677, 26.263486368933634, 60.964537593647975, 0.4819847990607983,
              6.317877785652723]
    e = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 7), (0, 9), (0, 20), (1, 6), (2, 8), (2, 16), (3, 10), (3, 14),
              (4, 5), (5, 10), (6, 15), (7, 10), (7, 11), (7, 14), (8, 21), (9, 18), (10, 13), (11, 12), (12, 13),
              (12, 18), (13, 15), (13, 19), (14, 21), (15, 21), (16, 17), (17, 21), (18, 21), (19, 21), (20, 21)]
    type = [3, 2, 3, 1, 3, 2, 3, 4, 2, 3, 4, 5, 5, 2, 4, 2, 1, 5, 1, 2, 3, 2]
    MS = [2, 3, 4, 5, 6]
#test2
    v = [1, 1, 2, 3, 1, 1, 1, 1]
    e = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 5), (4, 7), (5, 6), (6, 7)]
    type = [1, 2, 2, 3, 2, 4, 2, 4]
    MS = [2, 2, 2, 2]
    # print (len(v))
    # print (len(e))
    T=randomDAG.DAGtask(v,e,100,100,0,type)
    rt=findRT(T,MS)
    print ("rt=",rt)


