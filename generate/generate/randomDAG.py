#coding=utf-8
from __future__ import division
import math
import random
import copy
import pickle
# import numpy as np


# import  taskpro0
INF = pow(10, 5)
check_edge=[1]
for i in range(1,1000):
    check_edge.append(check_edge[i-1]+i+1)
# print check_edge

def printdag(DAG):
    for i in range(len(DAG)):
        print(DAG[i])


class DAG_t(object):
    def __init__(self,  V, E, Di, Ti, critical_path , P, typeddag, name='T' ):
        self.V = V
        self.E = E
        self.Di = Di
        self.Ti = Ti
        self.critical_path = critical_path
        self.P = P
        self.name = name
        self.typeddag=typeddag

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
        for i in range(0, len(self.critical_path)):
            w = w + self.V[self.critical_path[i]]
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






class generate_DAG(object):
    # 初始化
    def __init__(self, Ndagmin, Ndagmax, Tmin, Tmax, Pr, numP):
        self.Ndagmin = Ndagmin
        self.Ndagmax = Ndagmax
        self.Tmin = Tmin
        self.Tmax = Tmax
        self.Pr = Pr
        self.numP = numP
        # self.numMS=numMS

    # 每个结点的WETC生成
    def generate_edge(self, m, edgenum):
        tedge = [0] * edgenum
        tedge = random.sample(range(1, m + 1), edgenum)
        # print "tedge=",tedge
        return tedge

    # 边的位置寻找
    def locate_edge(self, num):
        for i in range(len(check_edge)):
            if num == check_edge[i]:
                return i,0
            elif num < check_edge[i] :
                j = check_edge[i] - num
                return i,j
                # if num < check_edge[i + 1]:
                #     j = check_edge[i + 1] - num
                #     return i + 1, j
                # 生成单一伪结点开始结束的G

    def extend_edge(self, dag):
        matrix_extend = [[0] * (len(dag) + 2) for i in range(len(dag) + 2)]
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
                matrix_extend[m + 1][len(matrix_extend) - 1] = 1
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
                matrix_extend[0][m2 + 1] = 1
                count2 = 0
        # 中间copy
        for m3 in range(len(dag)):
            for n3 in range(len(dag)):
                matrix_extend[m3 + 1][n3 + 1] = dag[m3][n3]
        #printdag(dag)
        #printdag(matrix_extend)
        # for t in range(len(matrix_extend)):
        #     print "matrix_extend=",matrix_extend[t]
        return matrix_extend

    # 求拓扑排序
    def Topological_sort(self, dag):
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
        #print(V)
        #print ("Cp=",Cp)
        return Cp

    # def longestPath(self,temdaf,V):

    # # 原版：实验中P从0到numV-1的整数序列中随机选择numP个不同的整数，返回一个列表
    # def randomPro(self,V,numP):
    #     numV=len(V)
    #     P=[0] * numV
    #     temp=[]
    #     typeddag=[]#按类别分类提取点，放入不同的分类，按点的执行时间大小进行排序
    #     for i in range(numP):
    #         typeddag.append([])
    #     # check_edge=[]
    #     for i in range(1,numP+1):
    #         temp.append(i)
    #     # print temp
    #     # for i in range(0,numV):
    #     #     check_edge.append(i)
    #     # 该函数从0到numV-1的整数序列中随机选择numP个不同的整数，返回一个列表。
    #     # 使用random.sample()函数可以确保所选的整数不重复
    #     tempP=random.sample(list(range(0,numV)),numP)
    #     for i in range(len(tempP)):
    #         P[tempP[i]]=i+1
    #         typeddag[i].append(tempP[i])
    #     # 检查是否存在没分配的点，存在就随机在1~nump-1赋值
    #     # i=0
    #     # while i < numP:
    #     #     x = random.randint(0, numV - 1)
    #     #     if P[x] == 0:
    #     #         P[x] = i + 1
    #     #         i += 1
    #     #     else:
    #     #         i -= 1
    #     for i in range(numV):
    #         if P[i] == 0:
    #             y = random.randint(1, numP)
    #             P[i] = y
    #             typeddag[y-1].append(i)
    #     # print "P=", P
    #     return [P,typeddag]


    # 实验中P随机分配
    def randomPro(self,V,numP):
        numV=len(V)
        P=[0] * numV
        temp=[]
        typeddag=[]#按类别分类提取点，放入不同的分类，按点的执行时间大小进行排序
        # 为每个点类型创建一个空列表，用于后续存储相同类型的点
        for i in range(numP):
            typeddag.append([])
        for i in range(1,numP+1):
            temp.append(i)
        # 函数从0到numV-1的整数中，随机选择numP个不同的整数，并返回一个列表，可以重复。
        tempP=random.choices(list(range(0,numV)),k=numP)
        # print tempP
        for i in range(len(tempP)):
            P[tempP[i]]=i+1
            typeddag[i].append(tempP[i])
        # 处理未被映射的顶点，随机映射到一个点上，并添加到对应的typeddag列表
        for i in range(numV):
            if P[i] == 0:

                y = random.randint(1, numP)
                P[i] = y
                typeddag[y-1].append(i)## y-1为下标
        # print "P=", P
        return [P,typeddag]


    # 原版
    def generate_DAG_task(self,U):
        # print("first of all")
        T = random.randint(self.Tmin, self.Tmax)
        # print "T=",T
        N = random.randint(self.Ndagmin, self.Ndagmax)
        # print "Node=",N
        D=T

        # 随即生成[0.1,1]之间的Pr值
        Pr = 0.1 + random.random() * 0.9
        Pr = round(Pr, 1)


        V = [0]*N
        # c = T * U

        # D = random.randint(int(T/2),T)
        # print "N=",N
        # print "V=",V

        # 初始化邻接矩阵
        matrix = [[0] * N for i in range(N)]
        # 最多有多少边
        # print('N=',N)
        # m_edge=math.floor(N * (N - 1) / 2)
        m_edge = int(N * (N - 1) / 2)
        # 实际有多少边
        # print "m_edge=",m_edge



        #
        # # 原版
        # r_edge = int(m_edge * self.Pr)

        # pr随机取值
        r_edge = int(m_edge * Pr)



        # print "edgenum=",r_edge
        # uniform 产生选取边
        #   endtedge=[0]*r_edge
        endtedge = self.generate_edge(m_edge, r_edge)
        #    print endtedge
        # 对邻接矩阵进行处理
        for i in range(r_edge):
            temp_edge = self.locate_edge(endtedge[i])
            matrix[N - 1 - temp_edge[0]-1][N - 1 - temp_edge[1]] = 1
        # for i in range(len(matrix)):
            # print(matrix[i])
            # 给E进行赋值
        E = []
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    E.append((i, j))
                    # print "E=",E
                    # 处理G，求cp
        matrix_extend = self.extend_edge(matrix)
        # for t in range(len(matrix_extend)):
        #     print "matrix_extend=",matrix_extend[t]
        # 添加两个伪结点后的V2
        V2 = copy.deepcopy(V)
        V2.insert(0, 0)
        V2.append(0)
        E2 = []
        for i in range(N + 2):
            for j in range(N + 2):
                if matrix_extend[i][j] == 1:
                    E2.append((i, j))
        # print "E2=",E2
        # print V2


        #属性赋予
        rettemp=self.randomPro(V, self.numP)#给每一个点都赋予一个type，其中每个type至少1个点。
        P=rettemp[0]
        typeddag=rettemp[1]

        #print ("P=",P)

        #U划分
        Uc = U#总利用率
        Up = []#每个类型核上所分到的总利用率。，加和等于U
        for i in range(1, self.numP):#给每一个类型的核上的总任务分配一个利用率
            Unc = Uc * random.uniform(0, 1) ** (1 / (self.numP - i))
            Up.append(Uc - Unc)
            Uc = Unc
        Up.append(Uc)
        pN=[0] * self.numP#每类核上 的 点个数。
        # print "Up=", Up
        sumUp=0
        for i in Up:
            sumUp+=i
        # print "sumUp=",sumUp
        #每种类型个数pN
        for i in range(self.numP):
            for j in range(len(V)):
                if P[j]== i+1:
                    pN[i]+=1
        # print "pN=",pN
        tempU=[[] * pN[i] for i in range(self.numP)]#每一类核上的每个任务的wcet
        #print(tempU)
        # print tempU
        for i in range(self.numP):
            c=T * Up[i]#每一类核上的总wcet
            # print "c=",c
            for k in range(1,pN[i]):
                nc=c * random.uniform(0,1)**(1/(pN[i]-k))
                tempU[i].append(c-nc)
                c=nc
            tempU[i].append(c)
            # print tempU[i]
        #print(tempU)
        #WCET赋予
        count=[0]*self.numP
        for i in range(0,N):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!给0号点也赋值了。
            j=P[i]-1
            V[i]=tempU[j][count[j]]
            count[j]+=1
        for i in range(0, N):
            V2[i + 1] = V[i]
        # print "test=",test

        for i in range (self.numP):################################################对应点的下表改成对应点的执行时间
            for j in range(len(typeddag[i])):
                typeddag[i][j]=V[typeddag[i][j]]

        for i in range(self.numP):######################################################按执行时间排序
            typeddag[i].sort(reverse=True)
            #print(len(typeddag[i]))

        start = random.randint(1, self.numP)
        sink = random.randint(1, self.numP)

        P.insert(0, start)
        P.append(sink)
        # print("长度", len(V2), "V2", V2)
        # print("长度", len(P), "P", P)
        # print("typed", typeddag)
        # print("P", len(P),len(V2))
        List = self.Topological_sort(matrix_extend)
        # print (List)
        Cp = self.longestPath(matrix_extend, List, V2)
        # print "Cp=",Cp
        task = DAG_t(V2, E2, D, T, Cp,  P,typeddag, "T%d" % 0)

        #print(task.typeddag)
        # print "task1.E=",task.E
        return task





#求祖先后继什么的
class findpcoDAG(object):
    # def __init__(self):
    #     self

    def find_ancestors(self,V,E):
        # task=self.generate_DAG_task(0)
        numV=len(V)
        parVset=[[0]]

        for i in range(1,numV): #每个结点的直接父亲节点parVset
            temp=[]
            for j in range(0,i):
                if(j,i) in E:
                    temp.append(j)
            parVset.append(temp)
        # parVsetA=[]
        # print parVset
        for i in range(0,numV): #求每个节点的所有祖先节点
            temp3=[]
            for j in parVset[i]:
                temp3=list(set(parVset[j]+parVset[i]))
                parVset[i]=temp3

        #parVset存储每个结点的所有祖先
        # print "parVset=",parVset
        # print E
        return parVset

    def find_child(self,V,E):
        numV = len(V)
        childVset = []

        for i in range(numV-1,-1,-1):  # 每个结点的直接孩子结点childVset
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

        for i in range(numV-1,-1,-1):  # 求每个结点的所有后继节点
            temp3 = []
            for j in childVset[i]:
                temp3 = list(set(childVset[j] + childVset[i]))
                childVset[i] = temp3
        # print "childVset=",childVset
        # print E
        return childVset

    def find_parallel(self,V,E,P):
        pset=self.find_ancestors(V,E)
        # print "pset=",pset
        numV=len(V)
        cset=self.find_child(V,E)
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


class RandomTask(object):
    # 初始化
    def __init__(self, Tmin, Tmax, numP):
        self.Tmin = Tmin
        self.Tmax = Tmax
        self.numP = numP
        # self.numMS=numMS
    def creattask(self,Umin, Umax):
        Ti=random.randint(self.Tmin,self.Tmax)
        Ui=random.uniform(Umin,Umax)
        Ci=math.ceil(Ti*Ui)
        Si=random.randint(1,self.numP)
        Di=Ti
        task=[Ci,Ti,Di,Si]
        return task
    def creatTsets_s(self,s,n_s,U_s):
        U=[]
        Tsets=[]
        if n_s>1:
            for i in range(1,n_s):
                nextU = U_s * random.uniform(0, 1) ** (1 / (n_s - i))
                U.append(U_s-nextU)
                U_s=nextU
            U.append(U_s)
        else:
            U.append(U_s)
        T=[]
        #print("U:",U)
        for u in U:
            Ti=random.randint(self.Tmin,self.Tmax)
            Ci = math.ceil(Ti * u)
            # Si = random.randint(1, self.numP)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)
        Tsets_tp=[]
        for i in range(0,len(T)):
            tmin=min(T)
            index_t=T.index(tmin)
            Tsets_tp.append(Tsets[index_t])
            T[index_t]=T[index_t]+10000

        return Tsets_tp



    def creatTsets_s_2(self,s,n_s):
        U=[]
        Tsets=[]

        T=[]
        #print("U:",U)
        for x in range(0,n_s):
            Ti=random.randint(self.Tmin,self.Tmax)
            Ci = 0#暂时
            # Si = random.randint(1, self.numP)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)
        Tsets_tp=[]
        for i in range(0,len(T)):
            tmin=min(T)
            index_t=T.index(tmin)
            Tsets_tp.append(Tsets[index_t])
            T[index_t]=T[index_t]+10000

        return Tsets_tp

    def creatTsets(self,T_s,Thps):
        if len(Thps) == 0:
            for task in T_s:
                Thps.append(task)
        else:
            start = 0
            for task in T_s:
                p_c = task[1]
                for irt_ts in range(start, len(Thps)):
                    # print(len(Thps))
                    if p_c >= Thps[irt_ts][1]:
                        if start==len(Thps)-1:
                            Thps.append(task)
                            break
                        else:
                            start=start+1
                    else:
                        Thps.insert(start, task)
                        break
        return Thps
    def creatTsets_s_3(self,s,n_s,u):

        T=[]
        Tsets = []
        #print("U:",U)
        for i in range(0,n_s):
            Ti=random.randint(self.Tmin,self.Tmax)
            Ci = math.ceil(Ti * u)
            # Si = random.randint(1, self.numP)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)
        Tsets_tp=[]
        for i in range(0,len(T)):
            tmin=min(T)
            index_t=T.index(tmin)
            Tsets_tp.append(Tsets[index_t])
            T[index_t]=T[index_t]+10000

        return Tsets_tp

    def creatTsets_s_final(self,s,n_s,Us):
        U=Us
        Tsets=[]
        Umax=U/n_s
        if(Umax>=1):
            Umax=0.7

        T=[]
        #print("U:",U)
        Udag=0
        for x in range(0,n_s):
            Ti=random.randint(self.Tmin,self.Tmax)

            Ui=random.uniform(Umax/2,Umax)
            Udag=Udag+(Umax-Ui)

            Ci = Ui*Ti  # 暂时
            # Si = random.randint(1, self.numP)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)
        Tsets_tp=[]
        for i in range(0,len(T)):
            tmin=min(T)
            index_t=T.index(tmin)
            Tsets_tp.append(Tsets[index_t])
            T[index_t]=T[index_t]+10000

        return [Tsets_tp,Udag]

    def creatTsets_s_final2(self,s,n_s,Us):
        U=Us
        Tsets=[]
        Umax=U/n_s
        whatsleft=0
        T = []
        if(Umax>=1):
            Umax=0.7
            Udag=U-0.7*n_s
        else:
        #print("U:",U)
            Udag=0
        #分配U
        Utemp=[]
        for x in range(0,n_s):

            Ui=random.uniform(Umax/2,Umax)

            whatsleft=whatsleft+(Umax-Ui)
            Utemp.append(Ui)
        average=whatsleft/n_s
        for x in range(0, n_s):
            if (Utemp[x]+average)<=0.75:
                Utemp[x]=Utemp[x]+average
            else:
                Udag=Udag+(Utemp[x]+average-0.75)
                Utemp[x] = 0.75


        for x in range(0, n_s):
            Ti = random.randint(self.Tmin, self.Tmax)
            Ci = Utemp[x]*Ti  # 暂时
            # Si = random.randint(1, self.numP)
            Di = Ti
            task = [Ci, Ti, Di, s]
            Tsets.append(task)
            T.append(Ti)
        Tsets_tp=[]
        for i in range(0,len(T)):
            tmin=min(T)
            index_t=T.index(tmin)
            Tsets_tp.append(Tsets[index_t])
            T[index_t]=T[index_t]+10000

        return [Tsets_tp,Udag]





if __name__ == '__main__':
    # task=RandomTask(10,1000,5)
    # Tset=task.creatTsets_s(1,2,0.1)
    # print(Tset)

    # T_s=[[3, 114, 114, 2], [5, 226, 226, 2], [3, 350, 350, 2], [24, 711, 711, 3]]
    # Thps=[[22, 268, 268, 1], [15, 698, 698, 1]]
    # T_s2=[[1, 782, 782, 5], [17, 825, 825, 3]]
    # T=task.creatTsets(T_s,Thps)
    # T=task.creatTsets(T_s2,T)

    #          Ndagmin, Ndagmax, tmin, Tmax, Pr, numP
    T=generate_DAG(5,5,10,1000,0.2,5)
    task=T.generate_DAG_task(0.5)

    numV = len(task.V)
    for i in range(numV):
        print("[v%d,%d]"%(i,task.P[i]))
    #print(task.Ci()/task.Ti)
    # for n in range(50):
        # task=generate_DAG(5,30,40,1000,0.2,7
        # T=task.generate_DAG_task(0)
        # paV=findpcoDAG().find_ancestors(T.V,T.E)
        # chV=findpcoDAG().find_child(T.V,T.E)
        # paraV=findpcoDAG().findnorelationV(T.V,T.E,T.P)
    # v=[1,3,4,5,6,10,1,11,15,2,1 ]
    # e=[(0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,10),(5,10),(6,8),(7,9),(8,10),(9,10) ]
    # type=[1,1,2,1,1,2,2,2,1,1,1]
    # MS=[2,3]
    # print (len(v))
    # print (len(e))
    #  Ndagmin, Ndagmax, Tmin, Tmax, Pr, numP):
    # T=DAG_t(v,e,100,100,0,type)

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
    # # paV=findpcoDAG().find_ancestors(T.V,T.E)
    # # print paV
    # # chV=findpcoDAG().find_child(T.V,T.E)
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

