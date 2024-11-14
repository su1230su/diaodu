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


# def EXPERIMENT():
#     #参数区
#     num_tasks=5
#     u=0.8
#     Tmin=0.0001
#     Tmax=10
#     Ndagmin=10
#     Ndagmax=20
#     Mmin=5
#     Mmax=10
#     Pr=0.1
#     numP=10
#     turn=1000
#
#     R = []
#
#     N=0
#
#
#
#     while N < 1:
#
#         N = N + 1
#
#         tempMS = []
#         #if (numP % 2 == 0):
#         #    tempMS = Experiment_rt_Sun.devide_cores_oddodd(numP, Mmin, Mmax, hp_lessthan_m)
#         #else:
#         #    if (hp_lessthan_m % 2 == 0):
#         #        tempMS = Experiment_rt_Sun.devide_cores_oddodd(numP, Mmin, Mmax, hp_lessthan_m)  # 分配核。
#         #    else:
#         #        tempMS = Experiment_rt_Sun.devide_cores_evenodd(numP, Mmin, Mmax, hp_lessthan_m)
#         #tempMS=Experiment_rt_Sun.devide_cores_HP(numP,Mmin,Mmax,hp_lessthan_m)
#         #tempMS = Experiment_rt_Sun.devide_cores(numP, Mmin, Mmax, hp_lessthan_m)
#
#         U = sepU(10, 8, 10)
#         MS = devide_cores_dags(numP, Mmin, Mmax)#核数安排
#         tmin=Tmin  #随机生成dag的最小周期
#         task=[]
#         for s in range(0,num_tasks):#生成dag任务集
#             # T = randomDAG.RandomDAGtask(Ndagmin, Ndagmax, tmin, Tmax, Pr, numP)
#             T = randomDAG.generate_DAG(Ndagmin, Ndagmax, tmin, Tmax, Pr, numP)
#             task.append(T.generate_DAG_task(U[s]))
#             #task.append(T.createtask(u))
#             # print(task[s].Ti)
#             Tmin=task[s].Ti
#
#
#         #处理
#
#         R=get_set_R(task,MS)
#         print(R)
#
#
#
#
#     return R
#
#
# def devide_cores_dags(numP,Mmin,Mmax):
#     MS=[]
#     # NHP=[]
#     for i in range(numP):
#         m = random.randint(Mmin, Mmax)
#         MS.append(m)
#         # n_s = m - random.randint(1,math.floor(m/2))  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
#         # NHP.append(n_s)
#     return MS# [MS,NHP]


def sepU(tasknum, Umin, Umax):
    U = []

    # Usum=random.uniform(Umin,Umax)
    # # print(Usum)
    # for i in range(1, tasknum):
    #     Uleft = Usum * random.uniform(0, 1) ** (1 / (tasknum - i))
    #     U.append(Usum - Uleft)
    #     Usum = Uleft
    # U.append(Usum)
    # random.shuffle(U)

    Umin /= tasknum
    Umax /= tasknum
    for i in range(0, tasknum):
        U.append(random.uniform(Umin, Umax))

    return U


# def get_set_R(task, MS):
#     lenth = len(task)
#     R1 = [0] * lenth
#     R2 = [0] * lenth
#     imp = 0
#     # 求出每一个任务的低优先级干涉（MS和MS-1）两种
#     types = []  # 每一项是一个任务，这一项里有nump个列表，每个列表两项，Ms和Ms-1
#     for i in range(lenth):  # 任务序号
#         temp = []
#         for j in range(len(MS)):  # 当前任务下遍历到何种type
#             #          temp2 =[0,0]
#             the_type = []
#             for k in range(i + 1, lenth):
#                 the_type += task[k].typeddag[j]  # 遍历每一个低优先级任务这个类型的节点集合，结果为集合
#
#             count = len(the_type)
#             while (count < MS[j]):  # 补齐到至少MS个
#                 the_type.append(0)
#                 count += 1
#             the_type.sort(reverse=True)  # 列表排序
#             AMS = 0
#
#             BMS = 0
#             for x in range(MS[j] - 1):
#                 BMS += the_type[x]  # 前ms-1个求和
#             AMS = BMS + the_type[MS[j] - 1]
#             temp2 = [AMS, BMS]
#
#             temp.append(temp2)
#
#         types.append(temp)
#     #################################  求R序列  ###################################
#     SUCCESS1 = 1
#     SUCCESS2 = 1
#     # t0 = time.time()
#     for i in range(lenth):
#         if (i == 0):
#             flag1 = 1
#             flag2 = 1
#         tasksss = []
#         for j in range(0, i):
#             tasksss.append(task[j])e4rf5=-==
#         # i为当前任务序号,tasksss为高优先级dag任务集，types[i]为当前任务的各类型低优先级任务干涉，R为当前已经计算的（高优先级任务）响应时间集。
#         tempR = dag_new(task[i], i, tasksss, MS, types[i], R1, flag1)
#         if tempR == 0:
#             SUCCESS1 = 0
#
#         flag1 = 0
#         R1[i] = tempR
#
#
#         tempR2 = dag_new3(task[i], i, tasksss, MS, types[i], R2, flag2)
#
#         if tempR2 == 0:
#             SUCCESS2 = 0
#
#         flag2 = 0
#         R2[i] = tempR2
#
#         if tempR != 0:
#             imp += (tempR - tempR2) /tempR
#         elif tempR ==0 and tempR2 != 0:
#             imp += 1
#     #     if tempR == 0:
#     #         SUCCESS = 0
#     #         continue
#     #     flag = 0
#     #     R[i] = tempR
#     # t1 = time.time()
#     # TIME = t1 - t0
#
#
#     return [R1, R2, 0 , 0, SUCCESS1 ,SUCCESS2 ,imp]

# 原版
def get_set_R(task, MS):
    lenth = len(task)
    R = [0] * lenth
    num_ntuple = [0] *lenth
    # 求出每一个任务的低优先级干涉（MS和MS-1）两种
    types = []  # 每一项是一个任务，这一项里有nump个列表，每个列表两项，Ms和Ms-1
    for i in range(lenth):  # 任务序号
        temp = []
        for j in range(len(MS)):  # 当前任务下遍历到何种type
            #          temp2 =[0,0]
            the_type = []
            for k in range(i + 1, lenth):
                the_type += task[k].typeddag[j]  # 遍历每一个低优先级任务这个类型的节点集合，结果为集合
            count = len(the_type)
            while (count < MS[j]):  # 补齐到至少MS个
                the_type.append(0)
                count += 1
            the_type.sort(reverse=True)  # 列表排序
            AMS = 0
            BMS = 0
            for x in range(MS[j] - 1):
                BMS += the_type[x]  # 前ms-1个求和
            AMS = BMS + the_type[MS[j] - 1]
            temp2 = [AMS, BMS]
            temp.append(temp2)
        types.append(temp)
    #################################  求R序列  ###################################
    SUCCESS = 1
    t0 = time.time()
    for i in range(lenth):
        if (i == 0):
            flag = 1
        tasksss = []
        for j in range(0, i):
            tasksss.append(task[j])
        # i为当前任务序号,tasksss为高优先级dag任务集，types[i]为当前任务的各类型低优先级任务干涉，R为当前已经计算的（高优先级任务）响应时间集。
        tempR = dag_new(task[i], i, tasksss, MS, types[i], R, flag)
        if tempR[0] == 0:
            SUCCESS = 0
            R[i] = tempR[0]
            num_ntuple[i] = tempR[1]
            break
        flag = 0
        R[i] = tempR[0]
        num_ntuple[i] = tempR[1]
    t1 = time.time()
    TIME = t1 - t0
    return [R, TIME, SUCCESS, num_ntuple]


def get_set_R1(task, MS):
    lenth = len(task)
    R = [0] * lenth
    num_ntuple = [0] * lenth
    # 求出每一个任务的低优先级干涉（MS和MS-1）两种
    types = []  # 每一项是一个任务，这一项里有nump个列表，每个列表两项，Ms和Ms-1
    for i in range(lenth):  # 任务序号
        temp = []
        for j in range(len(MS)):  # 当前任务下遍历到何种type
            #          temp2 =[0,0]
            the_type = []
            for k in range(i + 1, lenth):
                the_type += task[k].typeddag[j]  # 遍历每一个低优先级任务这个类型的节点集合，结果为集合
            count = len(the_type)
            while (count < MS[j]):  # 补齐到至少MS个
                the_type.append(0)
                count += 1
            the_type.sort(reverse=True)  # 列表排序
            AMS = 0
            BMS = 0
            for x in range(MS[j] - 1):
                BMS += the_type[x]  # 前ms-1个求和
            AMS = BMS + the_type[MS[j] - 1]
            temp2 = [AMS, BMS]
            temp.append(temp2)
        types.append(temp)
    #################################  求R序列  ###################################
    SUCCESS = 1
    t0 = time.time()
    for i in range(lenth):
        if (i == 0):
            flag = 1
        tasksss = []
        for j in range(0, i):
            tasksss.append(task[j])
        # i为当前任务序号,tasksss为高优先级dag任务集，types[i]为当前任务的各类型低优先级任务干涉，R为当前已经计算的（高优先级任务）响应时间集。
        tempR = dag_new3(task[i], i, tasksss, MS, types[i], R, flag)
        # 初始值为路径长度的global_fp
        # tempR = dag_new2(task[i], i, tasksss, MS, types[i], R, flag)
        if tempR[0] == 0:
            SUCCESS = 0
            R[i] = tempR[0]
            num_ntuple[i] = tempR[1]
            break
        flag = 0
        R[i] = tempR[0]
        num_ntuple[i] = tempR[1]
    t1 = time.time()
    TIME = t1 - t0
    return [R, TIME, SUCCESS, num_ntuple]


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


def find_pre(task):
    anceV = randomDAG.findpcoDAG().find_ancestors(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)

    return preV


# 原版---
def dag_new(task, tasknum, tasks, Ms, types, Reshigh, flag):
    # print("###############",tasknum)
    ThpS = tasks
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
                        # # 原版
                        # flagst = 1
                        # for fgn in range(0, lenFg):
                        #     if ntuple[1] == FGtemp[i][fgn][1]:
                        #         # flagst = 0
                        #         if rt > FGtemp[i][fgn][0]:
                        #             FGtemp[i][fgn][0] = rt
                        #     else:
                        #         ntuple2 = FGtemp[i][fgn]
                        #         flagst -= whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV)
                        #         if (flagst == 0):
                        #             FGtemp[i][fgn] = ntuple
                        #             break
                        #         flagst -= whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV)
                        #         if (flagst == 0):
                        #             break

                        # 修改版
                        flagst = 1
                        for fgn in range(0, lenFg):
                            if ntuple[1] == FGtemp[i][fgn][1]:
                                # flagst = 0
                                if rt > FGtemp[i][fgn][0]:
                                    # FGtemp[i][fgn] = ntuple
                                    ntuple2 = FGtemp[i][fgn]
                                    flagst -= whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV)
                                    if (flagst == 0):
                                        FGtemp[i][fgn] = ntuple
                                        break
                                else:
                                    ntuple2 = FGtemp[i][fgn]
                                    flagst -= whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV)
                                    if (flagst == 0):
                                        break
                                    else:
                                        flagst = 1

                        if flagst == 1:
                            FGtemp[i].append(ntuple)

    t1 = time.time()
    TIME = t1 - t0
    # print(f"dag_new的ntuple的time:{TIME}")
    # print("####################dag_new1#######################")
                # if ntuple not in FGtemp[i]:
                #      FGtemp[i].append
    lenth_ntuple = len(FGtemp[lenV -1])

    t2 = time.time()

    if rt == 0:
        RT_f = 0
    else:
        rtv = []
        mart = 0
        # print ("the number of all tuple is",len(FGtemp[i]))
        for k in FGtemp[lenV - 1]:
            # print("**************************************")
            # print(k)
            # print("**************************************")
            if (flag):
                rtv.append(k[0])
            else:
                rthigh = 0  # 当前路径的高优先级任务计算结果
                x = k[3]
                y = 0
                while (x != y and x <= D_k):
                    # if x>D:break
                    y = x
                    # print("x=%d" % (x))
                    total = 0
                    for c in range(len(Ms)):
                        if (k[1][c] != -1):
                            # index_s=Type.index(s)
                            M_s = Ms[c]  # 当前类型核的个数
                            RT_s = Reshigh  # 高优先级任务响应时间
                            TmpSet_s = tasks  # 高优先级任务集
                            # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s,
                                                                       y) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    x = total + k[0]
                    # x = total + ck + intra
                    rthigh = x
                    # print("x=%d" % (x))
                if x != y:
                    return [0, lenth_ntuple]
                # print ("k[0]=",k[0])
                else:
                    rtv.append(rthigh)
                # print(rthigh-k[0])
        if len(rtv) != 0:
            mart = max(rtv)
        # print("mart=", mart)
        RT_f = mart
        if (RT_f > D_k):
            RT_f = 0
    t3 = time.time()
    TIME1 = t3 - t2
    # print(f"dag_new的RT的time:{TIME1}")
    # print("####################dag_new1#######################")
    return [RT_f, lenth_ntuple]







# basic的ntuple全加进去
def dag_new4(task, tasknum, tasks, Ms, types, Reshigh, flag):
    # print("###############",tasknum)
    ThpS = tasks
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

                    FGtemp[i].append(ntuple)

    t1 = time.time()
    TIME = t1 - t0
    # print(f"dag_new1 的ntuple的time:{TIME}")
    # print("####################dag_new1#######################")
                # if ntuple not in FGtemp[i]:
                #      FGtemp[i].append
    lenth_ntuple = len(FGtemp[lenV -1])

    t2 = time.time()

    if rt == 0:
        RT_f = 0
    else:
        rtv = []
        mart = 0
        # print ("the number of all tuple is",len(FGtemp[i]))
        for k in FGtemp[lenV - 1]:
            # print("**************************************")
            # print(k)
            # print("**************************************")
            if (flag):
                rtv.append(k[0])
            else:
                rthigh = 0  # 当前路径的高优先级任务计算结果
                x = k[3]
                y = 0
                while (x != y and x <= D_k):
                    # if x>D:break
                    y = x
                    # print("x=%d" % (x))
                    total = 0
                    for c in range(len(Ms)):
                        if (k[1][c] != -1):
                            # index_s=Type.index(s)
                            M_s = Ms[c]  # 当前类型核的个数
                            RT_s = Reshigh  # 高优先级任务响应时间
                            TmpSet_s = tasks  # 高优先级任务集
                            # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s,
                                                                       y) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    x = total + k[0]
                    # x = total + ck + intra
                    rthigh = x
                    # print("x=%d" % (x))
                if x != y:
                    return [0, lenth_ntuple]
                # print ("k[0]=",k[0])
                else:
                    rtv.append(rthigh)
                # print(rthigh-k[0])
        if len(rtv) != 0:
            mart = max(rtv)
        # print("mart=", mart)
        RT_f = mart
        if (RT_f > D_k):
            RT_f = 0
    t3 = time.time()
    TIME1 = t3 - t2
    # print(f"dag_new1 的RT的time:{TIME1}")
    # print("####################dag_new1#######################")
    return [RT_f, lenth_ntuple]



# 2.17 去除低优先级---globaledf
def dag_new1(task, Ms):
    # print("###############",tasknum)
    # ThpS=tasks
    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k = task.Di
    RT = []
    Tsets = []
    ty_num = len(Ms)
    rt = 0
    flag = 0

    ###################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    chV = randomDAG.findpcoDAG().find_child(task.V, task.E)

    paraV = randomDAG.findpcoDAG().find_parallel(task.V, task.E, task.P)

    lenV = len(task.V)

    E = task.E

    FGtemp = [[] * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV = find_pre_neighbor(task)

    for i in range(lenV):
        # print ("calculating vertex ",i)
        # first vertex
        if i == 0:
            ty_i = task.P[i] - 1
            # if it is a source node
            rtlen = task.V[i]
            # rtlow = types[ty_i][0]/Ms[ty_i]
            # 2.17去除低优先级
            # rtlow=0
            sumc = rtlen
            #  print("rtlen=",rtlen)
            #  print("rtlow=",rtlow)
            # 2.17去除低优先级
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
            FGtemp[i] = [[rt, nn_set, pretype_i, sumc]]  # 依次是（len+inter）、（类型集合）、（前驱节点编号，rt中加入该点值后更新）
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
                    # 2.17去除低优先级
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
                        flagst = 1
                        for fgn in range(0, lenFg):
                            if ntuple[1] == FGtemp[i][fgn][1]:
                                flagst = 0
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

                        if flagst == 1:
                            FGtemp[i].append(ntuple)

    return FGtemp


# # 深度遍历
# def dfs(task,start_node,current_node,end_node,path,path_type,sumc,paths,paths_type,sumcs):
def dfs(task, start_node, current_node, end_node, path, sumc, paths, sumcs):
    #  将当前点的信息加入到path等
    path.append(current_node)
    sumc += task.V[current_node]
    # path_type[current_node] = task.P[current_node] - 1

    # 当前的点是最终点
    if current_node == end_node:
        paths.append(path.copy())
        # for i in range(len(paths)):
        #     for item in path:
        #         path_type[item] = task.P[item] - 1

        # paths_type.append(path_type)
        sumcs.append(sumc)
        # 开始回溯
        path.pop()
        # sumc -=task.V[current_node]
        # path_type[current_node] = -1
    else:
        for parent in task.preV[current_node]:
            if parent not in path:
                # dfs(task,start_node,parent,end_node,path, path_type, sumc, paths, paths_type, sumcs)
                dfs(task, start_node, parent, end_node, path, sumc, paths, sumcs)
        path.pop()
        # sumc -= task.V[current_node]
        # path_type[current_node] = -1

        # return paths, paths_type, sumcs
        return paths, sumcs


def get_path_info(task, start_node, end_node):
    """
    获取从起始节点到结束节点的路径信息。
    参数：
    - task：包含顶点、边、类型和其他参数信息的DAG任务对象。
    - start_node：路径的起始节点编号。
    - end_node：路径的结束节点编号。
    返回：
    - path_info：包含从起始节点到结束节点的路径信息的列表。
    - type_info: 包含从起始节点到结束节点的路径上每个节点的类型信息的列表。
    - SUMC：路径的和。
    """
    # 初始化访问标记列表
    visited = [False] * len(task.V)
    # 初始化路径信息
    path = []

    paths = []
    # 初始化类型信息
    type_info = [-1] * len(task.V)
    # 初始化路径和
    SUMC = 0
    # task.preV = randomDAG.findpcoDAG().find_ancestors(task.V, task.E)
    # 使用深度优先搜索找到路径
    task.preV = find_pre(task)

    paths_type = []

    sumcs = []
    if start_node != end_node:
        paths, sumcs = dfs(task, end_node, end_node, start_node, path, SUMC, paths, sumcs)
        # paths, paths_type, sumcs = dfs(task, end_node, end_node, start_node, path, type_info, SUMC, paths, paths_type,
        #                                sumcs)
        # 若找到路径，则将其反转以获得从起始节点到结束节点的路径
        for i in range(len(paths)):
            paths[i].reverse()
            # 初始化类型信息
            type_info1 = [-1] * len(task.V)
            for item in paths[i]:
                type_info1[item] = task.P[item] - 1

            paths_type.append(type_info1)

        return paths, paths_type, sumcs
    else:

        type_info[start_node] = task.P[start_node] - 1
        SUMC += task.V[start_node]

        return start_node, type_info, SUMC


# gobal-fp版，初始值是rt+当前路径中的类型对应的 V(C)/Ms累计和
def dag_new3(task, tasknum, tasks, Ms, types, Reshigh, flag):
    # print("###############",tasknum)
    ThpS = tasks
    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k = task.Di
    RT = []
    Tsets = []
    ty_num = len(Ms)
    rt = 0

    ###################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    chV = randomDAG.findpcoDAG().find_child(task.V, task.E)

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
            path = [i]
            rt = rtlen

            nn_set = []
            for j in range(len(Ms)):
                nn_set.append(-1)
            # print(rtlen,rtlow)
            # nearest type s
            # nn_set[ty_i] = i
            # tuple?
            pretype_i = -1  # 路径下一个节点到来时，它的前驱的类型，也就是当前加入的这个点。
            FGtemp[i] = [[rt, nn_set, pretype_i, sumc, path]]  # 依次是（len+inter+低优先级）、（类型集合）、（前驱节点编号，rt中加入该点值后更新）
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

                    path = k[-1] + [i]

                    ntuple = [rt, tmset, cori, sumc, path]
                    lenFg = len(FGtemp[i])
                    if lenFg == 0:
                        FGtemp[i].append(ntuple)
                    else:

                        # 正常删减版9.11
                        flagst = 1
                        for fgn in range(0, lenFg):
                            ntuple2 = FGtemp[i][fgn]
                            if ntuple == ntuple2:
                                flagst = 0
                                break
                            else:
                                flagst = 1
                                # if flagst == 0:
                                #     break
                        if flagst == 1:
                            FGtemp[i].append(ntuple)


                        # # 参考论文修改版
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
                        #
                        # if flagst == 1:
                        #     FGtemp[i].append(ntuple)


    t1 = time.time()
    TIME = t1 - t0
    # print(f"dag_new3 的ntuple的time:{TIME}")
    # print("####################dag_new3#######################")
    lenth_ntuple = len(FGtemp[lenV-1])

    t2 = time.time()
    if rt == 0:
        RT_f = 0
    else:
        rtv = []
        mart = 0
        rt_flag = True
        last_rt = 0
        # print ("the number of all tuple is",len(FGtemp[i]))
        for k in FGtemp[lenV - 1]:
            # print(k)
            if (flag):
                rtv.append(k[0])
            else:
                # 当前路径的高优先级任务计算结果
                # 第一次执行时
                if (rt_flag == True):
                    rthigh = 0
                    # 求出当前的路径上点的类型及不同类型的个数
                    arrtype = [0] * len(k[4])
                    for i in range(len(k[4])):
                        arrtype[i] = task.P[k[4][i]] - 1
                    settype = set(arrtype)
                    x = 0
                    # 将type_initrt的长度设置成nump的长度，
                    # 存储时，用type_initrt[i]来存储对应i类型的初始化长度
                    typeset_initrt = [0]*100
                    for i in settype:
                        x = x + sum_from_first_to_last_type1(i,arrtype,k,task)
                        typeset_initrt[i] = sum_from_first_to_last_type1(i,arrtype,k,task)
                    # print("当前的任务的typeset_initrt=",typeset_initrt)
                    # 2024.7.31修改
                    # y = 0
                    # while (x != y and x <= D_k):
                    #     # if x>D:break
                    #     y = x
                    #     # print("x=%d" % (x))
                    #     total = 0
                    #     for c in range(len(Ms)):
                    #         if (k[1][c] != -1):
                    #             # index_s=Type.index(s)
                    #             M_s = Ms[c]  # 当前类型核的个数
                    #             RT_s = Reshigh  # 高优先级任务响应时间
                    #             TmpSet_s = tasks  # 高优先级任务集
                    #             # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    #             total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, typeset_initrt[
                    #                 c]) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    #     x = total + k[0]
                    #     # x = total + ck + intra
                    #     rthigh = x
                    #     # print("x=%d" % (x))

                    total = 0
                    for c in range(len(Ms)):
                        if (k[1][c] != -1):
                            # index_s=Type.index(s)
                            M_s = Ms[c]  # 当前类型核的个数
                            RT_s = Reshigh  # 高优先级任务响应时间
                            TmpSet_s = tasks  # 高优先级任务集
                            # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, typeset_initrt[c]) / M_s) # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            # print(total)
                    x = total + k[0]
                    # x = total + ck + intra
                    rthigh = x
                    # 修改7.29 22：00
                    rtv.append(rthigh)
                    rt_flag = False
                    last_rt = rthigh

                    # print(rthigh-k[0])
                else:
                    rthigh = 0
                    x = last_rt
                    y = 0
                    while (x != y and x <= D_k):
                        # if x>D:break
                        y = x
                        # print("x=%d" % (x))
                        total = 0
                        for c in range(len(Ms)):
                            if (k[1][c] != -1):
                                # index_s=Type.index(s)
                                M_s = Ms[c]  # 当前类型核的个数
                                RT_s = Reshigh  # 高优先级任务响应时间
                                TmpSet_s = tasks  # 高优先级任务集
                                # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                                total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s,y) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                        x = total + k[0]
                        # x = total + ck + intra
                        rthigh = x
                        # print("x=%d" % (x))
                    if x != y:
                        return [0, lenth_ntuple]
                    else:
                        rtv.append(rthigh)
        if len(rtv) != 0:
            mart = max(rtv)
        # print("mart=", mart)
        RT_f = mart
        if (RT_f > D_k):
            RT_f = 0
    t3 = time.time()
    TIME1 = t3 - t2
    # print(f"dag_new3 的RT的time:{TIME}")
    # print("####################dag_new3#######################")
    return [RT_f,lenth_ntuple]


# gobal-fp版，初始值是rt+当前路径中的类型对应的 V(C)/Ms累计和，但是ntuple直接要添加版
def dag_new5(task, tasknum, tasks, Ms, types, Reshigh, flag):
    # print("###############",tasknum)
    ThpS = tasks
    # cp=ImpBL.findCriPath(DAG)
    # T_k=DAG.Ti
    D_k = task.Di
    RT = []
    Tsets = []
    ty_num = len(Ms)
    rt = 0

    ###################################EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    chV = randomDAG.findpcoDAG().find_child(task.V, task.E)

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
            path = [i]
            rt = rtlen

            nn_set = []
            for j in range(len(Ms)):
                nn_set.append(-1)
            # print(rtlen,rtlow)
            # nearest type s
            # nn_set[ty_i] = i
            # tuple?
            pretype_i = -1  # 路径下一个节点到来时，它的前驱的类型，也就是当前加入的这个点。
            FGtemp[i] = [[rt, nn_set, pretype_i, sumc, path]]  # 依次是（len+inter+低优先级）、（类型集合）、（前驱节点编号，rt中加入该点值后更新）
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

                    path = k[-1] + [i]

                    ntuple = [rt, tmset, cori, sumc, path]
                    lenFg = len(FGtemp[i])
                    if lenFg == 0:
                        FGtemp[i].append(ntuple)
                    else:

                        # flagst = 1
                        # for fgn in range(0, lenFg):
                        #     if ntuple[1] == FGtemp[i][fgn][1]:
                        #         flagst = 0
                        #         if rt > FGtemp[i][fgn][0]:
                        #             FGtemp[i][fgn][0] = rt
                        #     else:
                        #         ntuple2 = FGtemp[i][fgn]
                        #
                        #         flagst -= whether_to_switch_con(Ms, ntuple, ntuple2, paraV, chV)
                        #         if (flagst == 0):
                        #             FGtemp[i][fgn] = ntuple
                        #             break
                        #         flagst -= whether_to_delete_con(Ms, ntuple, ntuple2, paraV, chV)
                        #         if (flagst == 0):
                        #             break

                        flagst = 1
                        for fgn in range(0, lenFg):
                            ntuple2 = FGtemp[i][fgn]
                            if ntuple == ntuple2:
                                flagst = 0
                                break
                            else:
                                flagst = 1
                                # if flagst == 0:
                                #     break
                        if flagst == 1:
                            FGtemp[i].append(ntuple)
                # if ntuple not in FGtemp[i]:
                #      FGtemp[i].append(ntuple)

    t1 = time.time()
    TIME = t1 - t0
    # print(f"dag_new3 的ntuple的time:{TIME}")
    # print("####################dag_new3#######################")
    lenth_ntuple = len(FGtemp[lenV-1])

    t2 = time.time()
    if rt == 0:
        RT_f = 0
    else:
        rtv = []
        mart = 0
        rt_flag = True
        last_rt = 0
        # print ("the number of all tuple is",len(FGtemp[i]))
        for k in FGtemp[lenV - 1]:
            # print(k)
            if (flag):
                rtv.append(k[0])
            else:
                # 当前路径的高优先级任务计算结果
                # 第一次执行时
                if (rt_flag == True):
                    rthigh = 0
                    # 求出当前的路径上点的类型及不同类型的个数
                    arrtype = [0] * len(k[4])
                    for i in range(len(k[4])):
                        arrtype[i] = task.P[k[4][i]] - 1
                    settype = set(arrtype)
                    x = 0
                    # 将type_initrt的长度设置成nump的长度，
                    # 存储时，用type_initrt[i]来存储对应i类型的初始化长度
                    typeset_initrt = [0]*100
                    for i in settype:
                        x = x + sum_from_first_to_last_type1(i,arrtype,k,task)
                        typeset_initrt[i] = sum_from_first_to_last_type1(i,arrtype,k,task)
                    # print("当前的任务的typeset_initrt=",typeset_initrt)
                    # 2024.7.31修改
                    # y = 0
                    # while (x != y and x <= D_k):
                    #     # if x>D:break
                    #     y = x
                    #     # print("x=%d" % (x))
                    #     total = 0
                    #     for c in range(len(Ms)):
                    #         if (k[1][c] != -1):
                    #             # index_s=Type.index(s)
                    #             M_s = Ms[c]  # 当前类型核的个数
                    #             RT_s = Reshigh  # 高优先级任务响应时间
                    #             TmpSet_s = tasks  # 高优先级任务集
                    #             # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    #             total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, typeset_initrt[
                    #                 c]) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                    #     x = total + k[0]
                    #     # x = total + ck + intra
                    #     rthigh = x
                    #     # print("x=%d" % (x))

                    total = 0
                    for c in range(len(Ms)):
                        if (k[1][c] != -1):
                            # index_s=Type.index(s)
                            M_s = Ms[c]  # 当前类型核的个数
                            RT_s = Reshigh  # 高优先级任务响应时间
                            TmpSet_s = tasks  # 高优先级任务集
                            # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, typeset_initrt[c]) / M_s) # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                            # print(total)
                    x = total + k[0]
                    # x = total + ck + intra
                    rthigh = x
                    # 修改7.29 22：00
                    rtv.append(rthigh)
                    rt_flag = False
                    last_rt = rthigh

                    # print(rthigh-k[0])
                else:
                    rthigh = 0
                    x = last_rt
                    y = 0
                    while (x != y and x <= D_k):
                        # if x>D:break
                        y = x
                        # print("x=%d" % (x))
                        total = 0
                        for c in range(len(Ms)):
                            if (k[1][c] != -1):
                                # index_s=Type.index(s)
                                M_s = Ms[c]  # 当前类型核的个数
                                RT_s = Reshigh  # 高优先级任务响应时间
                                TmpSet_s = tasks  # 高优先级任务集
                                # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                                total += math.floor(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s,y) / M_s)  # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级）
                        x = total + k[0]
                        # x = total + ck + intra
                        rthigh = x
                        # print("x=%d" % (x))
                    if x != y:
                        return [0, lenth_ntuple]
                    else:
                        rtv.append(rthigh)
        if len(rtv) != 0:
            mart = max(rtv)
        # print("mart=", mart)
        RT_f = mart
        if (RT_f > D_k):
            RT_f = 0
    t3 = time.time()
    TIME1 = t3 - t2
    # print(f"dag_new3 的RT的time:{TIME}")
    # print("####################dag_new3#######################")
    return [RT_f,lenth_ntuple]


# 找到当前路径上type1节点类型的RT长度
def sum_from_first_to_last_type1(type1, arr1, k ,task):
    total_sum = 0
    first_flag = False
    first_index = 0
    last_index = 0

    # 寻找type1的第一个和最后一个出现位置
    for i, val in enumerate(arr1):
        if val == type1:
            if first_flag == False:
                first_index = i
                first_flag = True
            last_index = i

    # 如果找到了type1，则累加指定区间内的元素值
    if first_flag == True:
        lastnumber = last_index + 1
        for i in range(first_index , lastnumber):
            total_sum = total_sum + task.V[k[4][i]]

        return total_sum


    # elif last_index != 0:
    #     # 如果后一个type1没有出现在数组中，返回
    #     return task.V[k[4][last_index]]
    # else:
    #     return 0


# 高优先级任务集合除了本身以外的所有任务集合
def hightask(task, tsets):
    """

    :param task: 当前所在的任务
    :param tsets: 所有的任务集合
    :return: 高优先任务集合(除了当前任务本身的其他所有任务)
    """
    # 高优先级任务集合除了本身以外的所有任务集合
    tasksss = []
    task_index = tsets.index(task)
    for task in tsets:
        if tsets.index(task) != task_index:
            tasksss.append(task)

    return tasksss


# 求高优先级任务集合对应的RT（高优先集合除了本任务的所有集合）
def hightask_rt(task_index, RTset):
    '''
    :param task_index: 当前任务的序号
    :param RTset: 已经计算的的RT
    :return: 高优先级任务集合对应的RT（高优先集合除了本任务的所有集合）
    '''
    hightask_rtime = []

    for i in range(len(RTset)):
        if i != task_index:
            hightask_rtime.append(RTset[i])

    return hightask_rtime


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


# 判断while循环是否继续的条件
def checkone(arr):
    for element in arr:
        if element == 0:
            return False
    return True


def globaledf(tsets, Ms):
    t0 = time.time()
    RTset = []
    # 存取task的高任务优先集
    tasksss = []
    # 当前路径的高优先级任务计算结果
    rthigh = 0

    # MaxR_len = [list() for i in range(len(tsets))]
    MaxR_len = [0] * len(tsets)

    TIME = 0

    # print(tsets)

    # print(tsets[0].Di)

    # 初始化RTset数组让其的值等于tsets[i]的di
    # for task in tsets:
    #     task_index4 = tsets.index(task)
    #     RTset[task_index4] = task.Di
    for t in range(len(tsets)):
        # print(t)
        RTset.append(tsets[t].Di)

    # 初始化flag_up数组令其里面都等于1
    # flag_up = np.ones((1, len(RTset)))
    flag_up = [1] * len(RTset)
    RT_K = [0] * len(tsets)

    # 当数组flag_up里存在1就执行
    while (checkone(flag_up)):

        for task in tsets:

            # 当前任务的序号
            task_index = tsets.index(task)

            # 取出在dag_new里面的tuple用于下一步计算。
            task_tuple = dag_new1(task, Ms)

            # 当前任务的RTset等于任务的DI执行，即第一次访问
            if RTset[task_index] == task.Di:

                max_len = 0

                lenV = len(task.V)

                # task_tuple = dag_new(task,Ms)
                max = 0

                # # tuple需要在while循环里求出最大的K[0] K[3]
                # # 遍历所有的tuple,求导致最大R的路径信息

                # 获取高优先任务集合
                tasksss = hightask(task, tsets)

                # Reshigh  高优先级任务响应时间： 对应的RTset里的值
                Reshigh = hightask_rt(task_index, RTset)

                # tuple需要在while循环里求出最大的K[0] K[3]
                # 遍历所有的tuple,求导致最大R的路径信息
                for k in task_tuple[lenV - 1]:
                    # 当前路径的高优先级任务计算结果
                    rthigh = 0
                    x = k[3]
                    y = 0
                    while x != y:
                        # if x>D:break
                        y = x
                        # print("x=%d" % (x))
                        total = 0
                        for c in range(len(Ms)):
                            if k[1][c] != -1:
                                # index_s=Type.index(s)
                                D_k = task.Di
                                M_s = Ms[c]  # 当前类型核的个数
                                RT_s = Reshigh  # 高优先级任务响应时间
                                TmpSet_s = tasksss  # 高优先级任务集
                                # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级），D_k=task.Di
                                total += math.floor(min(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, y),
                                                        highprio_path.totalInt2(c, M_s, TmpSet_s, RT_s, D_k))
                                                    / M_s)
                        x = total + k[0]

                        rthigh = x
                        # x = total + ck + intra
                    RTset[task_index] = rthigh

                    # print(k[3])
                    if RTset[task_index] > max_len:
                        max_len = RTset[task_index]
                        MaxR_len[task_index] = k[3]
                        RT_K[task_index] = k[0]

                # 当for循环结束时，更新最大R

                RTset[task_index] = max_len

            # 在RTset[task_index] != task.DI时

            else:

                # task_tuple = dag_new(task, Ms)

                lenV = len(task.V)

                # 获取高优先任务集合
                tasksss = hightask(task, tsets)

                # Reshigh  高优先级任务响应时间： 对应的RTset里的值
                Reshigh = hightask_rt(task_index, RTset)

                for k in task_tuple[lenV - 1]:
                    # 当前路径的高优先级任务计算结果

                    rthigh = 0
                    x = MaxR_len[task_index]

                    y = 0

                    # print(task_index)
                    while x != y:
                        # if x>D:break
                        y = x
                        # print("x=%d" % (x))
                        total = 0
                        for c in range(len(Ms)):
                            if k[1][c] != -1:
                                D_k = task.Di
                                # index_s=Type.index(s)
                                M_s = Ms[c]  # 当前类型核的个数
                                RT_s = Reshigh  # 高优先级任务响应时间
                                TmpSet_s = tasksss  # 高优先级任务集
                                # c为当前遍历到的核类型下表， y就是加入高优先级任务后本次迭代前的区间长度，K[0]是任务本身的占用时间（运行+内部+低优先级），D_k=task.Di
                                total += math.floor(min(highprio_path.TotalInt(c, M_s, TmpSet_s, RT_s, y),
                                                        highprio_path.totalInt2(c, M_s, TmpSet_s, RT_s, D_k))
                                                    / M_s)

                        x = total + RT_K[task_index]
                        # x = total + ck + intra
                        rthigh = x

                # 如果当前的任务的rt不在变换，将标志位改成0
                if RTset[task_index] == rthigh:
                    # 结束当前循环，更改标志位  1 -> 0
                    flag_up[task_index] = 0
                    # print("当前的flag_up", flag_up)


                elif RTset[task_index] != rthigh:

                    RTset[task_index] = rthigh

    # 假若在RTset 的数组里存在RTset[i]>D_K(大于截止期)，则就不调度，返回0
    for task in tsets:
        # 任务的序号是task_index2
        task_index2 = tsets.index(task)
        if RTset[task_index2] > task.Di:
            RTset[task_index2] = 0
    t1 = time.time()
    TIME = t1 - t0

    # print("最后结果的RTset是：", RTset)
    # print("当前运行花费的时间是：", TIME)

    return [RTset, TIME]



if __name__ == '__main__':
# 初始参数设置
    tasknum = 20
    Umin = 8
    Umax = 8
    Tmin = 100     #100
    Tmax = 1000    #1000
    Ndagmin = 50
    Ndagmax = 50
    Msmin = 15
    Msmax = 15
    Pr = 0.9
    numP = 5       #15

    U = sepU(tasknum, Umin, Umax)
    # print(U)

    MS = Experiment_rt_Sun_path.devide_cores_dags(numP, Msmin, Msmax)  # 核数安排，即每个分类要安排几个内核（不限制内核编号）
    tmin = Tmin  # 随机生成dag的最小周期
    task = []
    for s in range(0, tasknum):  # 生成dag任务集
        T = randomDAG.generate_DAG(Ndagmin, Ndagmax, tmin, Tmax, Pr, numP)
        # u=random.uniform(Umin,Umax)
        # print(U[s])
        task.append(T.generate_DAG_task(U[s]))
        # print(task[s].Ti)
        tmin = task[s].Ti
    # # 修改为指定任务参数
    # modV = [[0, 12.430931859708892, 16.181670732249188, 8.694577401804068, 3.9961353361173018, 8.79573503290852,
    #          18.767622809592314, 1.343887429107384, 19.713881278500764, 0.6043082518554046, 34.5229195366496,
    #          13.003409650850603, 2.0396100354130047, 58.376047150310335, 5.090306631495025, 3.372290196770921, 0],
    #         [0, 87.1843880351318, 20.872076686226734, 1.646338053334297, 10.988641111201602, 16.02696582375964,
    #          2.6711099951355735, 28.11401161540074, 1.0624846166025748, 17.072144387319398, 54.16933248709809,
    #          5.026370469782848, 91.82780394890841, 4.798059691739887, 67.70618962058991, 40.434083457768494, 0],
    #         [0, 24.543292498339554, 6.8251250729639, 11.520366003861, 25.728617192819996, 29.344574317391505,
    #          112.91614341845997, 112.55239301016897, 12.988760526599734, 57.03333906743581, 18.055260428401688,
    #          0.27245291180260023, 28.927385238280607, 34.14772705137094, 21.338552207856118, 35.006011054247544, 0],
    #         [0, 12.893507836628388, 10.170445447802052, 166.3261912782343, 29.49934419633486, 64.1997649252722,
    #          5.0291422921778235, 43.44610026265196, 3.936375215275723, 2.001720491183398, 46.55565714555025,
    #          2.6354159395677055, 11.279177141138712, 14.135256048454181, 3.682666152238383, 115.40923562749005, 0],
    #         [0, 10.995469182979612, 21.94301610342771, 45.89808444674122, 36.33776281817812, 44.135841415522435,
    #          7.08337948132581, 25.18969453125294, 56.61071298954892, 2.0415969876137847, 48.880464294842184,
    #          0.25749052304718134, 7.0400110378586245, 10.957615258644724, 195.99151532912742, 17.83734559988923, 0],
    #         [0, 4.225075513621533, 2.779740123415607, 10.148560388611571, 45.49583339713463, 258.21837060375157,
    #          34.99702153835091, 37.80933218669255, 4.7291541350096225, 3.627289761113971, 43.02575834084414,
    #          18.644792004822268, 15.145480703547854, 24.762707632218813, 7.837346272033878, 21.88687073216439, 0],
    #         [0, 121.66450874501865, 31.967538693878765, 22.7401848462259, 14.255265045633436, 85.2610348525729,
    #          1.0668386304458792, 6.840777979974085, 0.5313270514060946, 18.800382935242464, 61.924757390484906,
    #          8.40536754806173, 29.78805184462603, 2.943941875865334, 124.14648906481484, 2.9968668290822786, 0],
    #         [0, 31.122420001175836, 43.32387136481978, 0.3207413000952677, 5.607626350343756, 38.45803424324026,
    #          92.64249403394783, 176.6304567116191, 1.141403166476934, 6.320189583831138, 1.7645042885268225,
    #          4.24971457564351, 19.751215859477128, 57.32593342395818, 5.108710080596272, 49.566018349581505, 0],
    #         [0, 36.65873406927966, 3.0499558709347525, 16.068645726895284, 18.00393658433893, 63.55921760400827,
    #          4.299131256983721, 98.33140430670831, 3.8422151249771233, 61.35562913743303, 50.71665412094596,
    #          42.48315761423926, 20.560355826701016, 13.008267820314629, 61.54496427892994, 39.85106399064341, 0],
    #         [0, 17.08686471284569, 1.9662712180214008, 296.2596404495787, 0.8926719450962146, 0.5428152656838918,
    #          0.19070963772058036, 93.34124407873878, 25.5100354358053, 4.455901612606825, 11.12485702945894,
    #          0.19541177675604438, 11.618497117433385, 16.844865793675936, 49.246980794141415, 4.056566465770263, 0],
    #         [0, 19.850327338471544, 70.0396481274903, 44.562130445915756, 17.05548239459992, 17.922176497888003,
    #          108.29772302219027, 26.4569543822238, 9.645154104593772, 38.51576638178262, 18.638295798718502,
    #          24.671465667642323, 36.8410818568059, 15.278256601725058, 25.950163155751444, 59.608707557534146, 0],
    #         [0, 7.498987665227588, 32.42536213535672, 18.16686852079357, 50.406808680073084, 19.65259307867751,
    #          60.837153363052664, 32.91902613569545, 76.19879481420122, 18.64552305946458, 175.78543727932671,
    #          13.357490538896023, 0.12643026892776277, 0.8632296832194628, 16.119416819014997, 10.330211291405996, 0],
    #         [0, 2.7555355991922, 23.5736489141147, 17.451466974039903, 36.80515373003564, 19.300365635588605,
    #          22.342653125818217, 4.566090315532016, 68.66340747239997, 59.13718742610082, 168.81377329113377,
    #          43.44899962214271, 11.406603155937882, 45.31823223884715, 1.5835447934225098, 8.166671039027255, 0],
    #         [0, 39.367822419015084, 30.352493305696356, 36.76697189951031, 23.788397179191804, 53.19818930070801,
    #          45.80995362637201, 14.092117008686458, 0.5300736854270269, 108.76231156390081, 86.18880057830786,
    #          9.956839869574674, 33.663445415191596, 13.660529313233555, 36.47138431367309, 0.7240038548446649, 0],
    #         [0, 7.991010830051135, 7.0135259257665865, 3.5657553527944685, 307.40358123898073, 0.47067853010029737,
    #          84.06952821648702, 6.570465071539136, 54.91922744670431, 17.999246099120906, 5.677335493691517,
    #          2.7284210186311775, 24.171242246753803, 4.8158887167851505, 2.632814728265832, 3.3046124176612266, 0]]
    # modE = [[(0, 1), (0, 2), (0, 4), (0, 5), (0, 8), (0, 10), (0, 11), (0, 13), (1, 6), (2, 3), (2, 7), (3, 14), (4, 12),
    #          (5, 16), (6, 16), (7, 9), (7, 12), (8, 16), (9, 16), (10, 15), (11, 15), (12, 16), (13, 14), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 5), (0, 8), (0, 9), (0, 12), (0, 14), (1, 4), (1, 7), (2, 7), (3, 16), (4, 16),
    #          (5, 6), (5, 13), (6, 15), (7, 16), (8, 16), (9, 10), (10, 11), (11, 15), (12, 13), (13, 16), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (0, 11), (1, 10), (2, 9), (2, 15), (3, 6), (4, 15),
    #          (5, 16), (6, 16), (7, 14), (8, 13), (8, 15), (9, 16), (10, 16), (11, 12), (12, 15), (13, 16), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 2), (0, 5), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 3), (1, 4), (1, 6), (2, 16), (3, 13),
    #          (4, 15), (5, 16), (6, 14), (7, 16), (8, 16), (9, 12), (10, 13), (11, 16), (12, 13), (13, 14), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 3), (0, 4), (0, 5), (0, 6), (0, 8), (0, 10), (0, 11), (0, 12), (1, 2), (2, 9), (2, 13), (3, 7),
    #          (3, 14), (4, 16), (5, 16), (6, 15), (7, 15), (8, 16), (9, 13), (10, 16), (11, 13), (12, 16), (13, 15),
    #          (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 6), (0, 7), (0, 8), (0, 10), (1, 16), (2, 5), (2, 11), (3, 12), (4, 9),
    #          (4, 12), (5, 16), (6, 12), (6, 14), (7, 16), (8, 16), (9, 13), (10, 15), (11, 16), (12, 16), (13, 14),
    #          (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (0, 11), (0, 13), (1, 6), (2, 6), (3, 9), (3, 14),
    #          (4, 16), (5, 16), (6, 9), (6, 12), (7, 14), (7, 15), (8, 12), (9, 10), (10, 16), (11, 16), (12, 16), (13, 16),
    #          (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 8), (0, 11), (1, 9), (2, 16), (3, 6), (3, 7), (3, 10), (3, 13),
    #          (4, 16), (5, 16), (6, 7), (6, 15), (7, 16), (8, 13), (8, 14), (9, 16), (10, 12), (11, 16), (12, 16), (13, 16),
    #          (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (0, 11), (1, 6), (2, 6), (3, 13), (4, 9), (5, 10),
    #          (5, 14), (6, 16), (7, 12), (7, 15), (8, 16), (9, 12), (9, 14), (10, 16), (11, 16), (12, 16), (13, 16),
    #          (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 10), (0, 13), (1, 14), (2, 16), (3, 8), (4, 8),
    #          (5, 8), (6, 9), (6, 11), (6, 12), (7, 8), (8, 16), (9, 16), (10, 16), (11, 16), (12, 14), (13, 16), (14, 15),
    #          (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 10), (0, 11), (1, 9), (1, 15), (2, 13),
    #          (3, 16), (4, 13), (5, 16), (6, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 16), (11, 12), (11, 13), (12, 16),
    #          (13, 16), (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 8), (0, 10), (1, 7), (2, 12), (2, 13), (3, 14), (4, 12),
    #          (5, 9), (6, 16), (7, 12), (7, 15), (8, 11), (9, 16), (10, 16), (11, 13), (12, 16), (13, 16), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 10), (0, 11), (0, 15), (1, 13), (2, 7), (2, 8), (2, 12),
    #          (3, 7), (4, 14), (5, 7), (5, 9), (5, 12), (6, 16), (7, 12), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16),
    #          (13, 16), (14, 16), (15, 16)],
    #         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (0, 10), (0, 15), (1, 6), (2, 11), (3, 13), (4, 14),
    #          (5, 16), (6, 13), (7, 11), (7, 13), (8, 9), (9, 12), (9, 13), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16),
    #          (15, 16)],
    #         [(0, 1), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 2), (2, 13), (3, 9), (4, 14), (5, 16), (6, 13),
    #          (7, 16), (8, 10), (9, 11), (10, 12), (11, 13), (12, 16), (13, 16), (14, 15), (15, 16)]]
    # modT = [388, 843, 996, 996, 996, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    # modP = [[1, 2, 2, 3, 2, 2, 1, 2, 3, 2, 3, 1, 2, 3, 1, 2, 2], [1, 1, 1, 2, 1, 3, 2, 1, 3, 1, 2, 2, 3, 3, 1, 3, 1],
    #         [2, 2, 3, 2, 3, 3, 2, 2, 3, 2, 3, 2, 1, 1, 3, 1, 1], [1, 3, 1, 1, 3, 2, 3, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2],
    #         [3, 3, 2, 1, 3, 1, 3, 1, 2, 3, 2, 1, 2, 3, 1, 1, 2], [2, 1, 1, 2, 2, 3, 1, 2, 1, 3, 1, 3, 2, 2, 2, 1, 1],
    #         [3, 3, 1, 1, 1, 3, 1, 1, 1, 1, 2, 2, 1, 2, 3, 2, 2], [1, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 2, 3, 1, 3, 1, 2],
    #         [3, 2, 3, 2, 2, 2, 1, 2, 1, 3, 2, 3, 1, 3, 3, 2, 2], [2, 3, 2, 1, 2, 3, 3, 1, 3, 2, 2, 2, 1, 3, 1, 2, 1],
    #         [1, 2, 1, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 3], [3, 2, 1, 2, 1, 1, 2, 3, 3, 3, 3, 2, 3, 1, 2, 3, 2],
    #         [2, 1, 3, 2, 2, 3, 1, 1, 3, 3, 2, 1, 1, 2, 3, 3, 1], [3, 2, 1, 1, 2, 2, 2, 1, 3, 3, 1, 1, 3, 2, 3, 2, 3],
    #         [1, 3, 2, 2, 1, 3, 2, 3, 1, 1, 3, 3, 2, 2, 3, 3, 1]]
    # typeddag = [[[18.767622809592314, 13.003409650850603, 5.090306631495025],
    #              [16.181670732249188, 12.430931859708892, 8.79573503290852, 3.9961353361173018, 3.372290196770921,
    #               2.0396100354130047, 1.343887429107384, 0.6043082518554046],
    #              [58.376047150310335, 34.5229195366496, 19.713881278500764, 8.694577401804068]], [
    #                 [87.1843880351318, 67.70618962058991, 28.11401161540074, 20.872076686226734, 17.072144387319398,
    #                  10.988641111201602], [54.16933248709809, 5.026370469782848, 2.6711099951355735, 1.646338053334297],
    #                 [91.82780394890841, 40.434083457768494, 16.02696582375964, 4.798059691739887, 1.0624846166025748]],
    #             [[35.006011054247544, 34.14772705137094, 28.927385238280607],
    #              [112.91614341845997, 112.55239301016897, 57.03333906743581, 24.543292498339554, 11.520366003861,
    #               0.27245291180260023],
    #              [29.344574317391505, 25.728617192819996, 21.338552207856118, 18.055260428401688, 12.988760526599734,
    #               6.8251250729639]],
    #             [[166.3261912782343, 43.44610026265196, 10.170445447802052, 3.936375215275723, 2.001720491183398],
    #              [115.40923562749005, 64.1997649252722, 14.135256048454181, 3.682666152238383],
    #              [46.55565714555025, 29.49934419633486, 12.893507836628388, 11.279177141138712, 5.0291422921778235,
    #               2.6354159395677055]], [
    #                 [195.99151532912742, 45.89808444674122, 44.135841415522435, 25.18969453125294, 17.83734559988923,
    #                  0.25749052304718134], [56.61071298954892, 48.880464294842184, 21.94301610342771, 7.0400110378586245],
    #                 [36.33776281817812, 10.995469182979612, 10.957615258644724, 7.08337948132581, 2.0415969876137847]], [
    #                 [43.02575834084414, 34.99702153835091, 21.88687073216439, 4.7291541350096225, 4.225075513621533,
    #                  2.779740123415607],
    #                 [45.49583339713463, 37.80933218669255, 24.762707632218813, 15.145480703547854, 10.148560388611571,
    #                  7.837346272033878], [258.21837060375157, 18.644792004822268, 3.627289761113971]], [
    #                 [31.967538693878765, 29.78805184462603, 22.7401848462259, 18.800382935242464, 14.255265045633436,
    #                  6.840777979974085, 1.0668386304458792, 0.5313270514060946],
    #                 [61.924757390484906, 8.40536754806173, 2.9968668290822786, 2.943941875865334],
    #                 [124.14648906481484, 121.66450874501865, 85.2610348525729]],
    #             [[92.64249403394783, 57.32593342395818, 49.566018349581505],
    #              [31.122420001175836, 6.320189583831138, 5.607626350343756, 4.24971457564351, 1.7645042885268225,
    #               1.141403166476934, 0.3207413000952677],
    #              [176.6304567116191, 43.32387136481978, 38.45803424324026, 19.751215859477128, 5.108710080596272]],
    #             [[63.55921760400827, 20.560355826701016, 4.299131256983721, 3.8422151249771233],
    #              [98.33140430670831, 63.55921760400827, 50.71665412094596, 39.85106399064341, 36.65873406927966,
    #               18.00393658433893, 16.068645726895284],
    #              [61.54496427892994, 61.35562913743303, 42.48315761423926, 13.008267820314629, 3.0499558709347525]],
    #             [[296.2596404495787, 93.34124407873878, 49.246980794141415, 11.618497117433385],
    #              [11.12485702945894, 4.455901612606825, 4.056566465770263, 1.9662712180214008, 0.8926719450962146,
    #               0.19541177675604438],
    #              [25.5100354358053, 17.08686471284569, 16.844865793675936, 0.5428152656838918, 0.19070963772058036]], [
    #                 [70.0396481274903, 59.608707557534146, 38.51576638178262, 26.4569543822238, 24.671465667642323,
    #                  17.922176497888003],
    #                 [44.562130445915756, 36.8410818568059, 25.950163155751444, 19.850327338471544, 18.638295798718502,
    #                  17.05548239459992, 15.278256601725058, 9.645154104593772], [108.29772302219027, 38.51576638178262]],
    #             [[50.406808680073084, 32.42536213535672, 19.65259307867751, 0.8632296832194628],
    #              [60.837153363052664, 18.16686852079357, 16.119416819014997, 13.357490538896023, 7.498987665227588],
    #              [175.78543727932671, 76.19879481420122, 32.91902613569545, 18.64552305946458, 10.330211291405996,
    #               0.12643026892776277]], [
    #                 [59.13718742610082, 43.44899962214271, 22.342653125818217, 11.406603155937882, 4.566090315532016,
    #                  2.7555355991922], [168.81377329113377, 45.31823223884715, 36.80515373003564, 17.451466974039903],
    #                 [68.66340747239997, 59.13718742610082, 23.5736489141147, 19.300365635588605, 8.166671039027255,
    #                  1.5835447934225098]], [
    #                 [86.18880057830786, 45.80995362637201, 36.76697189951031, 30.352493305696356, 14.092117008686458,
    #                  9.956839869574674],
    #                 [53.19818930070801, 45.80995362637201, 39.367822419015084, 23.788397179191804, 13.660529313233555,
    #                  0.7240038548446649], [108.76231156390081, 36.47138431367309, 33.663445415191596, 0.5300736854270269]],
    #             [[307.40358123898073, 54.91922744670431, 17.999246099120906],
    #              [84.06952821648702, 24.171242246753803, 7.0135259257665865, 4.8158887167851505, 3.5657553527944685],
    #              [7.991010830051135, 6.570465071539136, 5.677335493691517, 3.3046124176612266, 2.7284210186311775,
    #               2.632814728265832, 0.47067853010029737]]]
    #
    # modPath = [[0, 7, 11],[0, 2, 11],[0, 2, 11],[0, 6, 11],[0, 4, 11],[0, 3, 11],[0, 4, 11],[0, 8, 11],[0, 1, 11],[0, 1, 11]]
    #
    # MS = [16, 18, 20]

#
#   # 修改任务的参数
#     for i in range(len(modV)):
#         task[i].V = modV[i]
#         task[i].E = modE[i]
#         task[i].Ti = modT[i]
#         task[i].Di = modT[i]
#         task[i].P = modP[i]
#         # task[i].critical_path = modPath[i]
#         task[i].typeddag = typeddag[i]

    # for i in range(0, tasknum):
    #     print(f"当前的任务是：{i}")
    #     print(f"节点执行时间为：\n{task[i].V}")
    #     print(f"图中存在的边有：\n{task[i].E}")
    #     print(f"该任务的截止时间D_i为：{task[i].Di}")
    #     print(f"该任务的周期为T_i：{task[i].Ti}")
    #     print(f"该任务DAG图的关键路径为：{task[i].critical_path}")
    #     print(f"该任务的P值为：\n{task[i].P}") # P可能表示分到的类
    #     print(f"该任务的类型(? typeddag)为：\n{task[i].typeddag}")
    #     print(f"该任务的任务名为：{task[i].name}")
    #     print('====================================================')

    basic_result = get_set_R(task, MS)
    improved_result = get_set_R1(task, MS)
    print(f"改进前后的任务结果分别为：\n改进前：{basic_result}\n改进后：{improved_result}")

    # for i in range(0, len(task[0].V)):
    #     for j in anceV[i]:
    #         k_info_i = get_path_info(task[0], j, i)
    #         print("============================")
    #         print(f"当前的路径上是从{j}到{i},路径信息{k_info_i}")
    #         print("============================")

    # print("12")

