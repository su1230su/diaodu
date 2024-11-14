#coding=utf-8
from __future__ import division
import math
import random
import copy
import pickle
# import numpy as np


# import  taskpro0
INF = pow(10, 5)
temp2=[1]
for i in range(1,1000):
    temp2.append(temp2[i-1]+i+1)
# print temp2

def printdag(DAG):
    for i in range(len(DAG)):
        print(DAG[i])


class DAGtask(object):
    def __init__(self,  V, E, Di, Ti, Cpi, P, name='T'):
        self.V = V
        self.E = E
        self.Di = Di
        self.Ti = Ti
        self.Cpi = Cpi
        self.P = P
        self.name = name

    def Ci(self):
        ci = 0
        for i in range(0, len(self.V)):
            ci = ci + self.V[i]
        return ci

    def Ui(self):
        ci = self.Ci()
        return ci / self.Ti

    def wcp(self):
        w = 0
        for i in range(0, len(self.Cpi)):
            w = w + self.V[self.Cpi[i]]
        return w

    def isparent(self, i, j):
        re = True
        if (i, j) in self.E:
            return True
        else:
            return False

    def parents(self, i):
        par = []
        for j in range(0, len(self.V)):
            if self.isparent(i, j):
                par.append(j)
        return par


class MCTaskSet(object):
    def __init__(self):
        # All tasks existing in low-criticality mode, i.e., *all* tasks for
        # standard certification cognizant models.
        self.Tsets = set()

    # adding a new task
    def add(self, T):

        self.Tsets.add(T)

    def clear(self):
        self.Tsets = set()

    def u(self):
        return sum([T.Ui() for T in self.Tsets])






class RandomDAGtask(object):
    # 初始化
    def __init__(self, Nummini, Nummax, Tmini, Tmax, Pr, numP):
        self.Nummini = Nummini
        self.Nummax = Nummax
        self.Tmini = Tmini
        self.Tmax = Tmax
        self.Pr = Pr
        self.numP = numP
        # self.numMS=numMS

    # 每个结点的WETC生成
    def dealInfo(self, m, edgenum):
        tedge = [0] * edgenum
        tedge = random.sample(range(1, m + 1), edgenum)
        # print "tedge=",tedge
        return tedge

    # 边的位置寻找
    def findp(self, num):
        for i in range(len(temp2)):
            if num == temp2[i]:
                return i,0
            elif num < temp2[i] :
                j = temp2[i] - num
                return i,j
                # if num < temp2[i + 1]:
                #     j = temp2[i + 1] - num
                #     return i + 1, j
                # 生成单一伪结点开始结束的G

    def endDAG(self, dag):
        tdag2 = [[0] * (len(dag) + 2) for i in range(len(dag) + 2)]
        count1 = 0
        count2 = 0
        # 终点
        for m in range(len(dag)):
            for n in range(len(dag)):
                if dag[m][n] == 0:
                    count1 = 1
                else:
                    count1 = 0
                    break
            if count1:
                tdag2[m + 1][len(tdag2) - 1] = 1
                count1 = 0
        # 起点
        for m2 in range(len(dag)):
            for n2 in range(len(dag)):
                if dag[n2][m2] == 0:
                    count2 = 1
                else:
                    count2 = 0
                    break
            if count2 == 1:
                tdag2[0][m2 + 1] = 1
                count2 = 0
        # 中间copy
        for m3 in range(len(dag)):
            for n3 in range(len(dag)):
                tdag2[m3 + 1][n3 + 1] = dag[m3][n3]
        #printdag(dag)
        #printdag(tdag2)
        # for t in range(len(tdag2)):
        #     print "tdag2=",tdag2[t]
        return tdag2

    # 求拓扑排序
    def TPOrder(self, dag):
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



    # 求cp
    def longestPath(self, tempdag, List, V):
        #初始化从source点到计算节点的最长路径
        el = [0] * len(tempdag)
        # print "temdag=",tempdag
        # 存储两点之间的最长路径
        path_l = [[0] * len(tempdag) for i in range(len(tempdag))]
        #存储v0到v的结点个数
        n_l = [0] * len(tempdag)
        n_l[0] = 1
        l = 0
        Cp = []
        for i in range(len(tempdag)):
            k = List[i]
            # print k
            for j in range(len(tempdag)):
                if tempdag[k][j] == 1:
                    if (V[j] + el[k]) > el[j]:
                        el[j] = V[j] + el[k]
                        # print n_l[k]
                        x = 0
                        for l in range(n_l[k] + 1):
                            path_l[j][l] = path_l[k][l]
                            x = l
                        path_l[j][x] = j
                        n_l[j] = x + 1
                        # print n_l[j]
        #print el
        #print n_l[len(tempdag) - 1]
        for i in range(n_l[len(tempdag) - 1]):
            Cp.append(path_l[len(tempdag) - 1][i])
        # print "Cp=",Cp
        return Cp

    # def longestPath(self,temdaf,V):


    def randomPro(self,V,numP):
        numV=len(V)
        P=[0] * numV
        temp=[]
        # temp2=[]
        for i in range(1,numP+1):
            temp.append(i)
        # print temp
        # for i in range(0,numV):
        #     temp2.append(i)
        tempP=random.sample(list(range(0,numV)),numP)
        # print tempP
        for i in range(len(tempP)):
            P[tempP[i]]=i+1
        # i=0
        # while i < numP:
        #     x = random.randint(0, numV - 1)
        #     if P[x] == 0:
        #         P[x] = i + 1
        #         i += 1
        #     else:
        #         i -= 1
        for i in range(numV):
            if P[i] == 0:
                y = random.randint(1, numP)
                P[i] = y
        # print "P=", P
        return P

    def createtask(self,U):
        T = random.randint(self.Tmini, self.Tmax)
        # print "T=",T
        N = random.randint(self.Nummini, self.Nummax)
        # print "Node=",N
        D=T


        V = [0]*N
        # c = T * U

        # D = random.randint(int(T/2),T)
        # print "N=",N
        # print "V=",V

            # 初始化邻接矩阵
        tdag = [[0] * N for i in range(N)]
        # 最多有多少边
        # print('N=',N)
        # maxEdge=math.floor(N * (N - 1) / 2)
        maxEdge = int(N * (N - 1) / 2)
        # 实际有多少边
        # print "maxEdge=",maxEdge
        realedge = int(maxEdge * self.Pr)
        # print "edgenum=",realedge
        # uniform 产生选取边
        #   endtedge=[0]*realedge
        endtedge = self.dealInfo(maxEdge, realedge)
        #    print endtedge
        # 对邻接矩阵进行处理
        for i in range(realedge):
            edgeplace = self.findp(endtedge[i])
            tdag[N - 1 - edgeplace[0]-1][N - 1 - edgeplace[1]] = 1

            #    print tdag
            # 给E进行赋值
        E = []
        for i in range(N):
            for j in range(N):
                if tdag[i][j] == 1:
                    E.append((i, j))
                    # print "E=",E
                    # 处理G，求cp
        tdag2 = self.endDAG(tdag)
        # for t in range(len(tdag2)):
        #     print "tdag2=",tdag2[t]
        # 添加两个伪结点后的V2
        V2 = copy.deepcopy(V)
        V2.insert(0, 0)
        V2.append(0)
        E2 = []
        for i in range(N + 2):
            for j in range(N + 2):
                if tdag2[i][j] == 1:
                    E2.append((i, j))
        # print "E2=",E2
        # print V2


        #属性赋予
        P=self.randomPro( V2, self.numP)
        # print "P=",P

        #U划分
        Uc = U
        Up = []
        for i in range(1, self.numP):
            Unc = Uc * random.uniform(0, 1) ** (1 / (self.numP - i))
            Up.append(Uc - Unc)
            Uc = Unc
        Up.append(Uc)
        pN=[0] * self.numP
        # print "Up=", Up
        sumUp=0
        for i in Up:
            sumUp+=i
        # print "sumUp=",sumUp
        #每种类型个数pN
        for i in range(self.numP):
            for j in range(len(V2)):
                if P[j]== i+1:
                    pN[i]+=1
        # print "pN=",pN
        tempU=[[] * self.numP for i in range(self.numP)]
        # print tempU
        for i in range(self.numP):
            c=T * Up[i]
            # print "c=",c
            for k in range(1,pN[i]):
                nc=c * random.uniform(0,1)**(1/(pN[i]-k))
                tempU[i].append(c-nc)
                c=nc
            tempU[i].append(c)
            # print tempU[i]
        #WCET赋予
        count=[0]*self.numP
        for i in range(1,N+2):
            j=P[i]-1
            V2[i]=tempU[j][count[j]]
            count[j]+=1
        test=0
        for i in V2:
            test+=i
        # print "test=",test
        List = self.TPOrder(tdag2)
        # print List
        Cp = self.longestPath(tdag2, List, V2)
        # print "Cp=",Cp
        task = DAGtask(V2, E2, D, T, Cp,  P, "T%d" % 0)
        # print "task1.E=",task.E
        return task


#求祖先后继什么的
class findpcoDAG(object):
    # def __init__(self):
    #     self

    def findpa(self,V,E):
        # task=self.createtask(0)
        numV=len(V)
        parVset=[[0]]
        # 每个结点的直接父亲节点parVset
        for i in range(1,numV):
            temp=[]
            for j in range(0,i):
                if(j,i) in E:
                    temp.append(j)
            parVset.append(temp)
        # parVsetA=[]
        # print parVset
        # 求每个节点的所有祖先节点
        for i in range(0,numV):
            temp3=[]
            for j in parVset[i]:
                temp3=list(set(parVset[j]+parVset[i]))
                parVset[i]=temp3

        #parVset存储每个结点的所有祖先
        # print "parVset=",parVset
        # print E
        return parVset

    def findchild(self,V,E):
        numV = len(V)
        childVset = []
        # 每个结点的直接孩子结点childVset
        for i in range(numV-1,-1,-1):
            temp = []
            # print "i=",i
            for j in range(i,numV):
                if (i, j) in E:
                    temp.append(j)
                    # print "j=",j
            childVset.insert(0,temp)
        # parVsetA=[]
        childVset[numV-1]=[numV-1]
        # print childVset

        # 求每个结点的所有后继节点
        for i in range(numV-1,-1,-1):
            temp3 = []
            for j in childVset[i]:
                temp3 = list(set(childVset[j] + childVset[i]))
                childVset[i] = temp3
        # print "childVset=",childVset
        # print E
        return childVset

    def findnorelationV(self,V,E,P):
        pset=self.findpa(V,E)
        # print "pset=",pset
        numV=len(V)
        cset=self.findchild(V,E)
        # print "cset=",cset
        parllalset=[]
        for i in range(0,numV):
            temp=[]
            # print pset[i]ba
            # print "i=",i
            for j in range(0,numV):
                if j not in (pset[i]+cset[i]) and j!=i and P[i]==P[j]:
                    # print "j=",j
                    temp.append(j)
            parllalset.append(temp)
        # print "parralset=",parllalset
        return parllalset

    #返回宽度优先拓扑排序
    def BfsOrder(self,dag):
        # print ("dag.E=",dag.E)
        res=[]
        res.append(0)
        inD=[0]* len(dag.V)
        for (i,j) in dag.E:
            inD[j]+=1
        # print ("inD=",inD)
        inD[0]=-1
        x=1
        # print ("res=",res)
        #因为情况特殊，肯定是0节点开始入度为0省去判断
        # res.append(0)
        for (i,j) in dag.E:
            if i==0:
                res.append(j)
                inD[j]-=1
        # print ("res",res)
        # print ("inD",inD)
        while x<len(dag.V):
            for k in range(x,len(res)):
                for (i,j) in dag.E:
                    if i==k :
                        inD[j]-=1
                        if inD[j]==0:
                            res.append(j)
                            inD[j]=-1
                            # print ("inD",inD)
                x+=1
        # print ("res=",res)
        return res


# class RandomTask(object):
#     # 初始化
#     def __init__(self, Tmini, Tmax, numP):
#         self.Tmini = Tmini
#         self.Tmax = Tmax
#         self.numP = numP
#         # self.numMS=numMS
#     def creattask(self,Umin, Umax):
#         Ti=random.randint(self.Tmini,self.Tmax)
#         Ui=random.uniform(Umin,Umax)
#         Ci=math.ceil(Ti*Ui)
#         Si=random.randint(1,self.numP)
#         Di=Ti
#         task=[Ci,Ti,Di,Si]
#         return task
#     # 生成任务集
#     def creatTsets_s(self,s,n_s,U_s):
#         U=[]
#         Tsets=[]
#         if n_s>1:
#             for i in range(1,n_s):
#                 nextU=U_s*random.uniform(0,1)**(1/(n_s-i))
#                 U.append(U_s-nextU)
#                 U_s=nextU
#             U.append(U_s)
#         else:
#             U.append(U_s)
#         T=[]
#         # 根据U值生成任务集
#         for u in U:
#             Ti=random.randint(self.Tmini,self.Tmax)
#             Ci = math.ceil(Ti * u)
#             # Si = random.randint(1, self.numP)
#             Di = Ti
#             task = [Ci, Ti, Di, s]
#             Tsets.append(task)
#             T.append(Ti)
#         Tsets_tp=[]
#         # 据任务的Ti值升序排列任务集，并返回排序后的任务集列表。
#         for i in range(0,len(T)):
#             tmin=min(T)
#             index_t=T.index(tmin)
#             Tsets_tp.append(Tsets[index_t])
#             T[index_t]=T[index_t]+10000
#
#         return Tsets_tp
#
#     # 用于将一组任务T_s插入到已排序的任务集Thps中
#     def creatTsets(self,T_s,Thps):
#         if len(Thps) == 0:
#             for task in T_s:
#                 Thps.append(task)
#         else:
#             start = 0
#             # 遍历T_s的每个任务
#             for task in T_s:
#                 p_c = task[1]
#                 for irt_ts in range(start, len(Thps)):
#                     # print(len(Thps))
#                     # 如果当前任务的优先级大于等于Thps中的任务优先级，则继续检查下一个任务
#                     if p_c >= Thps[irt_ts][1]:
#                         if start==len(Thps)-1:
#                             # 如果已经遍历到Thps的末尾，则将当前任务添加到Thps的末尾
#                             Thps.append(task)
#                             break
#                         else:
#                             start=start+1
#                     else:
#                         # 如果当前任务的优先级小于Thps中的任务优先级，则将当前任务插入到Thps的当前位置
#                         Thps.insert(start, task)
#                         break
#         return Thps



class RandomTask(object):
    def __init__(self, Tmini, Tmax, numP):
        self.Tmini = Tmini
        self.Tmax = Tmax
        self.numP = numP

    def creattask(self, Umin, Umax):
        Ti = random.randint(self.Tmini, self.Tmax)
        Ui = random.uniform(Umin, Umax)
        Ci = math.ceil(Ti * Ui)
        Si = random.randint(1, self.numP)
        Di = Ti
        task = [Ci, Ti, Di, Si]
        return task

    def creatTsets_s(self, s, n_s, U_s):
        U = []
        Tsets = []
        if n_s > 1:
            for i in range(1, n_s):
                nextU = U_s * random.uniform(0, 1) ** (1 / (n_s - i))
                U.append(U_s - nextU)
                U_s = nextU
            U.append(U_s)
        else:
            U.append(U_s)

        T = []
        for u in U:
            Ti = random.randint(self.Tmini, self.Tmax)
            Ci = math.ceil(Ti * u)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)

        Tsets_tp = sorted(Tsets, key=lambda x: x[1])  # 根据任务的 Ti 值升序排列任务集
        return Tsets_tp

    def creatTsets(self, T_s, Thps):
        if not Thps:
            Thps.extend(T_s)
        else:
            start = 0
            for task in T_s:
                p_c = task[1]
                for irt_ts in range(start, len(Thps)):
                    if p_c >= Thps[irt_ts][1]:
                        if start == len(Thps) - 1:
                            Thps.append(task)
                            break
                        else:
                            start = start + 1
                    else:
                        Thps.insert(start, task)
                        break
        return Thps



if __name__ == '__main__':
    # task=RandomTask(10,1000,5)
    # Tset=task.creatTsets_s(1,2,0.1)
    # print(Tset)

    # T_s=[[3, 114, 114, 2], [5, 226, 226, 2], [3, 350, 350, 2], [24, 711, 711, 3]]
    # Thps=[[22, 268, 268, 1], [15, 698, 698, 1]]
    # T_s2=[[1, 782, 782, 5], [17, 825, 825, 3]]
    # T=task.creatTsets(T_s,Thps)
    # T=task.creatTsets(T_s2,T)
    T=RandomDAGtask(1,1,10,20,0,1)
    task=T.createtask(0)
    print(task)
    # for n in range(50):
        # task=RandomDAGtask(5,30,40,1000,0.2,7
        # T=task.createtask(0)
        # paV=findpcoDAG().findpa(T.V,T.E)
        # chV=findpcoDAG().findchild(T.V,T.E)
        # paraV=findpcoDAG().findnorelationV(T.V,T.E,T.P)
    # v=[1,3,4,5,6,10,1,11,15,2,1 ]
    # e=[(0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,10),(5,10),(6,8),(7,9),(8,10),(9,10) ]
    # type=[1,1,2,1,1,2,2,2,1,1,1]
    # MS=[2,3]
    # print (len(v))
    # print (len(e))
    # T=DAGtask(v,e,100,100,0,type)

    # for i in  range(0,len(T.V)):
    #     print "[v%d,%d]"%(i,T.V[i])
    #     print T.P[i]
    # print T.V
    # print T.P

        # print MS
        #算法1
    # newT=Baseline.schedulAlgorithm(T,MS)
    # print("newT.V=",newT.V)
    # print(newT.P)
    # print(T.V)
    # print(T.P)
    # # #
    # newCP=Baseline.findCriPath(T)
    # print (newCP)
    #
    # wectAllS=Baseline.totalAllS(T,MS)
    # print (wectAllS)
    # # criWectS=schedulAlgorithm.critotalS(T,newCP,MS)
    # # print (criWectS)
    # RT=Baseline.getwcrt(T,MS)
    # print(RT)
    #     # #算法2
    # # paV=findpcoDAG().findpa(T.V,T.E)
    # # print paV
    # # chV=findpcoDAG().findchild(T.V,T.E)
    # # print  chV
    # # paraV=findpcoDAG().findnorelationV(T.V,T.E,T.P)
    # # print paraV
    # # subSet=schedulAlgorithm2.schedulAlgorithm2(T,chV,paraV)
    # # # # print "paraV=",paraV
    # # print "subSet=",subSet
    # #
    # # inter=schedulAlgorithm2.findInter(T,subSet,chV,paV)
    # # print inter
    # rt=schedulAlgorithm2.findRT(T,MS)
    # print(rt)

