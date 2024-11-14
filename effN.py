
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

def UexperienmentsMS(Tsetsnum,Nummini, Nummax, Tmini,Tmax , Prmin,Prmax, Pnmin,Pnmax):
    N=0
    results=[]



    Umin=1
    accbrt = 0
    accbrt1 = 0
    accrtdp = 0
    accrttp = 0
    rtimp = 0
    rtdp = 0
    rttp = 0
    tbl = 0
    timp = 0
    tdp = 0
    ttp = 0
    accrtyd = 0
    rtyd = 0
    tyd = 0
    while N < Tsetsnum:
        # print "U=", U
        # print "N=",N
        u_t = 0
        Pr=random.uniform(Prmin,Prmax)
        numP=random.randint(Pnmin,Pnmax)
        numP=min(Nummini,numP)
        MS=[]
        for i in range(numP):
            MS.append(2+i)
        Umax=3.5
        while u_t == 0 or u_t > Umax:

            T = randomDAG.RandomDAGtask(Nummini, Nummax, Tmini, Tmax, Pr, numP)
            utemp=random.uniform(1,3)
            task = T.createtask(utemp)
            # print "V",task.V
            # print "E",task.E
            # print "P",task.P
            # print "Ci=",task.Ci()
            # print "Ti=",task.Ti
            u_t= task.Ci() / task.Ti
            # print "u_t=", u_t
        if u_t > Umin:
            N=N+1
            # print "task.E",task.E
            # print "task.Cpi=",task.Cpi
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
def Run_Utest(tnum,Nummini, Nummax, Tmini, Tmax, Prmin,Prmax, Pnmin,Pnmax,fpath):
    M = 0
    # for i in range(0, len(MS)):
    #         M =M+ MS[i]
    # Umax = 2.5
    # for i in range(0,len(MS)):
    #     if MS[i]>M:
    #         M=MS[i]
    # Umax=3
    # print Umax
    # Ustep=(Umax-Umin)/20
    # U=Umin
    N=Nummini+5
    Nstep=5
    # U=3
    # Umax=3
    X = []
    accbrt = []
    accimp = []
    accdp = []
    acctp = []
    rtimp = []
    rtdp = []
    rttp = []
    tbl = []
    timp = []
    tdp = []
    ttp = []
    Tsetsnum = []
    accyd = []
    rtyd = []
    tyd = []

    while N <= Nummax:

        print("VN=",N)

        tmin=N-Nstep
        re=UexperienmentsMS(tnum,tmin, N, Tmini,Tmax , Prmin,Prmax, Pnmin,Pnmax)
        X.append(N)
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
        N=N+Nstep
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
    MS=[]
    pn=10
    Mmin = 2
    Mmax = 8
    for i in range(0,pn):
        ms = 2+i
        MS.append(ms)
    print(MS)
    # tnum, Umin, Nummini, Nummax, Tmini, Tmax, Pr, numP, MS, fpath, numMS
    Run_Utest(100,5,115,100,1000,0.08,0.4,5,10,'.\\tupleresult\\yresult\\effN=5-10pn=5-10pr=008-01ms=2-11u=1-3.pickle')
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
