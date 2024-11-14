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
    lenS=len(MS)            #lenS种类个数
    for i in range(lenP):
        for j in range(lenS):
            if task.P[i]== j+1:
                V.append(task.V[i]*(1-1/MS[j]*1.0))
    # print "oldV=",task.V
    # 0, v, e, 100, 100, 0, 0, type
    newT=randomDAG.DAGtask(V,task.E,task.Di,task.Ti,0,task.P)
    return newT

# 拓扑排序
def TPOrder(dag):
    List = [0] * len(dag)
    indegree = [0] * len(dag)
    Stack = [0] * len(dag)
    top = 0
    # 记录每个结点的入度
    for i in range(len(dag)):
        for j in range(len(dag)):
            if dag[j][i] != 0:
                indegree[i] += 1
        if indegree[i] == 0:
            Stack[top] = i
            top += 1
    count3 = 0
    while top != 0:
        top -= 1
        i = Stack[top]
        List[count3] = i
        count3 += 1
        for j in range(len(dag)):
            if dag[i][j] != 0:
                indegree[j] -= 1
                if indegree[j] == 0:
                    Stack[top] = j
                    top += 1
    return List

# 找关键路径
def findCriPath(newT):
    #find the ctitial path of the changebal task
    # newT=schedulAlgorithm(task,MS)
    tdag = [[0] * len(newT.V) for i in range(len(newT.V))]
    # print tdag
    for (i,j) in newT.E:
        try:
            tdag[i][j]=1
        except(IndexError):
            print("the edge is (%d,%d)"%(i,j))
    # print tdag
    List=TPOrder(tdag)
    V=newT.V
    el = [0] * len(tdag)
    path_l = [[0] * len(tdag) for i in range(len(tdag))]
    n_l = [0] * len(tdag)
    n_l[0] = 1
    Cp = []
    el[0]=V[0]
    for i in range(len(tdag)):
        k = List[i]
        # print (k)
        for j in range(len(tdag)):
            if tdag[k][j] == 1:
                if (V[j] + el[k]) > el[j]:
                    el[j] = V[j] + el[k]
                    # print n_l[k]
                    # print n_l[j]
    # print (el)

    return el[len(tdag)-1]

def totalAllS(task,MS):
    lenS=len(MS)
    lenV=len(task.V)
    wcetS=[0] * lenS        #wcetS[0]指的是第一类，依此类推
    for i in range(lenV):
        for j in range(lenS):
            if task.P[i]== j+1:
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

# 最坏响应时间
def getwcrt(task,MS):
    T=schedulAlgorithm(task,MS)
    ws=totalAllS(task,MS)
    # print "ws=",ws
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