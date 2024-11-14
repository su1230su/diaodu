# -*- coding: utf-8 -*
from __future__ import division
import math
import copy
import sys

from generate.path import Experiment_rt_Sun_path


from generate.generate import randomDAG
# import moreDAG
import random
import highprio_path
import time


def find_pre_neighbor(task):
    anceV = randomDAG.findpcoDAG().find_ancestors(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)
    # print('preV=',preV)
    faV = copy.deepcopy(preV)
    for i in range(0, lenV):
        for u in preV[i]:
            for v in preV[i]:
                if v != u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break
    # print ("faV=",faV)
    return faV


def suan_ntuple(tasks, Ms):
    num_ntuple = [0] * len(tasks)
    for i in range(len(tasks)):
        num_ntuple[i] = dag_new_ntuple(tasks[i], Ms)
    return num_ntuple
def suan_ntuple1(tasks, Ms):
    num_ntuple = [0] * len(tasks)
    for i in range(len(tasks)):
        num_ntuple[i] = dag_new_ntuple1(tasks[i], Ms)
    return num_ntuple

def dag_new_ntuple(task, Ms):
    # print("###############",tasknum)

    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k = task.Di
    RT = []
    Tsets = []
    ty_num = len(Ms)
    rt = 0

    ###################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    # 找后继节点
    chV = randomDAG.findpcoDAG().find_child(task.V, task.E)
    # 找同类型的并行节点(不在祖先节点和后继节点中)
    paraV = randomDAG.findpcoDAG().find_parallel(task.V, task.E, task.P)

    lenV = len(task.V)

    E = task.E

    FGtemp = [[] * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV = find_pre_neighbor(task)
    t0 = time.time()
    for i in range(lenV):
        # print ("calculating vertex ",i)
        # first vertex
        if i == 0:
            ty_i = task.P[i] - 1
            # if it is a source node
            rtlen = task.V[i]
            # rtlow = types[ty_i][0]/Ms[ty_i]

            # 去除低优先级
            # rtlow=0
            sumc = rtlen
            #  print("rtlen=",rtlen)
            #  print("rtlow=",rtlow)

            # rt= rtlen + rtlow

            rt = rtlen

            nn_set = []
            for j in range(len(Ms)):
                nn_set.append(-1)
            # print(rtlen,rtlow)
            # nearest type s
            # nn_set[ty_i] = i
            # tuple?
            pretype_i = -1  # 路径下一个节点到来时，它的前驱的类型，也就是当前加入的这个点。
            FGtemp[i] = [[rt, nn_set, pretype_i, sumc]]  # 依次是（len+inter+低优先级）、（类型集合）、（前驱节点编号，rt中加入该点值后更新）
        else:
            # print("preV=",preV)
            for j in preV[i]:
                # print("the vertex %d is a father vertex of %d"%(j,i))
                # print("FGtemp[j]=", FGtemp)
                for k in FGtemp[j]:
                    # wi = task.V[i] + k[0]
                    C_k = task.V[i]
                    # print ("wi=",wi)
                    tmpp = []

                    # teh type of i
                    cori = task.P[i] - 1
                    scv = k[1][cori]
                    # print("scv=", scv)

                    tmset = copy.deepcopy(k[1])
                    if scv != -1:
                        tmpp = list(set(paraV[i]) - set(paraV[scv]))
                    else:
                        tmpp = paraV[i]
                    lenw = 0.0
                    for p in range(len(tmpp)):
                        # print("i=%d,j=%d,p=%d" % (i, j, tmpp[p]))
                        lenw = lenw + task.V[tmpp[p]]
                    # print ("lenw=",lenw)
                    ##########################SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
                    intra = lenw / Ms[cori]
                    rtlen = C_k + intra

                    # 去除低优先级
                    # if(k[2]!=cori) :#当前路径最后一个点和新增的点类型进行比较
                    #     rtlow = types[cori][0]/Ms[cori]
                    # else :
                    #     rtlow = types[cori][1]/Ms[cori]
                    # rt = rtlen + rtlow

                    rt = rtlen

                    rt = rt + k[0]
                    sumc = k[3] + C_k
                    # print("rt=",rt)
                    ################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                    tmset[cori] = i
                    ntuple = [rt, tmset, cori, sumc]
                    lenFg = len(FGtemp[i])
                    if lenFg == 0:
                        FGtemp[i].append(ntuple)
                    else:
                        # 原版
                        flagst = 1
                        for fgn in range(0, lenFg):
                            if ntuple[1] == FGtemp[i][fgn][1]:
                                # flagst = 0
                                if rt > FGtemp[i][fgn][0]:
                                    FGtemp[i][fgn][0] = rt
                            else:
                                ntuple2 = FGtemp[i][fgn]
                                flagst -= whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV)
                                if (flagst == 0):
                                    FGtemp[i][fgn] = ntuple
                                    break
                                flagst -= whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV)
                                if (flagst == 0):
                                    break

                        # # 修改版
                        # flagst = 1
                        # for fgn in range(0, lenFg):
                        #     if ntuple[1] == FGtemp[i][fgn][1]:
                        #         # flagst = 0
                        #         if rt > FGtemp[i][fgn][0]:
                        #             # FGtemp[i][fgn] = ntuple
                        #             ntuple2 = FGtemp[i][fgn]
                        #             flagst -= whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV)
                        #             if (flagst == 0):
                        #                 FGtemp[i][fgn] = ntuple
                        #                 break
                        #         else:
                        #             ntuple2 = FGtemp[i][fgn]
                        #             flagst -= whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV)
                        #             if (flagst == 0):
                        #                 break
                        #             else:
                        #                 flagst = 1

                        if flagst == 1:
                            FGtemp[i].append(ntuple)



    # print(f"dag_new的ntuple的time:{TIME}")
    # print("####################dag_new1#######################")
                # if ntuple not in FGtemp[i]:
                #      FGtemp[i].append
    lenth_ntuple = len(FGtemp[lenV -1])

    return lenth_ntuple





def dag_new_ntuple1(task, Ms):
    # print("###############",tasknum)

    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k = task.Di
    RT = []
    Tsets = []
    ty_num = len(Ms)
    rt = 0

    ###################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    # 找后继节点
    chV = randomDAG.findpcoDAG().find_child(task.V, task.E)
    # 找同类型的并行节点(不在祖先节点和后继节点中)
    paraV = randomDAG.findpcoDAG().find_parallel(task.V, task.E, task.P)

    lenV = len(task.V)

    E = task.E

    FGtemp = [[] * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV = find_pre_neighbor(task)
    t0 = time.time()
    for i in range(lenV):
        # print ("calculating vertex ",i)
        # first vertex
        if i == 0:
            ty_i = task.P[i] - 1
            # if it is a source node
            rtlen = task.V[i]
            # rtlow = types[ty_i][0]/Ms[ty_i]

            # 去除低优先级
            # rtlow=0
            sumc = rtlen
            #  print("rtlen=",rtlen)
            #  print("rtlow=",rtlow)

            # rt= rtlen + rtlow

            rt = rtlen

            nn_set = []
            for j in range(len(Ms)):
                nn_set.append(-1)
            # print(rtlen,rtlow)
            # nearest type s
            # nn_set[ty_i] = i
            # tuple?
            pretype_i = -1  # 路径下一个节点到来时，它的前驱的类型，也就是当前加入的这个点。
            FGtemp[i] = [[rt, nn_set, pretype_i, sumc]]  # 依次是（len+inter+低优先级）、（类型集合）、（前驱节点编号，rt中加入该点值后更新）
        else:
            # print("preV=",preV)
            for j in preV[i]:
                # print("the vertex %d is a father vertex of %d"%(j,i))
                # print("FGtemp[j]=", FGtemp)
                for k in FGtemp[j]:
                    # wi = task.V[i] + k[0]
                    C_k = task.V[i]
                    # print ("wi=",wi)
                    tmpp = []

                    # teh type of i
                    cori = task.P[i] - 1
                    scv = k[1][cori]
                    # print("scv=", scv)

                    tmset = copy.deepcopy(k[1])
                    if scv != -1:
                        tmpp = list(set(paraV[i]) - set(paraV[scv]))
                    else:
                        tmpp = paraV[i]
                    lenw = 0.0
                    for p in range(len(tmpp)):
                        # print("i=%d,j=%d,p=%d" % (i, j, tmpp[p]))
                        lenw = lenw + task.V[tmpp[p]]
                    # print ("lenw=",lenw)
                    ##########################SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
                    intra = lenw / Ms[cori]
                    rtlen = C_k + intra

                    # 去除低优先级
                    # if(k[2]!=cori) :#当前路径最后一个点和新增的点类型进行比较
                    #     rtlow = types[cori][0]/Ms[cori]
                    # else :
                    #     rtlow = types[cori][1]/Ms[cori]
                    # rt = rtlen + rtlow

                    rt = rtlen

                    rt = rt + k[0]
                    sumc = k[3] + C_k
                    # print("rt=",rt)
                    ################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                    tmset[cori] = i
                    ntuple = [rt, tmset, cori, sumc]

                    FGtemp[i].append(ntuple)

    lenth_ntuple = len(FGtemp[lenV -1])

    return lenth_ntuple


def whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV):
    flag = 1
    # 如果新路径长度小于已有路径长度
    if ntuple[0] < ntuple2[0]:
        return 0
    # 检查新路径和已有路径的类型集合
    for tmpv in range(len(Ms)):
        tmpminV = ntuple2[1][tmpv]
        tmpmaxV = ntuple[1][tmpv]
        if tmpmaxV != tmpminV:
            # if tmpmaxV == -1:
            #    flag = 1
            if (tmpmaxV != -1 and tmpminV != -1):
                # 在并行节点里查找
                # 从一个列表 paraV[tmpmaxV] 中筛选出另一个列表 chV[tmpminV] 中存在的元素，并将结果存储到临时列表 tmp 中。
                tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]

                if (len(tmp)):
                    flag = 0
                    break
            else:
                flag = 0
                break
    # if (flag):
    #     print("方法二替换",ntuple2,"使用",ntuple)
    return flag


# 是否删减
def whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV):

    flag = 1
    # sum1 = 0
    # sum2 = 0

    # for i in range(len(Ms)):
    #    sum1 += ntuple[2][i]
    # sum1 += ntuple[0]

    # for i in range(len(Ms)):
    #    sum2 += ntuple2[2][i]
    # sum2 += ntuple2[0]

    # 如果当前路径长度大于另一个路径长度，
    if ntuple[0] > ntuple2[0]:
        return 0

    for tmpv in range(len(Ms)):
        tmpminV = ntuple[1][tmpv]
        tmpmaxV = ntuple2[1][tmpv]
        if tmpmaxV != tmpminV:
            # if tmpmaxV == -1:
            #    flag = 1
            if tmpmaxV != -1 and tmpminV != -1:
                tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                if len(tmp):
                    flag = 0
                    break
            else:
                flag = 0
                break
    # if (flag):
    #     print("方法二删除", ntuple, "因为", ntuple2)
    return flag