#coding=utf-8

import randomDAG
import random
import copy

#id, V, E, Di, Ti, Cpi, SL, P, name='T'
def schedulAlgorithm(task,MS):
    # print "oldV=",task.V
    # print task.P
    # print "oldcp=",task.Cpi
    V=[]
    E=[]
    P=[]
    lenP=len(task.P)
    lenV=len(task.V)        #lenV结点个数
    lenS=len(MS)
    MaxMs=max(MS)#lenS种类个数
    for i in range(lenP):
        # 重新计算任务
        V.append(task.V[i] * (1 - 1 / MaxMs * 1.0))
        # for j in range(lenS):
        #     if task.P[i]== j+1:

    # print "oldV=",task.V
    # 0, v, e, 100, 100, 0, 0, type
    newT=randomDAG.DAGtask(V,task.E,task.Di,task.Ti,0,task.P)
    return newT

# 找有向图的拓扑排序
def TPOrder(dag, V):
    List = [0] * len(dag)
    indegree = [0] * len(dag)
    Stack = [0] * len(dag)
    top = 0
    # 记录每个结点的入度
    for i in range(len(dag)):
        for j in range(len(dag)):
            if dag[j][i] != 0:
                indegree[i] += 1
        # 将入度为0的线进栈
        if indegree[i] == 0:
            Stack[top] = i
            top += 1
    count3 = 0
    while top != 0:
        top -= 1
        i = Stack[top]
        # 将栈顶元素添加到list中去
        List[count3] = i
        count3 += 1
        for j in range(len(dag)):
            # 更新结点的入度，并且将新的入度为0的节点放在栈中去
            if dag[i][j] != 0:
                indegree[j] -= 1
                if indegree[j] == 0:
                    Stack[top] = j
                    top += 1
    return List

# 查找关键路径
def findCriPath(newT):
    #find the ctitial path of the changebal task
    # newT=schedulAlgorithm(task,MS)
    # tdag标记图中边的关系
    tdag = [[0] * len(newT.V) for i in range(len(newT.V))]
    # print tdag
    for (i,j) in newT.E:
        try:
            tdag[i][j]=1
        except(IndexError):
            print("the edge is (%d,%d)"%(i,j))
    # print tdag
    List=TPOrder(tdag,newT.V)
    V=newT.V
    # el最早开始时间
    el = [0] * len(tdag)
    path_l = [[0] * len(tdag) for i in range(len(tdag))]
    n_l = [0] * len(tdag)
    n_l[0] = 1
    Cp = []
    el[0]=V[0]
    # 计算最早开始时间
    for i in range(len(tdag)):
        k = List[i]
        # print (k)
        for j in range(len(tdag)):
            if tdag[k][j] == 1:
                # 在(V[j] + el[k]) > el[j]时，更新el[j]的值，即更新j的最早开始时间
                if (V[j] + el[k]) > el[j]:
                    el[j] = V[j] + el[k]
                    # print n_l[k]
                    # print n_l[j]
     # print (el)

    return el[len(tdag)-1]

# 计算每个任务类型的总的执行时间
# 每个元素 wcetS[j] 表示第 j+1 种任务类型的总执行时间。
def totalAllS(task,MS):
    lenS=len(MS)    # lenS任务类型数量
    lenV=len(task.V)    # lenV任务结点数量
    wcetS=[0] * lenS        #wcetS[0]指的是第一类，依此类推
    for i in range(lenV):
        for j in range(lenS):
            # 检查它的任务类型是否等于当前任务类型的索引加1
            if task.P[i]== j+1:
                # 条件成立，表示该任务结点属于当前任务类型，
                # 将该任务结点的执行时间 task.V[i] 累加到 wcetS[j] 中。
                wcetS[j]+=task.V[i]
    # print "wcetS=",wcetS
    return wcetS

# def critotalS(task,CP,MS):
#     # newT = schedulAlgorithm(task, MS)
#     lenCp=len(CP)
#     lenS=len(MS)
#     criWectS=[0] * lenS
#     for i in range(lenCp):
#         for j in range(lenS):
#             if task.P[CP[i]]== j+1:
#                 criWectS[j]+=task.V[CP[i]]
#     # print "criWectS=",criWectS
#     return criWectS

# 计算最坏响应时间
def getwcrt(task,MS):
    T=schedulAlgorithm(task,MS)
    # 调用 totalAllS(task, MS) 函数
    # 该函数计算每种任务类型的总执行时间，并将结果存储在 ws 列表中。
    ws=totalAllS(task,MS)
    # print "ws=",ws
    # 找出关键路径
    cp=findCriPath(T)
    # ls=critotalS(T,cp,MS)
    # # print ls
    # a=0
    # for i in range(len(ls)):
    #     a+=ls[i]
    b=0
    for i in range(len(ws)):
        b+=((ws[i])/MS[i])
    RT=cp+b
    # print "RT=",RT
    return RT