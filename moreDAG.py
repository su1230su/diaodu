# -*- coding: utf-8 -*
from __future__ import division
import math
import copy
import oRTA
import ImpBL
import randomDAG

# 从任务集Tsets中选出类型为s的任务，并将任务组成新的列表Tests_s
def GetST(Tsets,s):
    Tsets_s=[]
    i=0

    while i<len(Tsets):
        Ci = Tsets[i][0]
        Ti = Tsets[i][1]
        Di = Tsets[i][2]
        # 任务类型Si
        Si = Tsets[i][3]
        task=[0,0,0,i]
        # 检查任务类型是否等于给定的类型S
        if Si==s:
            # 将任务的执行时间、最小的任务到达时间间隔、截止时间存入到task[]中
            task[0]=Ci
            task[1]=Ti
            task[2]=Di
            Tsets_s.append(task)
        i=i+1
    return Tsets_s


# 使用高优先级率测试算法（HPRT）计算每个任务在Tsest中的响应时间。
def HPRT(Tsest,Type_S,M):
    # 初始化全为0的列表
    RT=[0 for i in range(len(Tsest))]
    # 遍历任务类型
    for s in Type_S:
        # 取出类型为s的任务
        Tsets_s=GetST(Tsest,s)
        print("taskset is")
        print(Tsets_s)
        # 求出响应时间
        RT_s=oRTA.cal_RT(M[s-1],Tsets_s)
        # 响应时间存在相对应位置
        for i in range(0,len(Tsets_s)):
            index=Tsets_s[i][3]
            RT[index]=RT_s[i]
        # 响应时间中存在0结束
        if 0 in RT_s:
            break
    return RT


# 使用特定的调度算法计算有向无环图任务的响应时间。考虑来自更高优先级任务的干扰。
def Com_DAG_1(DAG,ThpS,Ms):
    # 获取关键路径
    cp=ImpBL.findCriPath(DAG)

    ck=cp
    # 最小的任务到达时间间隔
    T_k=DAG.Ti
    D_k=DAG.Di

    x = ck
    y = 0
    #计算出有向无环图的在最坏情况下的执行时间
    ws=ImpBL.totalAllS(DAG,Ms)
    intra=0

    for i in range(len(ws)):
        intra+=((ws[i])/Ms[i])
    RT = []
    Tsets=[]
    ty_num=len(Ms)
    flag=0
    for s in range(1, ty_num+1):
        # print("s=",s)
        TmpSet_s = GetST(ThpS, s)
        # print("taskset is")
        # print(TmpSet_s)
        M_s = Ms[s-1]
        RT_s = oRTA.cal_RT(M_s, TmpSet_s)
        # 计算出的响应时间中包含0，则将flag设置为1，并终止循环
        if 0 in RT_s:
            flag=1
            break
        else:

        # print ("RT_s=",RT_s)
            RT.append(RT_s)
            Tsets.append(TmpSet_s)
    rt=0
    if flag==1:
        rt=0
    else:
        while (x != y and x <= D_k):
                # if x>D:break
            y = x
            # print("x=%d" % (x))
            total=0
            for s in range(1, ty_num+1):
                # index_s=Type.index(s)
                M_s= Ms[s-1]
                RT_s =RT[s-1]
                TmpSet_s=Tsets[s-1]
                    # for i in range(0, len(TmpSet_s)):
                    #     index = TmpSet_s[i][3]
                    #     RT[index] = RT_s[i]
                # print("Tmpset_s=",TmpSet_s)
                if 0 in RT_s:
                    rt=0
                    break
                else:
                    # print("M_s=",M_s)
                    if M_s>len(TmpSet_s):
                        total+=0
                    else:
                        total += math.floor(oRTA.TotalInt(M_s, TmpSet_s, RT_s, ck, y))/M_s
                        # print("total=%d" % (total))
            x = total + ck+intra
            rt = x
            # print("x=%d" % (x))

        if x != y:
            rt = 0
    return rt


# 计算DAG中单个任务的响应时间，考虑来自更高优先级任务的干扰。
def Com_DAG_2(task,ThpS,Ms):
    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k=task.Di
    RT = []
    Tsets=[]
    ty_num=len(Ms)
    rt=0
    flag=0
    for s in range(1, ty_num+1):
        # print("s=",s)
        TmpSet_s = GetST(ThpS, s)
        # print("taskset is")
        # print(TmpSet_s)
        # M_s等于S类型的核心数
        M_s = Ms[s-1]
        RT_s = oRTA.cal_RT(M_s, TmpSet_s)
        if 0 in RT_s:
            flag=1
            break
        else:
        # print ("RT_s=",RT_s)
            RT.append(RT_s)
            Tsets.append(TmpSet_s)
    # 计算每个顶点的响应时间
    if flag==1:
        Rt_f=0
        return  Rt_f
    else:
        # 当前任务节点
        chV = randomDAG.findpcoDAG().findchild(task.V, task.E)
        # paV = randomDAG.findpcoDAG().findpa(task.V, task.E)
        # print (paV)
        # 与当前任务无关的节点
        paraV = randomDAG.findpcoDAG().findnorelationV(task.V, task.E, task.P)

        # 节点个数
        lenV = len(task.V)
        # 获取图的边
        E = task.E
        FGtemp = [[] * lenV for i in range(lenV)]
        # RT = [0] * lenV
        # 获取节点的直接父节点
        preV = refinefaV(task)
        # preV = [[]]
        # for i in range(1, lenV):  # 每个结点的直接父亲节点parVset
        #     temp = []
        #     for j in range(0, i):
        #         if (j, i) in E:
        #             temp.append(j)
        #     preV.append(temp)
        # print ("preV=",preV)
        # tuopuO = randomDAG.findpcoDAG().BfsOrder(task)

        # 遍历节点
        for i in range(lenV):
            # print ("calculating vertex ",i)
            # first vertex
            if i == 0:
                # if it is a source node
                rt = task.V[i]
                nn_set = []
                for j in range(len(Ms)):
                    nn_set.append(-1)
                ty_i = task.P[i] - 1
                # nearest type s
                nn_set[ty_i] = i
                # tuple?
                FGtemp[i] = [[rt, nn_set]]
            else:
                # print("preV=",preV)
                for j in preV[i]:
                    # print("the vertex %d is a father vertex of %d"%(j,i))
                    # print("FGtemp[j]=", FGtemp)
                    for k in FGtemp[j]:
                        # wi = task.V[i] + k[0]
                        C_k=task.V[i]
                        # print ("wi=",wi)
                        tmpp = []

                        # teh type of i
                        #节点K的执行时间
                        cori = task.P[i] - 1
                        # 前驱节点k的任务类型与当前节点i的任务类型在集合中的索引
                        scv = k[1][cori]
                        # print("scv=", scv)

                        tmset = copy.deepcopy(k[1])
                        if scv != -1:
                            # 当前节点i的前驱节点除了k之外的前驱节点。
                            tmpp = list(set(paraV[i]) - set(paraV[scv]))
                        else:
                            tmpp = paraV[i]
                        lenw = 0.0
                        for p in range(len(tmpp)):
                            # print("i=%d,j=%d,p=%d" % (i, j, tmpp[p]))
                            lenw = lenw + task.V[tmpp[p]]
                        # print ("lenw=",lenw)
                        # 当前节点i与它无关的前驱节点的执行时间总和除以当前节点类型的执行时间
                        intra =lenw / Ms[cori]
                        x=C_k
                        y=0
                        # compute the higher priority tasks interference
                        # 考虑来自高优先级任务干扰，直至干扰不变或者干扰超过最后截止期限
                        while (x != y and x <= D_k):
                            # if x>D:break
                            y = x
                            # print("x=%d" % (x))
                            total=0
                            M_s= Ms[cori]
                            RT_s =RT[cori]
                            TmpSet_s=Tsets[cori]
                                    # for i in range(0, len(TmpSet_s)):
                                    #     index = TmpSet_s[i][3]
                                    #     RT[index] = RT_s[i]
                            # print("Tmpset_s=",TmpSet_s)
                            if 0 in RT_s:
                                rt=0
                                break
                            else:
                                # print("M_s=",M_s)
                                if M_s>len(TmpSet_s):
                                    total+=0
                                else:
                                    total += math.floor(oRTA.TotalInt(M_s, TmpSet_s, RT_s, C_k, y))/M_s
                                    # print("total=%d" % (total))
                            x = total +C_k+intra
                            rt = x
                            # print("x=%d" % (x))

                        if x != y:
                            rt = 0
                            break
                        else:

                            # 前驱节点k的响应时间加到当前节点i的响应时间上
                            rt=rt+k[0]
                            # print("rt=",rt)
                            tmset[cori] = i
                            # 当前节点i的响应时间和任务类型集合组成的元组。
                            ntuple = [rt, tmset]
                            lenFg = len(FGtemp[i])
                            if lenFg == 0:
                                FGtemp[i].append(ntuple)
                            else:
                                flagst = 1
                                for fgn in range(0, lenFg):
                                    if ntuple == FGtemp[i][fgn][1]:
                                        # 标志位为0，不需要添加当前节点的响应时间和任务类型集合元组到列表中
                                        flagst = 0
                                        # 如果当前节点i的响应时间大于列表中已有的响应时间，更新列表中的响应时间
                                        if rt > FGtemp[i][fgn][0]:
                                            FGtemp[i][fgn][0] = rt
                                    else:
                                        flagds1 = 0
                                        flagds2 = 0
                                        # 列表中已有的响应时间和任务类型集合元组
                                        ntuple2 = FGtemp[i][fgn]
                                        for tmpv in range(len(Ms)):
                                            # print("tmpv=",tmpv)
                                            # 如果两个任务类型集合中的某一位置不相等，表示存在不同的节点。
                                            if ntuple[1][tmpv] != ntuple2[1][tmpv]:
                                                # 如果响应时间相等，说明两个节点的冲突
                                                if ntuple[0] == ntuple2[0]:
                                                    tmpminV = ntuple2[1][tmpv]
                                                    tmpmaxV = ntuple[1][tmpv]
                                                    # 设置标志位，表示存在冲突。
                                                    if tmpminV == -1:
                                                        flagds2 = 1
                                                    if tmpmaxV == -1:
                                                        flagds1 = 1
                                                    if tmpmaxV != -1 and tmpminV != -1:
                                                        tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                                                        tmp1 = [v for v in paraV[tmpminV] if v in chV[tmpmaxV]]
                                                        # print("tmp1=", tmp1)
                                                        if len(tmp) == 0:
                                                            flagds1 = 1
                                                            if len(tmp1) == 0:
                                                                flagds2 = 1
                                                            else:
                                                                flagds2 = 0
                                                                break

                                                        else:
                                                            flagds1 = 0
                                                            if len(tmp1) == 0:
                                                                flagds2 = 1
                                                            else:
                                                                flagds2 = 0
                                                                break

                                                else:
                                                    # 如果响应时间不相等，说明两个节点无冲突
                                                    tmpminV = 0
                                                    tmpmaxV = 0
                                                    # 如果当前节点的响应时间大于列表中已有的响应时间
                                                    if ntuple[0] > ntuple2[0]:
                                                        tmpminV = ntuple2[1][tmpv]
                                                        tmpmaxV = ntuple[1][tmpv]
                                                        if tmpmaxV == -1:
                                                            flagds1 = 1
                                                        if tmpminV == -1:
                                                            flagds1 = 0
                                                            break
                                                        # 最大和最小节点都存在
                                                        if tmpmaxV != -1 and tmpminV != -1:
                                                            tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                                                            if len(tmp) == 0:
                                                                flagds1 = 1
                                                            else:

                                                                flagds1 = 0
                                                                # tmpv = numP + 1
                                                                break
                                                    else:
                                                        tmpminV = ntuple[1][tmpv]
                                                        tmpmaxV = ntuple2[1][tmpv]
                                                        # 最大值不存在
                                                        if tmpmaxV == -1:
                                                            flagds2 = 1
                                                        if tmpminV == -1:
                                                            flagds2 = 0
                                                            break
                                                        # 最大和最小节点都存在
                                                        if tmpmaxV != -1 and tmpminV != -1:
                                                            tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                                                            if len(tmp) == 0:
                                                                flagds2 = 1
                                                            else:

                                                                flagds2 = 0
                                                                # tmpv = numP + 1
                                                                break
                                        # ts=time.time()-t0
                                        # print("nodiaoyong=",ts)
                                        # t0 = time.time()
                                        flagds = [flagds1, flagds2]
                                        # 如果当前节点的响应时间大于列表中已有的响应时间
                                        if ntuple[0] > FGtemp[i][fgn][0]:
                                            if flagds[0] == 1:
                                                flagst = 0
                                                FGtemp[i][fgn] = ntuple
                                                break
                                        else:
                                            # 如果当前节点的响应时间小于等于列表中已有的响应时间
                                            if ntuple[0] == FGtemp[i][fgn][0]:
                                                if flagds[0] == 1:
                                                    if flagds[1] == 0:
                                                        flagst = 0
                                                        FGtemp[i][fgn] = ntuple
                                                        break
                                                    else:
                                                        flagst = 0
                                                        break
                                                else:
                                                    if flagds[1] == 1:
                                                        flagst = 0
                                                        break
                                            else:
                                                if flagds[1] == 1:
                                                    flagst = 0
                                                    break

                                if flagst == 1:
                                    FGtemp[i].append(ntuple)
                        # if ntuple not in FGtemp[i]:
                        #      FGtemp[i].append(ntuple)
        # 任务的最终响应时间
        if rt==0:
            RT_f=0
        else:
            rtv = []
            mart = 0
            # print ("the number of all tuple is",len(FGtemp[i]))
            for k in FGtemp[lenV - 1]:
                # print ("k[0]=",k[0])
                rtv.append(k[0])
            if len(rtv) != 0:
                mart = max(rtv)
            # print("mart=", mart)
            RT_f = mart
        return RT_f


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


if __name__ == '__main__':
    Types=[1,2]
    M=[3,2]
    Tsets = [(13, 15,15,1), (41, 45,45,2), (52, 53,53,2), (48, 94,94,1), (38, 98,98,1)]

    rk =HPRT(Tsets,Types,M)
    print (rk)

    # v = [1, 3, 4, 5, 6, 10, 1, 11, 15, 2, 1]
    # e = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 10), (5, 10), (6, 8), (7, 9),
    #      (8, 10), (9, 10)]
    # type = [1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1]
    # MS = [2, 3]
    v=[ 0, 20.716641488647674, 1.179827515110695, 5.15625379958577, 0.22857954582676232, 3.653907595172001, 2.621332512642777, 5.289271942453988, 1.3759206899134426, 23.796665706487286, 2.0121839478843095, 2.309026182262189, 12.248490121105958]
    e=[(0, 1), (0, 2), (0, 3), (0, 4), (0, 7), (0, 10), (0, 11), (1, 6), (2, 12), (3, 5), (3, 6), (4, 9), (5, 8), (
    6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12)]
    P=[5, 5, 2, 1, 4, 2, 1, 2, 2, 1, 3, 4, 2]
    MS = [9, 8, 6, 5, 5]
    THPS = [[2, 20, 20, 4], [9, 47, 47, 2], [5, 59, 59, 2], [78, 76, 76, 0], [43, 97, 97, 0], [102, 155, 155, 3],
            [4, 163, 163, 0], [114, 167, 167, 2], [79, 177, 177, 1], [91, 185, 185, 0], [60, 190, 190, 0],
            [358, 206, 206, 0], [31, 212, 212, 1], [81, 214, 214, 0], [317, 254, 254, 0], [131, 275, 275, 2],
            [60, 277, 277, 0], [131, 283, 283, 0], [174, 300, 300, 4], [500, 332, 332, 0], [438, 392, 392, 3],
            [149, 398, 398, 1], [181, 422, 422, 2], [126, 436, 436, 1], [14, 447, 447, 4], [64, 463, 463, 1],
            [289, 483, 483, 4], [344, 509, 509, 1], [129, 525, 525, 0], [546, 530, 530, 2], [347, 535, 535, 1],
            [240, 541, 541, 0], [283, 580, 580, 1], [287, 603, 603, 3], [235, 604, 604, 2], [80, 613, 613, 1],
            [91, 628, 628, 4], [231, 684, 684, 2], [147, 687, 687, 1], [539, 741, 741, 1], [1454, 792, 792, 4],
            [293, 816, 816, 0], [542, 828, 828, 3], [106, 843, 843, 4], [52, 847, 847, 3], [2, 852, 852, 0],
            [273, 859, 859, 4], [1012, 873, 873, 4], [1541, 888, 888, 2]]

    # print(len(MS))
    # print(len(v))
    # print(len(e))
    # T = randomDAG.DAGtask(v, e, 1000, 1000 , 0, P)
    # rt=Com_DAG_1(T,THPS,MS)
    # print("rt=", rt)
    # R=Com_DAG_2(T,THPS,MS)
    # print("R=",R)