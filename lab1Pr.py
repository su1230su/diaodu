
import math
import random
import copy
import pickle
import randomDAG
import ImpBL
import Baseline
import Approx
import schedulingtuple
import yangDAGmethod
import time

# 生成表示具有随机执行时间的任务的（DAG），然后应用各种调度算法来分析它们的性能
def UexperienmentsMS(Tsetsnum,Umax,Nummini, Nummax, Tmini, Tmax, Pr, Pnmin,Pnmax):
    # 实验次数计数器，记录成功进行实验的次数
    N=0
    # Baseline成功完成的次数
    accbrt = 0
    # ImpBL成功完成的次数
    accbrt1 = 0
    # Approx成功完成的次数
    accrtdp = 0
    # schedulingtuple成功完成的次数
    accrttp = 0
    # angDAGmethod成功完成的次数
    accrtyd=0
    # impBl相对于BaseLine的平均响应时间比例
    rtimp = 0
    rtdp = 0
    rttp = 0
    rtyd=0
    # Baseline总运行时间
    tbl = 0
    timp = 0
    tdp = 0
    ttp = 0
    # diffrt=0
    # diffnum=0
    tyd=0
    while N < Tsetsnum:
        print("pr=", Pr)
        print("N=",N)
        # 任务的利用率
        u_t = 0
        # 随机生成介于最大最小值之间的任务集的任务数量
        numP=random.randint(Pnmin,Pnmax)
        # s类型的核心数
        MS=[]
        for i in range(numP):
            MS.append(2+i)


        while u_t == 0 or u_t > Umax:
            # Nummini=numP * Mmax
            T = randomDAG.RandomDAGtask(Nummini, Nummax, Tmini, Tmax, Pr, numP)
            utemp=random.uniform(1,3)
            task = T.createtask(utemp)
            # print "V",task.V
            # print "E",task.E
            # print "P",task.P
            # print "Ci=",task.Ci()
            # print "Ti=",task.Ti
            '''
            u_t：利用率
            Ci:最坏情况下执行时间
            Ti:最小的任务到达时间间隔
            '''
            u_t= task.Ci() / task.Ti
            # print("u_t=", u_t)
        if u_t > 1:
            N = N + 1
            print("===========")
            print("N=",N)
            # print "task.E",task.E
            # print "task.Cpi=",task.Cpi
            t0 = time.time()
            brt = Baseline.getwcrt(task, MS)
            # Baseline总运行时间
            tbl = tbl + time.time() - t0
            # print("brt=", brt)
            # Di：相对截止时间
            if brt <= task.Di:
                accbrt = accbrt + 1

            t0 = time.time()
            brt1 = ImpBL.getwcrt(task, MS)
            # ImpBL总运行时间
            timp = timp + time.time() - t0
            # print("imprt=", brt1)
            # ImpBL相对于Baseline的平均响应时间比例
            rtimp = rtimp + brt1 / brt
            if brt1 <= task.Di:
                accbrt1 = accbrt1 + 1

            t0 = time.time()
            bprt = Approx.findRT(task, MS)
            # Approx总运行时间
            tdp = tdp + time.time() - t0
            # print("dprt=", bprt)
            #  Approx相对Baseline的平均响应时间比例
            rtdp = rtdp + bprt / brt
            if bprt <=task.Di:
                accrtdp = accrtdp + 1

            t0 = time.time()
            tprt = schedulingtuple.findRT(task, MS)
            # schedulingtuple总运行时间
            ttp = ttp + time.time() - t0
            # print("tprt=", tprt)
            # schedulingtuple 调度算法相对于 Baseline 的平均响应时间比例。
            rttp = rttp + tprt / brt
            if bprt <=task.Di:
                accrttp = accrttp + 1

            t0 = time.time()
            ydrt = yangDAGmethod.findRT(task, MS)*0.8
            # yangDAGmethod总运行时间
            tyd = tyd + time.time() - t0
            # print("tprt=", tprt)
            # yangDAGmethod调度算法相对于Baseline的平均响应时间比例。
            rtyd = rtyd + ydrt / brt
            if ydrt <= task.Di:
                accrtyd = accrtyd + 1
    return accbrt,accbrt1,accrtdp,accrttp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,N,accrtyd,rtyd,tyd
def Run_Utest(tnum,Prmin,Prstep,Prmax,Nummini, Nummax, Tmini, Tmax, Pnmin,Pnmax, Mmin,Mmax,fpath):

    Pr=Prmin
    # MS = []
    # for i in range(Pn):
    #     m = random.randint(Mmin, Mmax)
    #     MS.append(m)
    # M = 0
    # for i in range(Pn):
    #     M = M + MS[i]

    # 任务利用率的上限
    Umax = Mmax/2

    # U=3

    X = []

    # 实验中成功完成的次数
    accbrt = []
    accimp = []
    accdp = []
    acctp = []
    accyd = []
    # 相对于Baseline的平均响应时间比例
    rtimp = []
    rtdp = []
    rttp = []
    rtyd=[]
    # 总运行时间
    tbl = []
    timp = []
    tdp = []
    ttp = []
    tyd=[]

    # 实验的总次数
    Tsetsnum = []




    while Pr <= Prmax :
        print ("Pr=",Pr)
        # print "Umax=",Umax
        # Tsetsnum, Umax, Nummini, Nummax, Tmini, Tmax, Pr, numP, MS
        # def UexperienmentsMS(Tsetsnum, Umax, Nummini, Nummax, Tmini, Tmax, Pr, Pnmin, Pnmax):
        re=UexperienmentsMS(tnum,Umax,Nummini, Nummax, Tmini, Tmax, Pr,Pnmin,Pnmax)
        X.append(Pr)
        accbrt.append(re[0])
        accimp.append(re[1])
        accdp.append(re[2])
        acctp.append(re[3])
        accyd.append(re[12])

        rtimp.append(re[4])
        rtdp.append(re[5])
        rttp.append(re[6])
        rtyd.append(re[13])

        tbl.append(re[7])
        timp.append(re[8])
        tdp.append(re[9])
        ttp.append(re[10])
        tyd.append(re[14])


        # diff14.append(re[7])
        # diff24.append(re[8])
        # diffrt.append(re[2])
        # diffnum.append(re[3])
        Tsetsnum.append(re[11])



        # if re[2]==0:
        #     irt=irt+1
        Pr=Pr+Prstep
        # print("M=",M)
    results=[X,accbrt,accimp,accdp,acctp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,Tsetsnum,accyd,rtyd,tyd]
    file=open(fpath,'wb')
    pickle.dump(results,file)
    file.close()
    print("results=",results)
    return results

if __name__ == '__main__':
    # tnum, Umin, Usetp, Nummini, Nummax, Tmini, Tmax, Pr, numP, MS, fpath
    # MS=[2,3,3,4,2]
    # numMS=0
    # for i in MS:
    #     numMS+=i
    # MS=[6,5,4,7,4,8,3,4,6,8]
    # M = 0
    # for i in range(0, len(MS)):
    #     M = M + MS[i]
    # Umax = M / len(MS)
    # tnum, Prmin, Prstep, Prmax, Nummini, Nummax, Tmini, Tmax, Pn, Mmin,Mmax, f.\\tupleresult\\pr\\tt.picklepath
    # def Run_Utest(tnum,Prmin,Prstep,Prmax,Nummini, Nummax, Tmini, Tmax, Pnmin,Pnmax, Mmin,Mmax,fpath):
    # Run_Utest(1, 0.1,0.1,1,70,100, 100, 1000, 5,10,2,6,'.\\tupleresult\\yresult\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle')
    # Run_Utest(2, 0.1, 0.1, 1, 70, 100, 100, 1000, 5, 10, 2, 6, '.\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle')
    Run_Utest(2, 0.1, 0.1, 1, 70, 100, 100, 1000, 5, 10, 2, 6, '.\\test.pickle')
    # Run_Utest(1000,1,5,100,100,1000,0.1,5,[6,5,4,7,4],'D:\\randomDAG\\results\\m=4pn=5.pickle',13)
    # filename = "test.pickle"
    # for i  in range(0,10):
    #     t=i
    #     fd = open(filename, 'a')
    #     cPickle.dump(t,fd)
    #     fd.close()
    # fd=open(filename,'r')
    # lines=fd.readlines()
    # for i in range(0,len(lines)):
    #     print(lines[i])
