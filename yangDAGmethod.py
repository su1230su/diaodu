import time

from scipy.optimize import linprog
from pulp import LpProblem, LpVariable, LpMaximize, LpMinimize, LpStatus, value, LpContinuous

import generate.generate.randomDAG
from generate.generate import randomDAG
import copy
import time



def refinefaV(task):
    """
    函数，用于计算给定任务的父变量集合。
    参数:
    - task: 一个包含变量集合V和边集合E的任务对象。
    返回值:
    - faV: 一个列表，包含每个变量在其依赖关系中的父变量集合。
    """
    # 查找给定任务的父母变量集合
    anceV= randomDAG.findpcoDAG().find_ancestors(task.V, task.E)
    #anceV = randomDAG.findpcoDAG().findpa(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            # 构建每个变量的前置变量集合
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)

    # 复制前置变量集合，用于后续操作
    faV=copy.deepcopy(preV)
    for i in range(0,lenV):
        for u in preV[i]:
            for v in preV[i]:
                # 移除在anceV中查找不到的u，即不是真正父变量的变量
                if v !=u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break
    return faV

def cal_wcets(task, s, ):
    """
    计算指定优先级任务的最坏情况执行时间（WCET）
    参数:
    - task: 一个包含任务信息的对象，必须有.V（任务执行时间列表）和.P（任务优先级列表）属性
    - s: 指定的优先级
    返回值:
    - WT: 指定优先级任务的总执行时间
    - maxv: 指定优先级任务中的最大执行时间
    """
    lenV = len(task.V)  # 获取任务执行时间列表的长度
    type = task.P  # 获取任务优先级列表
    WT = 0  # 初始化指定优先级任务的总执行时间为0
    maxv = 0  # 初始化指定优先级任务中的最大执行时间为0

    # 遍历任务执行时间列表，找出指定优先级的任务并累加其执行时间
    for i in range(lenV):
        if task.P[i] == s:  # 如果当前任务的优先级与指定优先级相等
            WT = WT + task.V[i]   # 累加该任务的执行时间
            if maxv < task.V[i]:  # 更新最大执行时间
                maxv = task.V[i]
    return WT, maxv


# def findRT(task, Ms,U):
#     """
#     参数:
#     - task: 一个包含任务边（E）和顶点（V）以及其它属性（如P）的任务对象。
#     - Ms: 一个列表，包含了每个任务的优先级。
#
#     返回值:
#     - 计算得到的最迟完成时间。
#     """
#     lenV = len(task.V)  # 顶点的数量
#     E = task.E  # 任务之间的边集合
#     # 初始化release offset和R数组
#     rt = [0 * lenV for i in range(lenV)]
#     R = [0 * lenV for i in range(lenV)]
#     preV = refinefaV(task)  # 精细化前置任务列表
#     for i in range(lenV):
#         corty = task.P[i]  # 当前任务的优先级
#         mk = Ms[corty-1]  # 获取当前任务的优先级系数
#         wcets = cal_wcets(task, corty,U)  # 计算当前任务的最坏情况执行时间（WCET）
#         if i == 0:
#             # 对于源节点（起始任务），初始化完成时间为0
#             rt[0] = 0
#             Rt = (1 / mk) * wcets[0] + wcets[1] + task.V[i] * ((mk - 1) / mk)
#             R[i] = Rt
#         else:
#             maxrt = 0
#             # 计算所有前置任务中最晚的完成时间
#             for j in preV[i]:
#                 curt = rt[j] + R[j]
#                 if maxrt < curt:
#                     maxrt = curt
#             rt[i] = maxrt  # 当前任务的最晚开始时间
#             if task.V[i] == 0:
#                 Rt = 0
#             else:
#                 Rt = (1 / mk) * wcets[0] + wcets[1] + task.V[i] * ((mk - 1) / mk)
#             R[i] = Rt
#     # 返回最终的最迟完成时间
#     return R[lenV-1] + rt[lenV-1]





def cal_maxwcet(Tsets, Ms):
    """
    计算每个任务集的最大工作周期（Maximum Worst Case Execution Time, WCET）。
    参数:
    Tsets -- 一个包含多个任务集的列表，每个任务集包含多个任务，每个任务有优先级和执行时间。
    Ms -- 一个整数列表，表示每个任务的最高优先级（从1开始）。

    返回值:
    mwcet -- 一个包含每个任务集的最大执行时间的列表。
    """
    mwcet = []  # 初始化用于存储最大WCET的列表

    lenp = len(Ms)  # 获取Ms的长度
    lens = len(Tsets)  # 获取Tsets的长度
    # 遍历所有任务的最高优先级
    for i in range(lenp):
        pv = []  # 初始化存储当前优先级任务执行时间的列表
        # 遍历所有任务集
        for j in range(0, lens):
            lenj = len(Tsets[j].V)  # 获取当前任务集中的任务数量
            # 遍历当前任务集中的所有任务
            for k in range(lenj):
                # 如果任务的优先级与当前遍历的优先级相等，则将执行时间添加到pv列表中
                if Tsets[j].P[k] == i + 1:
                    pv.append(Tsets[j].V[k])
        # 计算并存储当前优先级任务的最大执行时间
        mwcet.append(max(pv))
    return mwcet



def cal_RV(Tsets, Ms):
    """
    计算任务相对截止时间（Relative Deadline, RV）。
    参数:
    Tsets: 包含多个任务集的列表，每个任务集包含多个任务节点，每个任务节点包含周期（Ti）、执行时间矩阵（V）和处理器亲和性（P）。
    Ms: 一个包含多个处理器最大执行时间的列表，列表索引与处理器编号一致。
    返回值:
    RT: 一个二维列表，包含每个任务节点的响应时间。
    """
    # 初始化相关变量
    lens = len(Tsets)

    U = []

    # 为每个任务节点分配相对截止时间，并初始化响应时间和利用率
    mwcet = cal_maxwcet(Tsets, Ms)
    for i in range(lens):
        leni = len(Tsets[i].V)
        Ui = []
        for j in range(0, leni):
            # 相对截止时间初始化
            # 计算利用率
            Ui.append(Tsets[i].V[j] / Tsets[i].Ti)
        U.append(Ui)

    lenp = len(Ms)  # 获取Ms的长度
    tt_U = []
    tt_TD = []
    # 计算每个处理器的总利用率
    for i in range(lenp):
        ttup = 0
        ttdt = 0
        for j in range(lens):
            leni = len(Tsets[j].V)
            for k in range(leni):
                if Tsets[j].P[k] == i + 1:
                    ttup = ttup + U[j][k]
                    ttdt = ttdt + U[j][k] * (Tsets[j].Ti - Tsets[j].Di)

        tt_U.append(ttup)
        tt_TD.append(ttdt)

    return U ,tt_U, tt_TD







def LP_findrt(task, Ms, wcet, U, tt_TD):
    # 定义线性规划问题
    prob = LpProblem("ResponseTimeCalculation", LpMinimize)
    # 定义变量

    lenV = len(task.V)  # 顶点的数量
    D = [LpVariable(f"d_{i}", lowBound=0) for i in range(lenV)]
    O = [LpVariable(f"o_{i}") for i in range(lenV)]
    R = [LpVariable(f"r_{i}") for i in range(lenV)]


    # 设置变量 D 的初始值为 当前任务的周期
    for i in range(lenV):
        D[i].varValue = task.Ti
        # print(f"初始化的截止期的值是：{value(D[i])}")
    # print(D)
    O[0] = 0
    # print(O[0])
    #
    # print(D)
    # print(O)
    # print(R)
    # 目标函数变量
    Y = LpVariable("Y", lowBound=0)



    #  添加目标函数
    prob += Y

    preV = refinefaV(task)

    # 添加约束条件
    for i in range(lenV):
        # 截止期约束
        prob += D[i] - task.Ti <= 0

        # 偏移量约束
        for k in preV[i]:
            prob += O[i] >= O[k] + R[k]
        # 相对响应时间约束



        p = task.P[i] - 1
        mk = Ms[p]

        prob += R[i] == (1/mk) * (D[i] * U[p] + tt_TD[p]) + wcet[p] + (mk - 1)/mk * task.V[i]
        #prob += R[i] == (D[i] * result[1][p] + result[2][p]) / mk + result[0][p] + (mk - 1) * task.V[i] / mk

        # 目标函数约束
        prob += Y >= O[i] + R[i]

    # 求解
    status = prob.solve()


    # print(f"Status: {prob.status}")
    # print(f"Objective Value: {prob.objective.value()}")
    # print(f"Status: {LpStatus[status]}")
    # print(f"Objective Value: {value(prob.objective)}")
    # print(D)
    # print(O)
    # print(R)
    # 输出最优解对应的各个变量的值
    # for i in range(lenV):
    #     print(f"D_{i}: {value(D[i])}")
    #     print(f"O_{i}: {value(O[i])}")
    #     print(f"R_{i}: {value(R[i])}")
    # print(f"Y: {value(Y)}")

    return prob.objective.value()



def findRTs(Tsets, Ms):
    """
    计算并返回每个任务集的最短响应时间和计算过程的总时间。
    参数:
    Tsets: 一个包含多个任务集的列表，每个任务集是一个有向无环图(DAG)的表示，其中每个节点代表一个任务。
    Ms: 与Tsets对应的每个任务集的绝对截止时间的列表。
    返回值:
    一个包含两个元素的列表，第一个元素是每个任务的最短响应时间列表，第二个元素是计算过程的总时间。
    """
    RT = []
    t1 = time.time()
    wcet =  cal_maxwcet(Tsets, Ms)
    uu= cal_RV(Tsets, Ms)
    for task in Tsets:

        rt = LP_findrt(task, Ms, wcet, uu[1],uu[2])
        RT.append(rt)
    for task in Tsets:
        task_index = Tsets.index(task)
        # 需要更改对于是否超过截止期的判断
        if RT[task_index] > task.Ti:
            RT[task_index] = 0

    t2 = time.time()
    finish_time = t2 - t1
    return RT, finish_time










# def findRTs(Tsets, Ms):
#     """
#     计算并返回每个任务集的最短响应时间和计算过程的总时间。
#     参数:
#     Tsets: 一个包含多个任务集的列表，每个任务集是一个有向无环图(DAG)的表示，其中每个节点代表一个任务。
#     Ms: 与Tsets对应的每个任务集的绝对截止时间的列表。
#     返回值:
#     一个包含两个元素的列表，第一个元素是每个任务的最短响应时间列表，第二个元素是计算过程的总时间。
#     """
#     timetotal = 0  # 初始化总时间
#     t1 = time.time()  # 记录开始时间
#     lens = len(Tsets)  # 获取任务集的数量
#
#
#     # 计算并分配每个节点的相对截止时间
#     RT = cal_RV(Tsets, Ms)
#     # print("@@@@@@@@@@@")
#     # print(RT)
#     # print("@@@@@@@@@@@")
#
#     fRT = []  # 初始化最终的响应时间列表
#
#     # 遍历每个任务集
#     for i in range(lens):
#         rtset = 0
#         leni = len(Tsets[i].V)  # 获取当前任务集的节点数量
#         RTi = []  # 初始化存储当前任务集响应时间的列表
#         rti = []  # 初始化用于计算父节点响应时间的列表
#         # 修改父节点信息
#         fav = refinefaV(Tsets[i])
#         # 遍历当前任务集的每个节点
#         for j in range(0, leni):
#             if j == 0:
#                 rt = RT[i][j]
#                 rti.append(0)
#                 RTi.append(rt)
#             else:
#                 rtj = 0
#                 # 计算每个父节点的响应时间并找到最大值
#                 for k in fav[j]:
#                     rtk = rti[k] + RT[i][k]
#                     if rtj < rtk:
#                         rtj = rtk
#                 rti.append(rtj)
#                 rt = rtj + RT[i][j]
#                 RTi.append(rt)
#             rtset = max(RTi)
#         fRT.append(rtset)
#
#     for task in Tsets:
#         task_index = Tsets.index(task)
#         if fRT[task_index] > task.Di:
#             fRT[task_index] = 0
#         # fRT.append(RTi)
#
#     t2 = time.time()  # 记录结束时间
#     timetotal = t2 - t1  # 计算总时间
#
#     return [fRT, timetotal]












if __name__ == '__main__':
    v = [200,380,100,300]
    e = [(0, 1), (0, 2), (1, 3),(2,3)]
    type = [1,2,1,1]

    T1 = randomDAG.DAGtask(v, e, 500, 500, 0, type)
    # rt1=findRT(T,MS)
    # print("rt1=", rt1)
    # v = [133, 16, 83, 197, 78, 0]
    # e = [(0, 1), (1, 2), (1, 4), (2, 3), (3, 5), (4, 5)]
    # type = [1, 2, 2, 1, 1, 1]
    # T2 = randomDAG.DAGtask(v, e, 1000, 1000, 0, type)
    #
    # v = [73,242,5]
    # e = [(0, 1), (1, 2), (2, 3)]
    # type = [1, 2, 1]
    # T3 = randomDAG.DAGtask(v, e, 1000, 1000, 0, type)
    #
    # Tsets=[T1,T2,T3]

    Tsets = [T1]
    MS = [2, 2]
    rt = findRTs(Tsets, MS)
    print("rt=", rt)

