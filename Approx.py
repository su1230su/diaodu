#coding=utf-8

import randomDAG
import copy

# 计算任务调度
def schedulAlgorithm2(task,paraV,MS):
    lenV=len(task.V)    # 获取任务点的顶点个数
    lenparaV=len(paraV)     # 获取参数paraV的数量
    lenMS=len(MS)       # 获取执行环境的数量
    # print ("lenMS=",lenMS)
    # print "paraV=",paraV
    # 创建存储节点的前驱结点的列表preV[]
    preV=[]
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            # 检查是否有一条从顶点j到顶点i的有向边存在于任务的边集合task.E中
            if (j, i) in task.E:
                # 将前驱顶点的索引j添加到temp列表中，表示顶点i的前驱是顶点j。
                temp.append(j)
        # 将temp列表添加到名为preV的列表中，表示存储了顶点i的前驱顶点。
        preV.append(temp)
    # print("preV=",preV)

    # 创建一个 It 列表，它具有 lenV 行和 lenV 列，其中每个元素都是一个空列表
    # 二维列表It用来存储任务的执行时间
    It=[[]*lenV for i in range(lenV)]
    # 二位列表At用来存储任务的调度时间
    # At=[[]*lenV for i in range(lenV)]

    for i in range(lenV):
        # print("i=", i)
        # print("task.P[i]=%d,i=%d" % (task.P[i], i))

        # 创建一个名为 Ittemp 的二维列表，其中有 lenMS 行和 lenMS 列。这个列表将用于存储任务执行时间
        Ittemp=[[]* lenMS for k in range(lenMS)]
        # lenMS 表示执行环境的数量
        for j in range(1,lenMS+1):
            # 检查任务的优先级（task.P[i]）是否等于当前执行环境（j）
            if task.P[i]==j:
                # print ("task.P[i]=%d,j=%d"%(task.P[i],j))
                # Ittemp[j-1]=paraV[i]：将 paraV[i] 的值赋给 Ittemp 的第 j-1 行，表示任务 i 在执行环境 j 中的执行时间
                Ittemp[j-1]=paraV[i]
                # 表示任务 i 在不同执行环境中的执行时间。
                It[i]=Ittemp
            # print ("It[i]=",It[i])
    # print ("It=",It)
    # At=copy.deepcopy(It)：创建 At 的深度副本，以便进一步使用。At 是 It 的一个副本，两者之间的操作不会相互影响
    At=copy.deepcopy(It)
    # print ("At=",At)
    # for i in range(lenV):
        # print("i=", i)
        # print("A[i]=", At[i])
        # print("len(At[i]=)", len(At[i]))


    for i in range(lenV):
        if i != 0:
            # print ("i=",i)
            for t in range(lenMS):
                # print("t=", t)
                temp=[]
                for j in preV[i]:
                    # 将前驱顶点 j 在执行环境 t 中的调度时间（存储在 At[j][t] 中）添加到 temp 列表中。
                    temp+=At[j][t]
                '''
                temp=list(set(temp))：将 temp 列表中的重复值去除，以确保唯一性。
                set(temp)将列表转换成集合，集合中不存在重复元素
                list(set(temp))再将集合set(temp)转换成列表的形式，
                来确保只保留唯一的元素。
                '''
                temp=list(set(temp))
                # try:
                # 将 temp 列表的内容加到 At[i][t] 中，表示顶点 i 在执行环境 t 中的调度时间。
                At[i][t]+=temp
                # 去掉重复的调度时间
                At[i][t]=list(set(At[i][t]))
                # except(IndexError):
                #     print("the node is %d,%d"%(i,t))
                # print "temp=",temp
    # print "At=",At
    # print "It=",It
    # 外层循环从 lenV-1 递减到1，逆序遍历。
    for i in range(lenV-1,0,-1):
        for j in preV[i]:
            for t in range(lenMS):
                # 将前驱顶点 j 在执行环境 t 中的 It 值与顶点 i 在执行环境 t 中的 At 值的交集加到 It[j][t] 中。
                It[j][t]+=list(set(It[i][t])&set(At[j][t]))
                # 确保It[j][t]时间值的唯一性
                It[j][t] = list(set(It[j][t]))
    # print "It=",It
    return It


def findRT(task,MS):
 # chV=randomDAG.findpcoDAG().findchild(task.V,task.E)
    # paV = randomDAG.findpcoDAG().findpa(task.V, task.E)

 # 调用 randomDAG 模块中的 findpcoDAG 对象的 findnorelationV 函数，
 # 用于查找任务中没有关联的顶点，并将结果存储在 paraV 变量中。
    paraV = randomDAG.findpcoDAG().findnorelationV(task.V, task.E, task.P)
    # 包含任务在不同执行环境中调度时间的数据结构
    It=schedulAlgorithm2(task,paraV,MS)
    # print "It=",It
    # Inter=findInter(task,subSet,chV,paV)

    # lenV表示任务中的顶点数量。
    lenV=len(task.V)
    # E表示任务的边集合。
    E=task.E
    # FGtemp是一个二维列表，用于存储中间结果。
    FGtemp=[[] * lenV for i in range(lenV)]
    # RT是一个列表，用于存储每个顶点的调度时间。
    RT=[0] * lenV
    # preV是一个列表，初始化为一个包含一个空列表的列表。
    preV=[[]]
    # Ittemp 是 It 的深度复制，以备后用。
    Ittemp=copy.deepcopy(It)
    # Intertemp=Inter[:]
    # 计算出每个节点的直接父亲节点并存储在preV的列表中
    # 不从0开始是因为0不存在前驱结点
    for i in range(1, lenV):  # 每个结点的直接父亲节点parVset
        temp = []
        for j in range(0, i):
            # 检查是否存在一条从顶点 j 到顶点 i 的有向边，这表示顶点 j 是顶点 i 的前驱顶点。
            if (j, i) in E:
                temp.append(j)
        # 将填充好的 temp 列表添加到 preV 列表中，
        # 以表示顶点 i 的所有直接父亲节点（前驱顶点） 如（ 1 ，5 ）、（ 2 ，5 ）。
        preV.append(temp)
    # print "preV=",preV
    # print "FGtemp=",FGtemp
    for i in range(lenV):
        # print "i=",i
        # 初始化变量 wi：当前顶点 i 的最早开始时间
        wi=0
        # rt表示当前顶点i的最早完成时间
        rt=0
        # Intertmp=[]
        # cor=[[]* len(MS) for n in range(len(MS))]
        # 遍历到第一个节点时，为 FGtemp 列表中的第一个元素（即第一个顶点）创建一个子列表，
        # 该子列表包含任务的执行时间 task.V[i]，一个空列表 []，以及当前顶点的索引 i。
        if i == 0:
            FGtemp[i]=[[task.V[i],[],i]]
            # 将当前顶点的最早完成时间初始化为顶点的执行时间
            RT[i]=task.V[i]
        else:
            # 遍历前驱顶点列表preV[i]的前驱节点j
            for j in preV[i]:
                # print "j=",j
                # print FGtemp[j]
                # 遍历前驱结点j在FGtemp[j]的值k
                for k in FGtemp[j]:
                    wi = 0
                    rt = 0
                    temp = [0, [], i]
                    # print "k=",k
                    # 计算当前节点i最早完成时间wi = 当前节点的执行时间 task.V[i]+ 前驱结点的最早完成时间k[0]
                    wi=task.V[i] + k[0]
                    # print "wi=",wi
                    # 创建一个二维列表存储当前顶点i和前驱顶点j的相关信息，大小由MS决定
                    cor = [[] * len(MS) for n in range(len(MS))]

                    for t in range(len(MS)):
                        # cor中元素设置成It[i][t] + Ittemp[j][t]，并去除重复的值
                        cor[t]=list(set(It[i][t]+Ittemp[j][t]))
                    # print "cor=",cor
                    #  z是执行环境 t 的权重，
                    #  rt是当前顶点 i 的最早完成时间。
                    z = 0
                    for m in range(len(cor)):
                        y = 0
                        if cor[m]:
                            # print cor[m]
                            # 表示在当前执行环境 m 中所有相关任务的执行时间之和。
                            x = 0
                            for n in cor[m]:
                                x += task.V[n]
                            # print "x=",x
                            # print MS[m]
                            # print "x=",x
                            # 计算任务在当前执行环境 m 中的平均执行时间，即任务总执行时间除以执行环境的权重 MS[m]。
                            y = x / MS[m]
                            # print "y=",y
                        # 计算所有执行环境的权重累积
                        z += y
                        # print "z=",z
                    # 计算当前顶点 i 的最早完成时间 rt，它等于最早开始时间 wi 加上所有执行环境的权重累积 z
                    rt = wi + z
                    # print "rt=",rt
                    # 当 rt 大于 RT[i]，表示计算的最早完成时间更早
                    if rt > RT[i]:
                        Ittemp[i] = cor
                        FGtemp[i] = [[wi, Ittemp[i], i]]
                        RT[i] = rt
            # print "It=",It
    # print "FGtemp=", FGtemp
    # print "RT=",RT
    FG=[]
    for i in range(lenV):
        FG.append([RT[i],FGtemp[i]])
    # for i in range(0, lenV):
    #     print("FG[%d]=", i)
    #     print(FG[i])
    # print("FG=",FG)
    # 函数返回 FG 列表中最后一个元素的第一个值，即任务的最终调度时间
    return FG[len(FG)-1][0]

if __name__ == '__main__':
    # for n in range(50):
        # task=RandomDAGtask(5,30,40,1000,0.2,7
        # T=task.createtask(0)
        # paV=findpcoDAG().findpa(T.V,T.E)
        # chV=findpcoDAG().findchild(T.V,T.E)
        # paraV=findpcoDAG().findnorelationV(T.V,T.E,T.P)

    v = [1, 3, 4, 5, 6, 10, 1, 11, 15, 2, 1]
    e = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 10), (5, 10), (6, 8), (7, 9),
         (8, 10), (9, 10)]
    type = [1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1]
    MS = [2, 3]
    print (len(MS))
    print (len(v))
    print (len(e))
    T=randomDAG.DAGtask(v,e,100,100,0,type)
    rt=findRT(T,MS)
    print (rt)
