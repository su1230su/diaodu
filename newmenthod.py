import randomDAG  # 假设存在名为 randomDAG 的模块
import copy


# 定义函数 refinefaV，用于计算每个节点的父节点集合
def refinefaV(task):
    anceV = randomDAG.findpcoDAG().findpa(task.V, task.E)
    preV = []
    lenV = len(task.V)

    # 计算每个节点的直接父节点集合
    for i in range(lenV):
        temp = []
        for j in range(i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)

    # 修正父节点集合，保留节点间真正的父子关系
    faV = copy.deepcopy(preV)
    for i in range(lenV):
        for u in preV[i]:
            for v in preV[i]:
                if v != u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break

    return faV


# 定义函数 findRT，用于计算任务的最长运行时间
def findRT(task, MS, TS):
    chV = randomDAG.findpcoDAG().findchild(task.V, task.E)

    paraV = randomDAG.findpcoDAG().findnorelationV(task.V, task.E, task.P)

    lenV = len(task.V)

    E = task.E
    FGtemp = [[] for _ in range(lenV)]
    mart = 0
    preV = refinefaV(task)

    # TS 初始化
    TS = [(0, set(), 0)]

    for i in range(lenV):
        if i == 0:
            # 如果是源节点，初始化 FGtemp[i]
            rt = task.V[i]
            nn_set = [-1 for _ in range(len(MS))]
            ty_i = task.P[i] - 1
            nn_set[ty_i] = i
            FGtemp[i] = [[rt, nn_set]]
        else:
            for j in preV[i]:
                for k in FGtemp[j]:
                    wi = task.V[i] + k[0]
                    tmpp = []
                    cori = task.P[i] - 1
                    scv = k[1][cori]
                    tmset = copy.deepcopy(k[1])

                    if scv != -1:
                        tmpp = list(set(paraV[i]) - set(paraV[scv]))
                    else:
                        tmpp = paraV[i]

                    lenw = sum(task.V[p] for p in tmpp)
                    rt = wi + lenw / MS[cori]

                    tmset[cori] = i
                    ntuple = [rt, tmset]

                    lenFg = len(FGtemp[i])

                    if lenFg == 0:
                        FGtemp[i].append(ntuple)
                    else:
                        flagst = 1
                        for fgn in range(lenFg):
                            # 添加判断条件，检查是否需要添加新的元组到TS中
                            flagds1, flagds2 = find_diff(ntuple, FGtemp[i][fgn], paraV, chV, len(MS))
                            cond1 = not any(
                                (v_prime, Delta_star, R_tilde_star) in TS for (v_prime, Delta_star, R_tilde_star) in TS)
                            cond2 = any((v_prime, Delta_star, R_tilde_star) >= (v_prime, Delta_prime, R_tilde_prime) for
                                        (v_prime, Delta_prime, R_tilde_prime) in TS if v_prime in preV[i])
                            cond3 = (v_prime, Delta_star, R_tilde_star).Type != (
                            v_prime, Delta_prime, R_tilde_prime).Type

                            if ntuple == FGtemp[i][fgn][1]:
                                flagst = 0
                                if rt > FGtemp[i][fgn][0]:
                                    FGtemp[i][fgn][0] = rt
                            elif flagds1 == 1:
                                flagst = 0
                                if cond1 or cond2 or cond3:
                                    add_to_TS(TS, v_prime, Delta_star, R_tilde_star)  # 使用之前定义的添加到 TS 的函数
                                FGtemp[i][fgn] = ntuple

                        if flagst == 1:
                            if cond1 or cond2 or cond3:
                                add_to_TS(TS, v_prime, Delta_star, R_tilde_star)  # 使用之前定义的添加到 TS 的函数
                            FGtemp[i].append(ntuple)

    # 获取最长运行时间
    rtv = [k[0] for k in FGtemp[lenV - 1]]

    if len(rtv) != 0:
        mart = max(rtv)

    RT = mart
    return RT, TS


# 定义函数 find_diff，用于比较两个节点集合的差异性
def find_diff(ntuple, ntuple2, paraV, chV, numP):
    flagds1 = 0
    flagds2 = 0

    for tmpv in range(numP):
        if ntuple[1][tmpv] != ntuple2[1][tmpv]:
            if ntuple[0] == ntuple2[0]:
                tmpminV = ntuple2[1][tmpv]
                tmpmaxV = ntuple[1][tmpv]
                if tmpminV == -1:
                    flagds2 = 1
                if tmpmaxV == -1:
                    flagds1 = 1
                if tmpmaxV != -1 and tmpminV != -1:
                    tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                    tmp1 = [v for v in paraV[tmpminV] if v in chV[tmpmaxV]]
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
                tmpminV = 0
                tmpmaxV = 0
                if ntuple[0] > ntuple2[0]:
                    tmpminV = ntuple2[1][tmpv]
                    tmpmaxV = ntuple[1][tmpv]
                    if tmpmaxV == -1:
                        flagds1 = 1
                    if tmpminV == -1:
                        flagds1 = 0
                        break
                    if tmpmaxV != -1 and tmpminV != -1:
                        tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                        if len(tmp) == 0:
                            flagds1 = 1
                        else:
                            flagds1 = 0
                            break
                else:
                    tmpminV = ntuple[1][tmpv]
                    tmpmaxV = ntuple2[1][tmpv]
                    if tmpmaxV == -1:
                        flagds2 = 1
                    if tmpminV == -1:
                        flagds2 = 0
                        break
                    if tmpmaxV != -1 and tmpminV != -1:
                        tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                        if len(tmp) == 0:
                            flagds2 = 1
                        else:
                            flagds2 = 0
                            break

    return flagds1, flagds2


# 定义函数 add_to_TS，用于向 TS 中添加新的元组
def add_to_TS(TS, v_prime, Delta_star, R_tilde_star):
    # 判断是否已存在相同节点的元组
    if not any((v_prime, Delta_star, R_tilde_star) == (v, Delta, R_tilde) for (v, Delta, R_tilde) in TS):
        TS.append((v_prime, Delta_star, R_tilde_star))




# 示例数据
v = [0, 6.228144750378959, 11.854393845710266, 33.18986864032895, 16.72314913959317, 36.57983842554995,
     6.883061515922677, 12.690585350042639, 41.412152862200315, 6.830296739334428, 5.889877821288273,
     6.798050263083553, 17.30527470227729, 17.172379867494982, 47.21991597999763, 12.506874423001094,
     71.42694037408671, 0.33712161355116677, 26.263486368933634, 60.964537593647975, 0.4819847990607983,
     6.317877785652723]
e = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 7), (0, 9), (0, 20), (1, 6), (2, 8), (2, 16), (3, 10), (3, 14),
     (4, 5), (5, 10), (6, 15), (7, 10), (7, 11), (7, 14), (8, 21), (9, 18), (10, 13), (11, 12), (12, 13),
     (12, 18), (13, 15), (13, 19), (14, 21), (15, 21), (16, 17), (17, 21), (18, 21), (19, 21), (20, 21)]
type = [3, 2, 3, 1, 3, 2, 3, 4, 2, 3, 4, 5, 5, 2, 4, 2, 1, 5, 1, 2, 3, 2]
MS = [2, 3, 4, 5, 6]

# 创建任务实例
T = randomDAG.DAGtask(v, e, 100, 100, 0, type)

# 调用 findRT 函数
RT, TS = findRT(T, MS, [])
print("最长运行时间:", RT)
print("TS 元组:", TS)
