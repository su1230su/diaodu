#coding=utf-8
from __future__ import division
import math
import random
import copy
import pickle
import moreDAG
import randomDAG
import time

def UexperienmentsMS(Tsetsnum,Umin,Umax,Nummini, Nummax, Tmini, Tmax, Pr, numP,MS,Usg,NHP):
    N=0
    results=[]


    # U=Umin
    accbrt=0
    # 计算Com_DAG_2的运行次数
    accbrt1=0
    # accrtdp=0
    # accrttp=0
    rtimp=0
    # rtdp=0
    # rttp=0
    tbl=0
    timp=0
    # tdp=0
    # ttp=0

    while N < Tsetsnum:
        # print ("U=", U)
        # print ("N=",N)
        # 初始化利用率
        u_t = 0
        #
        task=0
        while u_t == 0 or u_t > Umax:

            T = randomDAG.RandomDAGtask(Nummini, Nummax, Tmini, Tmax, Pr, numP)
            task = T.createtask(Umax)
            # print ("V",task.V)
            # print ("E",task.E)
            # print ("P",task.P)
            # print ("Ci=",task.Ci())
            # print ("Ti=",task.Ti)

            # 计算利用率，以便进入IF条件
            u_t= task.Ci() / task.Ti
        # print("u_t=", u_t)
        if u_t > Umin:
            # 存储每个处理器的任务集
            Thps=[]
            # 获取当前任务的周期时间，作为后续任务集生成的上限
            Tmax=task.Ti
            # 遍历处理器
            for s in range(numP):
                # 获取第s个处理器的利用率
                U_s=Usg[s]
                # 获取第s个处理器的任务数量
                N_s=NHP[s]
                # 调用randomtask生成一个随机任务集包含了nump个处理器的任务
                T_sg=randomDAG.RandomTask(Tmini,Tmax,numP)
                # 第s个处理器生成任务集合
                T_s=T_sg.creatTsets_s(s,N_s,U_s)
                # 第s个处理器的任务集 T_s 添加到总的任务集 Thps 中。
                Thps=T_sg.creatTsets(T_s,Thps)

            # 成功运行次数加一
            N=N+1

            # print "task.E",task.E
            # print "task.Cpi=",task.Cpi
            t0=time.time()
            brt=moreDAG.Com_DAG_1(task,Thps,MS)
            # Com_DAG_1的总的运行时间
            tbl=tbl+time.time()-t0

            # print ("brt=",brt)
            #
            if brt<= task.Di and brt!=0:
                accbrt = accbrt + 1

            t0 = time.time()
            brt1=moreDAG.Com_DAG_2(task,Thps,MS)
            # Com_DAG_2的总的运行时间
            timp= timp + time.time() - t0

            # print ("imprt=",brt1)
            if brt1<=task.Di and brt1!=0:
                if  brt==0:
                    # 在Com_DAG_1的响应时间为0时，Com_DAG_2相对于Com_DAG_1的比例
                    rtimp=rtimp+1
                else:
                    # Com_DAG_2相对于Com_DAG_1的比例
                    rtimp = rtimp + brt1 / brt
                # 计算Com_DAG_2的运行次数
                accbrt1 = accbrt1 + 1
            else:
                # 当Com_DAG_2算法的响应时间大于任务的截止时间，输出任务的信息。
                if brt!=0:
                    print("errotask")
                    print ("V",task.V)
                    print ("E",task.E)
                    print ("P",task.P)
                    print ("Ci=",task.Ci())
                    print ("Ti=",task.Ti)
                    print("MS=",MS)
                    print("THPS=", Thps)
                    print("brt=",brt)
                    print("brt1=",brt1)

            # t0 = time.time()
            # bprt=Approx.findRT(task,MS)
            # tdp = tdp + time.time() - t0
            # # print("dprt=", bprt)
            # rtdp=rtdp+bprt/brt
            # if bprt<task.Di:
            #     accrtdp=accrtdp+1
            #
            # t0 = time.time()
            # tprt=schedulingtuple.findRT(task,MS)
            # ttp = ttp + time.time() - t0
            # exactrt=ExactpDP.findRT(task,MS)
            # print("tprt=", tprt)

            # rttp=rttp+tprt/brt
            # if tprt<task.Di:
            #     accrttp=accrttp+1
            # if tprt-exactrt>1 or tprt-exactrt<-1:
            #     print("dprt=", bprt)
            #     print("tprt=", tprt)
            #     print("exactrt=", exactrt)
            #     print ("error")
            #     print("task.v=",task.V)
            #     print("task.E=", task.E)
            #     print("task.p=", task.P)
            #     print("MS=",MS)
            #     break

    return accbrt,accbrt1,rtimp,tbl,timp,N


def Run_Utest(tnum,Nummini, Nummax, Tmini, Tmax, Pr, numP,Mmin,Mmax,Sgnum,fpath):

    MS=[]
    Usg = []
    NHP = []
    # 给每个处理器随机生成性能值、利用率、任务数量
    for i in range(numP):
        m=random.randint(Mmin,Mmax)
        u_s = random.uniform(0.0, m)
        MS.append(m)
        Usg.append(u_s)
        if u_s==0:
            n_s=0
        else:
            # 任务数量
            n_s=random.randint(m,Sgnum)
        NHP.append(n_s)

    Umin=0.1
    Umax=0.5
    # 计算每次前进的步长
    Ustep=(Umax-Umin)/10
    # 初始化dag的利用率为所有的最小的利用率
    Udag=Umin
    # U=3
    # Umax=3

    X=[]
    # 运行次数的集合
    accbrt=[]
    accimp=[]
    # accdp = []
    # acctp=[]
    # 比例
    rtimp=[]
    # rtdp=[]
    # rttp=[]
    # Com_DAG_1的总的运行时间
    tbl=[]
    # Com_DAG_2的总的运行时间
    timp=[]
    # tdp=[]
    # ttp=[]
    Tsetsnum=[]


    # 存储算法响应时间为0的次数
    irt=0

    while Udag <= Umax and irt<10:

        X.append(Udag)
        print("U=", Udag)

        umin=Udag-Ustep
        re=UexperienmentsMS(tnum,umin,Udag,Nummini, Nummax, Tmini, Tmax, Pr, numP,MS,Usg,NHP)

        accbrt.append(re[0])
        accimp.append(re[1])
        # accdp.append(re[2])
        # acctp.append(re[3])
        rtimp.append(re[2])
        # rtdp.append(re[5])
        # rttp.append(re[6])
        tbl.append(re[3])
        timp.append(re[4])
        # tdp.append(re[9])
        # ttp.append(re[10])
        # diff14.append(re[7])
        # diff24.append(re[8])
        # diffrt.append(re[2])
        # diffnum.append(re[3])
        Tsetsnum.append(re[5])
        # 统计
        if re[2]==0:
            irt=irt+1
            
        Udag=Udag+Ustep

    # results=[X,accbrt,accimp,accdp,acctp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,Tsetsnum,Umax]
    results = [X, accbrt, accimp, rtimp, tbl, timp,Tsetsnum, Umax]
    file=open(fpath,'wb')
    pickle.dump(results,file)
    file.close()
    print(("results=",results))
    return results

if __name__ == '__main__':
    tnum=100  #任务集数量
    Nummini=5 #最小节点数
    Nummax=20 #最大结点数
    Tmini=10 #最小周期
    Tmax=1000#最大周期
    Pr=0.1#并行度
    numP=5#类别数
    Mmin=2#每个类别最小处理器个数
    Mmax=10#每个类别最大处理器个数
    Sgnum=15#单结点任务数
    fpath='.\\test.pickle'
    # fpath = '.\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle'
    Run_Utest(tnum, Nummini, Nummax, Tmini, Tmax, Pr, numP, Mmin, Mmax, Sgnum, fpath)
