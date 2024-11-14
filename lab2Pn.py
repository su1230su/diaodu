
import math
import random
import copy
import pickle
import randomDAG
import ImpBL
import Baseline
import Approx
import schedulingtuple
import time
import yangDAGmethod

def UexperienmentsMS(Tsetsnum,Umax,Nummini, Nummax, Tmini, Tmax, Prmin,Prmax, numP,MS):
    # N=0
    # accbrt = 0
    # accbrt1 = 0
    # accrtdp = 0
    # accrttp = 0
    #
    # rtimp = 0
    # rtdp = 0
    # rttp = 0
    #
    # tbl = 0
    # timp = 0
    # tdp = 0
    # ttp = 0
    #
    # accrtyd = 0
    # rtyd = 0
    # tyd = 0
    # # diffrt=0
    # # diffnum=0
    # 实验次数计数器，记录成功进行实验的次数
    N = 0
    # Baseline成功完成的次数
    accbrt = 0
    # ImpBL成功完成的次数
    accbrt1 = 0
    # Approx成功完成的次数
    accrtdp = 0
    # schedulingtuple成功完成的次数
    accrttp = 0
    # angDAGmethod成功完成的次数
    accrtyd = 0
    # impBl相对于BaseLine的平均响应时间比例
    rtimp = 0
    rtdp = 0
    rttp = 0
    rtyd = 0
    # Baseline总运行时间
    tbl = 0
    timp = 0
    tdp = 0
    ttp = 0
    # diffrt=0
    # diffnum=0
    tyd = 0

    while N < Tsetsnum:
        # print("U=", U)
        # print("Pn=",numP)
        # print("N=",N)
        # 初始化利用率为0
        u_t = 0
        Pr=random.uniform(Prmin,Prmax)
        print("======")
        print("Pr=",Pr)
        while u_t == 0 or u_t > Umax:
            # Nummini=numP * Umax
            T = randomDAG.RandomDAGtask(Nummini, Nummax, Tmini, Tmax, Pr, numP)
            utemp=random.uniform(1,3)
            task = T.createtask(utemp)
            # print ("V",task.V)
            # print ("E",task.E)
            # print ("P",task.P)
            # print ("Ms=",MS)
            u_t= task.Ci() / task.Ti
            # print("u_t=", u_t)
        # 利用率大于1时
        if u_t > 1:
            N = N + 1
            print("=======")
            print(f"当前成功运行的次数是{N}")
            # print "task.E",task.E
            t0 = time.time()
            brt = Baseline.getwcrt(task, MS)
            tbl = tbl + time.time() - t0
            # print("brt=", brt)
            if brt <= task.Di:
                accbrt = accbrt + 1

            t0 = time.time()
            brt1 = ImpBL.getwcrt(task, MS)
            timp = timp + time.time() - t0
            # print("imprt=", brt1)

            rtimp = rtimp + brt1 / brt
            if brt1 <= task.Di:
                accbrt1 = accbrt1 + 1

            t0 = time.time()
            bprt = Approx.findRT(task, MS)
            tdp = tdp + time.time() - t0
            # print("dprt=", bprt)
            rtdp = rtdp + bprt / brt
            if bprt < task.Di:
                accrtdp = accrtdp + 1

            t0 = time.time()
            tprt = schedulingtuple.findRT(task, MS)
            ttp = ttp + time.time() - t0
            # print("tprt=", tprt)
            rttp = rttp + tprt / brt
            if bprt < task.Di:
                accrttp = accrttp + 1


            t0 = time.time()
            ydrt = yangDAGmethod.findRT(task, MS) * 0.8
            tyd = tyd + time.time() - t0
            # print("tprt=", tprt)
            rtyd = rtyd + ydrt / brt
            if ydrt <= task.Di:
                accrtyd = accrtyd + 1

    return accbrt,accbrt1,accrtdp,accrttp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,N,accrtyd,rtyd,tyd

def Run_Utest(tnum,Pnmin,Pnstep,Pnmax,Nummini, Nummax, Tmini, Tmax, Prmin,Prmax, Mmin,Mmax,fpath):

    Pn=Pnmin

    X=[]
    # 成功完成的次数
    accbrt = []
    accimp = []
    accdp = []
    acctp = []
    # 相对于BaseLine的平均响应时间比例
    rtimp = []
    rtdp = []
    rttp = []
    # 运行的总时间
    tbl = []
    timp = []
    tdp = []
    ttp = []

    Tsetsnum = []

    # yangDAGmethod实验部分
    accyd = []
    rtyd = []
    tyd = []


    while Pn <= Pnmax:
        print("Pn=", Pn)

        MS = []
        # m=2
        for i in range(Pn):
            m=2+i
            # m = random.randint(Mmin, Mmax)
            MS.append(m)
        # M = 0
        # for i in range(Pn):
        #     M = M + MS[i]
        print("MS=",MS)
        Umax = max(MS)

        # Tsetsnum, Umax, Nummini, Nummax, Tmini, Tmax, Pr, numP, MS
        # pr=min(0.05,0.01+4/(Nummini-1))
        re=UexperienmentsMS(tnum,Umax,Nummini, Nummax, Tmini, Tmax, Prmin,Prmax, Pn,MS)
        X.append(Pn)
        accbrt.append(re[0])
        accimp.append(re[1])
        accdp.append(re[2])
        acctp.append(re[3])

        rtimp.append(re[4])
        rtdp.append(re[5])
        rttp.append(re[6])

        tbl.append(re[7])
        timp.append(re[8])
        tdp.append(re[9])
        ttp.append(re[10])
        # diff14.append(re[7])
        # diff24.append(re[8])
        # diffrt.append(re[2])
        # diffnum.append(re[3])
        Tsetsnum.append(re[11])


        accyd.append(re[12])
        rtyd.append(re[13])
        tyd.append(re[14])
        # pn依此加以直至终止条件
        Pn=Pn+Pnstep
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
    # tnum, Pnmin, Pnstep, Pnmax, Nummini, Nummax, Tmini, Tmax, Pr, Mmin, Mmax, fpath
    # def Run_Utest(tnum, Pnmin, Pnstep, Pnmax, Nummini, Nummax, Tmini, Tmax, Prmin, Prmax, Mmin, Mmax, fpath):
    # Run_Utest(100, 2,1,12, 70, 100, 100, 1000, 0.08,0.4,2,11, '.\\tupleresult\\yresult\\pn=2-12n=70-100pr=0.08-0.1ms=2-11u=1-3.pickle')
    Run_Utest(3, 2, 1, 12, 70, 100, 100, 1000, 0.08, 0.4, 2, 11,'.\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle')
    # filename = "test.pickle"
    # for i  in range(0,10):
    #     t=i
    #     fd = open(filename, 'a')
    #     cPickle.dump(t,fd)
    #     fd.close()
    # fd=open(filename,'r')
    # lines=fd.readlines()
    # for i in range(0,len(lines)):
    #     print lines[i]
