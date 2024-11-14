from __future__ import division
import random
import sys
import time

import yangDAGmethod

from generate.generate import randomDAG
import Experiment_rt_Sun_path
import calculate_ntuple
import multidag_Sun_path

import datetime


def save_in_file(tasknum, tasks, turn):
    current_time = datetime.datetime.now()
    file = open("model.txt", 'a+')
    file.write(f'====================任务集{turn}共有{tasknum}个任务=====================\n')
    file.write(f"当前的时间{current_time}")
    i = 0
    for task in tasks:
        file.write(f"#################")
        file.write(f"----------task{i}:\n")
        file.write(f"V:\t{task.V}\n")
        file.write(f"edges:\t{task.E}\n")
        file.write(f"deadline:\t{task.Di}\n")
        file.write(f"period:\t{task.Ti}\n")
        file.write(f"type:\t{task.P}\n")
        file.write(f"typeddag:\t{task.typeddag}\n")
        file.write(f"name:\t{task.name}\n")
        file.write(f"critical_path:\t{task.critical_path}\n")
        file.write(f"任务集的截至期：{task.Di}")
        file.write(f"#################")
        i += 1
    file.close()



def save_in_file2(tasknum, task, turn, n1,n2):
    current_time = datetime.datetime.now()
    file = open("model1.txt", 'a+')
    file.write(f'=============当前的fp的响应时间{n1}=====================\n')
    file.write(f'=============当前的global_fp的响应时间{n2}=====================\n')
    file.write(f'=============当前的是第{turn}轮，要存的是任务是：=====================\n')
    file.write(f"当前的时间{current_time}")

    file.write(f"当前正在保存 it is saved\n")

    file.write(f"#################\n")
    file.write(f"V:\t{task.V}\n")
    file.write(f"edges:\t{task.E}\n")
    file.write(f"deadline:\t{task.Di}\n")
    file.write(f"period:\t{task.Ti}\n")
    file.write(f"type:\t{task.P}\n")
    file.write(f"typeddag:\t{task.typeddag}\n")
    file.write(f"name:\t{task.name}\n")
    file.write(f"critical_path:\t{task.critical_path}\n")
    file.write(f"任务集的{task.Di}\n")
    file.write(f"#################\n")

    file.close()

def check_0(SUCCESS, arr):
    # 数组定义
    R = arr

    # 初始化一个变量来表示是否存在0
    has_zero = False

    # 遍历数组R，检查是否存在0
    for num in R:
        if num == 0:
            has_zero = True
            break

    # 如果存在0，则输出"存在0"，否则输出"不存在0"
    if has_zero:
       print("存在0")
    else:
        SUCCESS += 1

    return SUCCESS


def EXPERIMENT(tasknum, Umin, Umax, Tmin, Tmax, Ndagmin, Ndagmax, Msmin, Msmax, Pr, numP, TURN, options, task_save):

    N = 0

    R = []
    TIME = 0
    SUCCESS = 0
    ntuple = []


    R2 = []
    TIME2 = 0
    SUCCESS2 = 0
    ntuple2 = []



    imp = 0

    while N < TURN:

        N = N + 1
        # print(N)
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

        # 保存任务集信息
        if (task_save):
            save_in_file(tasknum, task, N)

        # 只算NTUPLE 数量部分
        if(options[0]):
            result = calculate_ntuple.suan_ntuple(task, MS)
            #print(result)
            for i in range(len(result)):
                ntuple.append(result[i])
        if (options[1]):
            result1 = calculate_ntuple.suan_ntuple1(task, MS)
            #print(result1)
            for i in range(len(result1)):
                ntuple2.append(result1[i])

    return [0, 0, 0, 0, 0, ntuple, ntuple2]





        # # 归一化计算部分
        # if (options[0]):
        #     # 处理
        #     # print(len(task[1].typeddag[0]))
        #     t0 = time.time()
        #     RESULT = multidag_Sun_path.get_set_R(task, MS)  ###################################可替换的接口。
        #     t1 = time.time()
        #
        #     # print("&&&&&&&&&&&&&&&&&&&&&")
        #     # print(RESULT)
        #     # print("&&&&&&&&&&&&&&&&&&&&&")
        #     R = RESULT[0]
        #     # TIME += RESULT[1]
        #     TIME += (t1 - t0)
        #     SUCCESS += RESULT[2]
        #     for i in range(len(RESULT[3])):
        #         ntuple.append(RESULT[3][i])
        #
        #
        # if (options[1]):
        #     # 处理
        #     # print(len(task[1].typeddag[0]))
        #     t2 = time.time()
        #     RESULT2 = multidag_Sun_path.get_set_R1(task, MS)  ###################################可替换的接口。
        #     t3 = time.time()
        #     # print("!!!!!!!!!!!!!!!!!!!!")
        #     # print(RESULT2)
        #     # print("!!!!!!!!!!!!!!!!!!!!")
        #
        #     R2 = RESULT2[0]
        #     # TIME2 += RESULT2[1]
        #     TIME2 += (t3 - t2)
        #     SUCCESS2 += RESULT2[2]
        #     for i in range(len(RESULT2[3])):
        #         ntuple2.append(RESULT2[3][i])
        #
        # for i in range(len(R)):
        #     if R[i] < R2[i]:
        #         n1 = R[i]
        #         n2 = R2[i]
        #         save_in_file2(tasknum, task[i], N, n1 ,n2)
        #
        # # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # # print(f"当前的SUCCESS是：{SUCCESS}，当前的SUCCESS2是：{SUCCESS2}")
        # for i in range(len(R)):
        #     if R[i] != 0:
        #         imp += (R[i] - R2[i]) / R[i]
        #     elif R[i] == 0 and R2[i] != 0:
        #         imp += 1
        #     elif R[i] == 0 and R2[i] == 0:
        #         imp += 0
        #
        # print(f"当前的imp是：{imp}")
        # print(f"当前进行的是第:{N}次")
        # print(f"初始fp的数据R数组{R}")
        # print(f"初始fp花费的时间{TIME}")
        # print(f"初始fp计算的ntuple是：{ntuple}")
        # print(f"global-fp的数据R数组{R2}")
        # print(f"global-fp花费的时间{TIME2}")
        # print(f"global-fp计算的ntuple是：{ntuple2}")
        #
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    #     print("+++++++++++++++++++++++++++++++++++++++++++")
    #     # global-edf算法最终结果优化
    #     if (options[0]):
    #         # 处理
    #         # print(len(task[1].typeddag[0]))
    #         # RESULT=multidag_Sun_path.get_set_R(task,MS)
    #         RESULT = multidag_Sun_path.globaledf(task, MS)
    #         R = RESULT[0]
    #         print("===========================================================")
    #         print(R)
    #         print("===========================================================")
    #         TIME += RESULT[1]
    #         SUCCESS = check_0(SUCCESS, R)
    #         # for element in R:
    #         #     if element == 0:
    #         #         SUCCESS +=0
    #         # SUCCESS += 1
    #
    #     if (options[1]):
    #
    #         # RESULT2 = yangDAGmethod.findRTs(task, MS)
    #         RESULT2 = yangDAGmethod.findRTs(task, MS)
    #         R2 = RESULT2[0]
    #         print(R2)
    #         print("===========================================================")
    #         TIME2 += RESULT2[1]
    #         SUCCESS2 = check_0(SUCCESS2, R2)
    #         # for element in R2:
    #         #     if element == 0:
    #         #         SUCCESS2 += 0
    #         # SUCCESS2 += 1
    #
    # print(f"当前的SUCCESS是：{SUCCESS}，当前的SUCCESS2是：{SUCCESS2}")



    # 只算NTUPLE 数量部分才去掉
    # TIME = round(TIME, 2)
    # RATE = round(SUCCESS / TURN, 2)
    # # minus = random.uniform(1.2, 1.5)
    # minus = 1
    # RATE_fake = round((SUCCESS2 / TURN) / minus, 2)
    # TIME_fake = round(TIME2 / minus, 2)
    # # if (options == [1, 0]):
    # #     return [RATE, TIME]
    # # elif (options == [0, 1]):
    # #     return [RATE_fake, TIME_fake]
    # # elif (options == [1, 1]):
    # #     print("yes")
    # #     print(RATE, TIME, RATE_fake, TIME_fake)
    # #     return [RATE, TIME, RATE_fake, TIME_fake]
    #
    # # 归一化计算
    # imp = imp /tasknum
    #
    # # print("yes")
    # # print(RATE, TIME, RATE_fake, TIME_fake, imp)
    # return [RATE, TIME, RATE_fake, TIME_fake, imp, ntuple, ntuple2]


def sepU(tasknum, Umin, Umax):
    # Usum=random.uniform(Umin,Umax)
    # # print(Usum)
    # for i in range(1, tasknum):
    #     Uleft = Usum * random.uniform(0, 1) ** (1 / (tasknum - i))
    #     U.append(Usum - Uleft)
    #     Usum = Uleft
    # U.append(Usum)
    # random.shuffle(U)

    # 原版
    U = []
    Umin /= tasknum
    Umax /= tasknum
    for i in range(0, tasknum):
        U.append(random.uniform(Umin, Umax))

    return U


if __name__ == '__main__':
    # print(EXPERIMENT_numP())
    print(sepU(10, 9, 10))
    # print(10 % 1.15)

    # print(random.sample(list(range(0,20)),10))
    # temp=[]
    # for i in range(10):
    #     temp.append([])
    # print(temp)
    # temp[3].append(111)
    # temp[3].append(1999)
    # temp[1].sort(reverse=True)
    # temp[3].sort(reverse=True)
    #
    # print(temp)
    #
    # print([[0]for i in range(5)])
    # print([]+[1,2,3]+[[1],2,3])
