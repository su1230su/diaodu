from __future__ import division
import math
import copy
import sys

from generate.path import Experiment_rt_Sun_path

sys.path.append('E://NEU/NEU 4_2（研究生课）/毕业设计/毕业设计代码/generate/')
from generate.generate import randomDAG
# import moreDAG
import random
import highprio_path
import time

# def sepU(tasknum, Umin, Umax):
#     U = []
#
#     # Usum=random.uniform(Umin,Umax)
#     # # print(Usum)
#     # for i in range(1, tasknum):
#     #     Uleft = Usum * random.uniform(0, 1) ** (1 / (tasknum - i))
#     #     U.append(Usum - Uleft)
#     #     Usum = Uleft
#     # U.append(Usum)
#     # random.shuffle(U)
#
#     Umin /= tasknum
#     Umax /= tasknum
#     for i in range(0, tasknum):
#         U.append(random.uniform(Umin, Umax))
#
#     return U
#
#
# tasknum = 1
# Umax = 8
# Umin = 10
# numP = 5
# Msmin = 3
# Msmax = 5
#
# Tmin = 100
# Tmax = 1000
# Pr = 0.1
# Ndagmin = 5
# Ndagmax = 10
# U = sepU(tasknum, Umin, Umax)
# # print(U)
#
#
# MS = Experiment_rt_Sun_path.devide_cores_dags(numP, Msmin, Msmax)  # 核数安排
# tmin = Tmin  # 随机生成dag的最小周期
# task = []
# for s in range(0, tasknum):  # 生成dag任务集
#     T = randomDAG.generate_DAG(Ndagmin, Ndagmax, tmin, Tmax, Pr, numP)
#     # u=random.uniform(Umin,Umax)
#     # print(U[s])
#     task.append(T.generate_DAG_task(U[s]))
#     # print(task[s].Ti)
#     tmin = task[s].Ti
#     # 找到当前的所有的前驱
# anceV = randomDAG.findpcoDAG().find_ancestors(task[0].V, task[0].E)
#
#
# stack =[]
#
#
# def DFS_path(graph, start, end, path):
#     t = path.copy()
#     path.append(start)
#     if start == end:
#         return [path]
#
#     paths = []  # 用于存储所有路径
#     for i in anceV[start]:  # 从起点开始，依次遍历每个点能到达的点
#         if i not in path:  # 如果这个点不在路径中的话，就将其作为新起点，进行递归
#             pn = DFS_path(graph, i, end, path)
#             # 递归完成后说明以该点为起点的所有路径都已经被添加到paths中
#             for p in pn:
#                 paths.append(p)
#             path = t.copy()
#             path.append(start)
#     return paths
#
#
# def Check(graph, s, e, path=[]):  # s起点，e终点
#     path = path + [s]
#     # print('path',path)   取消注释查看当前path的元素
#     if s == e:
#         # print('回溯')
#         return [path]
#
#     paths = []
#     # 存储所有路径
#     for node in anceV[s]:
#         if node not in path:
#             ns = Check(graph, node, e, path)
#             for n in ns:
#                 paths.append(n)
#     # print(paths,'回溯')
#     return paths
x = 0
k[5] = {-1, 0, 1, -1, 8}
for num in k:
    if num != -1:
        x += 1
print(x)




if __name__ == '__main__':
    tasknum = 1
    Umax = 8
    Umin = 10
    numP = 5
    Msmin = 3
    Msmax = 5

    Tmin = 100
    Tmax = 1000
    Pr = 0.1
    Ndagmin = 5
    Ndagmax = 10
    U = sepU(tasknum, Umin, Umax)
    # print(U)

    MS = Experiment_rt_Sun_path.devide_cores_dags(numP, Msmin, Msmax)  # 核数安排
    tmin = Tmin  # 随机生成dag的最小周期
    task = []
    for s in range(0, tasknum):  # 生成dag任务集
        T = randomDAG.generate_DAG(Ndagmin, Ndagmax, tmin, Tmax, Pr, numP)
        # u=random.uniform(Umin,Umax)
        # print(U[s])
        task.append(T.generate_DAG_task(U[s]))
        # print(task[s].Ti)
        tmin = task[s].Ti
        # 找到当前的所有的前驱
    anceV = randomDAG.findpcoDAG().find_ancestors(task[0].V, task[0].E)
    for i in range(0, len(task[0].V)):
        for j in anceV[i]:
            a=Check(task[0], j, i,[])
            print(a)