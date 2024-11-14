#coding=utf-8
from __future__ import division
import math
import random
import sys

import numpy as np


import copy
import pickle
import time
import makeRandom_Sun_path
import Experiment_path

def devide_cores(numP,Mmin,Mmax,hp_lessthan_m):
    MS=[]
    NHP=[]
    for i in range(numP):
        m = random.randint(Mmin, Mmax)
        MS.append(m)
        n_s = m - hp_lessthan_m  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        NHP.append(n_s)
    return [MS,NHP]
def devide_cores_randomhp(numP,Mmin,Mmax):
    MS=[]
    NHP=[]
    for i in range(numP):
        m = random.randint(Mmin, Mmax)
        MS.append(m)
        n_s = m - random.randint(1,math.floor(m/2))  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        NHP.append(n_s)
    return [MS,NHP]
def devide_cores_dags(numP,Mmin,Mmax):
    MS=[]
    # NHP=[]
    for i in range(numP):
        m = random.randint(Mmin, Mmax)
        MS.append(m)
        # n_s = m - random.randint(1,math.floor(m/2))  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        # NHP.append(n_s)
    return MS# [MS,NHP]

# 原版，7.4 由两个伪节点加入
# def devide_cores_dags(numP,Mmin,Mmax):
#     MS=[]
#     # NHP=[]
#     for i in range(numP):
#         m = random.randint(Mmin, Mmax)
#         MS.append(m)
#         # n_s = m - random.randint(1,math.floor(m/2))  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
#         # NHP.append(n_s)
#     return MS# [MS,NHP]



def devide_cores_oddodd(numP,Mmin,Mmax,hp_lessthan_m):
    MS=[]
    NHP=[]
    odd=0
    for i in range(numP):
        if ( i==(numP-1) and odd%2 ):#现在有奇数个，需要生成一个偶数
            m=1
            while(m%2):
                m = random.randint(Mmin, Mmax)
        elif ( i==(numP-1) and odd%2==0 ):
            m=0
            while((m%2)==0):
                m = random.randint(Mmin, Mmax)
        else:
            m = random.randint(Mmin, Mmax)
            if(m%2):
                odd+=1
        MS.append(m)
        n_s = m - hp_lessthan_m  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        NHP.append(n_s)
    return [MS,NHP]

def devide_cores_evenodd(numP,Mmin,Mmax,hp_lessthan_m):
    MS=[]
    NHP=[]
    odd=0
    for i in range(numP):
        if ( i==(numP-1) and odd%2 ):#现在有奇数个，需要生成一个奇数
            m=0
            while((m%2)==0):
                m = random.randint(Mmin, Mmax)
        elif ( i==(numP-1) and odd%2==0 ):
            m=1
            while(m%2):
                m = random.randint(Mmin, Mmax)
        else:
            m = random.randint(Mmin, Mmax)
            if(m%2):
                odd+=1
        MS.append(m)
        n_s = m - hp_lessthan_m  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        NHP.append(n_s)
    return [MS,NHP]
def devide_cores_HP(numP,Mmin,Mmax,Num_HP):
    MS = []
    NHP = []
    Sum_M=0
    left=0
    for i in range(numP):
        m = random.randint(Mmin, Mmax)
        MS.append(m)
        Sum_M+=m
    hp_lessthan_m=math.floor((Sum_M-Num_HP)/numP)
    left=Sum_M-(hp_lessthan_m*numP+Num_HP)
    #left=0
    for i in range(numP):
        n_s = MS[i] - hp_lessthan_m  # 暂时设置每种核上都恰好有核数个高优先级单节点任务，确保可以调度。
        NHP.append(n_s)
    if(left!=0):
        for i in range(left):
            if left>0:
                NHP[i]=NHP[i]+1
            else:
                NHP[i] = NHP[i] -1
    return [MS, NHP]

def seperate_u(Thps,umin,umax):
    length=len(Thps)
    USum=(random.uniform(umin,umax))*(length+1)
    U=[]

    for i in range(1, length+1):
        nextU = USum * random.uniform(0, 1) ** (1 / (length + 1 - i))
        U.append(USum - nextU)
        USum = nextU
        #USum=random.uniform(umin, umax)
        #U.append(USum)
    #USum = random.uniform(umin, umax)
    U.append(USum)
   # print ("u",U)
    for i in range(0,length):
        Thps[i][0]=Thps[i][1]*U[i]

    DAGu=U[length]

    return [Thps,DAGu]
def seperate_u_fixedU(Thps,u):
    length=len(Thps)

    for i in range(0,length):
        Thps[i][0]=Thps[i][1]*u

    DAGu=u

    return [Thps,DAGu]
def seperate_u_01range(Thps,u):
    length=len(Thps)

    for i in range(0,length):
        Thps[i][0]=Thps[i][1]*random.uniform(u-0.09999,u)


    DAGu=random.uniform(u-0.09999,u)

    return [Thps,DAGu]
def seperate_u_changed(Thps,u):
    length = len(Thps)
    USum = u * (length + 1)
    U = []

    for i in range(1, length + 1):
        nextU = USum * random.uniform(0, 1) ** (1 / (length + 1 - i))
        U.append(USum - nextU)
        USum = nextU
        # USum=random.uniform(umin, umax)
        # U.append(USum)
    # USum = random.uniform(umin, umax)
    U.append(USum)
    # print ("u",U)
    for i in range(0, length):
        Thps[i][0] = Thps[i][1] * U[i]

    DAGu = U[length]

    return [Thps, DAGu]
def seperate_u_2(Thps,umin,umax):
    length=len(Thps)
    USum=(random.uniform(umin,umax))*(length+1)
    U=[]
    U=makeRandom_Sun_path.random_float(length+1,(umin+umax)/2,umin,umax)

    #print ("u",U)
    for i in range(0,length):
        Thps[i][0]=Thps[i][1]*U[i]

    DAGu=U[length]

    return [Thps,DAGu]


# def run_all(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#
#     #tasknum实验
#     # ret=run_numTask(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#     #Ms实验
#     # ret=run_Ms(tasknum, Umin, Umax, Tmin, Tmax, Ndagmin, Ndagmax, Msmin, Msmax, Pr, numP, TURN)
#     #U实验
#     # ret=run_U(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#     #numP实验
#     # ret=run_numP(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#     #Ndag
#     ret=run_Ndag(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#     # Pr
#     # ret=run_Pr(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#     return ret
#
#
# def run_U(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_U = [[], [], [],'U','U']
#     consequence = []
#     i = 1
#     for u in range(5, 15, 1 ):
#         print("第",i,"轮")
#         i += 1
#         #print(u)
#         Umin=u
#         Umax=u+1
#         temp_u = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_U[0].append(temp_u[0])
#         makeTable_U[1].append(temp_u[1])
#         makeTable_U[2].append(u)
#
#     for i in range(len(makeTable_U)):
#         print(makeTable_U[i])
#     return makeTable_U
#
#
# def run_numP(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_numP = [[], [],[],'|S|','numP']
#     consequence=[]
#     i=1
#     for numP in range(2, 16):
#         print("第",i,"轮")
#         i+=1
#         temp_numP = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_numP[0].append(temp_numP[0])
#         makeTable_numP[1].append(temp_numP[1])
#         makeTable_numP[2].append(numP)
#
#     for i in range(len(makeTable_numP)):
#         print(makeTable_numP[i])
#     return makeTable_numP
#
# def run_numTask(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_numTask = [[], [],[],'N','numtask']
#     consequence=[]
#     i=1
#     for tasknum in range(5, 20):
#
#         umin=Umin/10*tasknum
#         umax=Umax/10*tasknum
#
#         print("第",i,"轮")
#         i+=1
#         temp_numP = Experiment_path.EXPERIMENT(tasknum,umin,umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_numTask[0].append(temp_numP[0])
#         makeTable_numTask[1].append(temp_numP[1])
#         makeTable_numTask[2].append(tasknum)
#
#     for i in range(len(makeTable_numTask)):
#         print(makeTable_numTask[i])
#     return makeTable_numTask
#
# def run_Ms(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_Ms = [[], [], [],'Ms','Ms']
#     consequence = []
#     i = 1
#     for Msmin in range(3, 30, 3 ):
#         print("第",i,"轮")
#         i += 1
#         #print(u)
#         Msmax=Msmin+3
#         temp_u = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_Ms[0].append(temp_u[0])
#         makeTable_Ms[1].append(temp_u[1])
#         makeTable_Ms[2].append(Msmin)
#
#     for i in range(len(makeTable_Ms)):
#         print(makeTable_Ms[i])
#     return makeTable_Ms
#
# def run_Ndag(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_Ndag = [[], [], [],'|V|','Ndag']
#     consequence = []
#     i=1
#     for Ndagmin in range(10, 60,5):
#         Ndagmax=Ndagmin+5
#         print("第",i,"轮")
#         i+=1
#         temp_Ndag =Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_Ndag[0].append(temp_Ndag[0])
#         makeTable_Ndag[1].append(temp_Ndag[1])
#         makeTable_Ndag[2].append(Ndagmin)
#
#     for i in range(len(makeTable_Ndag)):
#         print(makeTable_Ndag[i])
#     return makeTable_Ndag
#
# def run_Pr(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN):
#     makeTable_Pr = [[], [], [],'Pr','Pr']
#     consequence = []
#     i=1
#     for Pr in range(1, 10):
#         Pr=round((Pr/10),1)
#         print("第",i,"轮")
#         i+=1
#         temp_Pr =Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
#         makeTable_Pr[0].append(temp_Pr[0])
#         makeTable_Pr[1].append(temp_Pr[1])
#         makeTable_Pr[2].append(Pr)
#
#     for i in range(len(makeTable_Pr)):
#         print(makeTable_Pr[i])
#     return makeTable_Pr

       # path(data=["10","8","10","100","1000","15","30","15","20","0.1","10","5"],[1,1],3,1,begin,end,pace)
def run_all(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,which_parameter,task_save,begin,end,pace):
    file = open("model.txt", 'w')
    file.write("generate\n")
    file.close()
    if (which_parameter==3 or which_parameter==6):
        begin=round(float(begin),4)
        end=round(float(end),4)
        pace=round(float(pace),4)
        print(begin,end,pace)
    else :
        begin = int(begin)
        end = int(end)
        pace = int(pace)
        print(begin, end, pace)
    if which_parameter==1:
    #tasknum实验
        ret=run_numTask(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace)
    elif which_parameter == 2:
    #Ms实验
        ret=run_Ms(tasknum, Umin, Umax, Tmin, Tmax, Ndagmin, Ndagmax, Msmin, Msmax, Pr, numP, TURN,options,task_save,begin, end, pace)
    elif which_parameter == 3:
    #U实验
        ret=run_U(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace)
    elif which_parameter == 4:
    #numP实验
        ret=run_numP(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace)
    elif which_parameter == 5:
    #Ndag
        ret=run_Ndag(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace)
    elif which_parameter == 6:
    #Pr
        ret=run_Pr(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace)
    return ret

# path(data=["10","8","10","100","1000","15","30","15","20","0.1","10","5"],[1,1],3,1,begin（1）,end（5）,pace（1）)
def  run_U(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace):
    makeTable_U = []
    num = options.count(1)
    for x in range(num):
        makeTable_U.append([])
        makeTable_U.append([])
    makeTable_U.append([])
    makeTable_U.append('U')
    makeTable_U.append('U')

    totalrt = []

    number_ntuple = []
    number_ntuple2 = []

    begin = int(begin * 10000)
    end = int((end+0.0001) * 10000)
    pace = int(pace * 10000)
    print("u", begin, end, pace)
    i = 1
    for u in range(begin, end, pace):
        print("第",i,"轮")
        u=u/10000
        i += 1
        #print(u)
        Umin=u
        Umax=u+1
        temp_u = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)
        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_u[4] / TURN )
        number_ntuple.append(temp_u[5])
        number_ntuple2.append(temp_u[6])
        # print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range(num):
            makeTable_U[2 * j].append(temp_u[2 * j])
            makeTable_U[2 * j + 1].append(temp_u[2 * j + 1])
        makeTable_U[-3].append(u)

    return [makeTable_U, totalrt, number_ntuple, number_ntuple2]




def run_numP(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,           options,task_save,begin, end, pace):
    makeTable_numP = []
    num = options.count(1)
    for x in range(num):
        makeTable_numP.append([])
        makeTable_numP.append([])
    makeTable_numP.append([])
    makeTable_numP.append('|Γ|')
    makeTable_numP.append('numP')
    totalrt = []

    number_ntuple = []
    number_ntuple2 = []


    i=1
    for numP in range(begin, end+1, pace):
        print("第",i,"轮")
        i+=1

        temp_numP = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)

        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_numP[4] / TURN)

        number_ntuple.append(temp_numP[5])
        number_ntuple2.append(temp_numP[6])

        # print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range(num):
            makeTable_numP[2 * j].append(temp_numP[2 * j])
            makeTable_numP[2 * j + 1].append(temp_numP[2 * j + 1])
        makeTable_numP[-3].append(numP)
    return [makeTable_numP, totalrt, number_ntuple, number_ntuple2]

def run_numTask(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace):
    makeTable_numTask=[]
    num=options.count(1)
    for x in range (num):
        makeTable_numTask .append([])
        makeTable_numTask .append([])
    makeTable_numTask.append([])
    makeTable_numTask.append('N')
    makeTable_numTask.append('numtask')
    print(makeTable_numTask)
    totalrt = []
    number_ntuple = []
    number_ntuple2 = []

    i=1
    for tasknum in range(begin, end+1, pace):

        umin=Umin/10*tasknum
        umax=Umax/10*tasknum

        print("第",i,"轮")
        i+=1
        temp_numTask = Experiment_path.EXPERIMENT(tasknum,umin,umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)
        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_numTask[4] / TURN)
        number_ntuple.append(temp_numTask[5])
        number_ntuple2.append(temp_numTask[6])
        print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range (num):
            makeTable_numTask[2 * j].append(temp_numTask[2 * j])
            makeTable_numTask[2 * j + 1].append(temp_numTask[2 * j + 1])
        makeTable_numTask[-3].append(tasknum)
    print("make",makeTable_numTask)
    return [makeTable_numTask,totalrt, number_ntuple, number_ntuple2]

def run_Ms(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,           options,task_save,begin, end, pace):
    makeTable_Ms = []
    num = options.count(1)
    for x in range(num):
        makeTable_Ms.append([])
        makeTable_Ms.append([])
    makeTable_Ms.append([])
    makeTable_Ms.append('Mγ')
    makeTable_Ms.append('Mγ')
    totalrt = []
    number_ntuple = []
    number_ntuple2 = []

    i = 1
    for Msmin in range(begin, end+1, pace):
        print("第",i,"轮")
        i += 1
        #print(u)
        Msmax=Msmin+3
        temp_ms = Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)
        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_ms[4] / TURN)
        number_ntuple.append(temp_ms[5])
        number_ntuple2.append(temp_ms[6])
        print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range(num):
            makeTable_Ms[2 * j].append(temp_ms[2 * j])
            makeTable_Ms[2 * j + 1].append(temp_ms[2 * j + 1])
        makeTable_Ms[-3].append(Msmin)

    return [makeTable_Ms, totalrt, number_ntuple, number_ntuple2]



def run_Ndag(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace):
    makeTable_Ndag = []
    num = options.count(1)
    for x in range(num):
        makeTable_Ndag.append([])
        makeTable_Ndag.append([])
    makeTable_Ndag.append([])
    makeTable_Ndag.append('|V|')
    makeTable_Ndag.append('Ndag')
    totalrt = []
    number_ntuple = []
    number_ntuple2 = []
    i=1
    for Ndagmin in range(begin, end+1, pace):
        Ndagmax=Ndagmin+5
        print("第",i,"轮")
        i+=1
        temp_Ndag =Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)
        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_Ndag[4] / TURN)
        number_ntuple.append(temp_Ndag[5])
        number_ntuple2.append(temp_Ndag[6])
        # print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range(num):
            makeTable_Ndag[2 * j].append(temp_Ndag[2 * j])
            makeTable_Ndag[2 * j + 1].append(temp_Ndag[2 * j + 1])
        makeTable_Ndag[-3].append(Ndagmin)

    print(makeTable_Ndag)
    print(totalrt)
    print(number_ntuple)
    print(number_ntuple2)

    return [makeTable_Ndag, totalrt, number_ntuple, number_ntuple2]


def run_Pr(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save,begin, end, pace):
    makeTable_Pr = []
    num = options.count(1)
    for x in range(num):
        makeTable_Pr.append([])
        makeTable_Pr.append([])
    makeTable_Pr.append([])
    makeTable_Pr.append('Pr')
    makeTable_Pr.append('Pr')
    begin = int(begin * 10000)
    end = int((end+0.0001) * 10000)
    pace = int(pace * 10000)
    print("pr", begin, end, pace)
    totalrt = []
    number_ntuple = []
    number_ntuple2 = []
    i=1
    for Pr in range(begin, end, pace):
        Pr=Pr/10000
        print("第",i,"轮")
        i+=1
        # # 类型随机
        # type_nump = random.randint(numP - 5, numP + 5)
        # temp_Pr = Experiment_path.EXPERIMENT(tasknum, Umin, Umax, Tmin, Tmax, Ndagmin, Ndagmax, Msmin, Msmax, Pr,type_nump,TURN, options, task_save)

        temp_Pr =Experiment_path.EXPERIMENT(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN,options,task_save)

        # [RATE, TIME, RATE_fake, TIME_fake, imp]
        # 归一化计算部分
        # 记录每轮的归一化处理
        totalrt.append(temp_Pr[4] / TURN)
        number_ntuple.append(temp_Pr[5])
        number_ntuple2.append(temp_Pr[6])
        print(f"当前第{i}轮的平均归一化RT{totalrt}")
        for j in range(num):
            makeTable_Pr[2 * j].append(temp_Pr[2 * j])
            makeTable_Pr[2 * j + 1].append(temp_Pr[2 * j + 1])
        makeTable_Pr[-3].append(Pr)

    return [makeTable_Pr,totalrt, number_ntuple, number_ntuple2]