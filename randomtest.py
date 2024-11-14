import random
import pickle
import time
import Approx
import randomDAG
import ImpBL
import Baseline
# import schedulingtuple



def UexperienmentsMS(Tsetsnum, Umin, Umax, Nummini, Nummax, Tmini, Tmax, Pr, numP, MS):
    N=0
    results=[]


    # U=Umin
    accbrt=0
    accbrt1=0
    accrtdp=0
    accrttp=0

    rtimp=0
    rtdp=0
    rttp=0

    tbl=0
    timp=0
    tdp=0
    ttp=0

    # N、Tsetsnum控制循环次数
    while N < Tsetsnum:
        # print ("U=", U)
        # print ("N=",N)
        # 初始化利用率
        u_t = 0
        # u_t=0即任务集执行时间等于0，
        while u_t == 0 or u_t > Umax:

            T = randomDAG.RandomDAGtask(Nummini, Nummax, Tmini, Tmax, Pr, numP)
            task = T.createtask(Umax)
            # print ("V",task.V)
            # print ("E",task.E)
            # print ("P",task.P)
            # print ("Ci=",task.Ci())
            # print ("Ti=",task.Ti)
            u_t= task.Ci() / task.Ti
            # print "u_t=", u_t


        if u_t > Umin:
            N=N+1
            print("========成功运行========")
            print("N=",N)
            # print "task.E",task.E
            # print "task.Cpi=",task.Cpi
            t0=time.time()
            # 最坏情况下的的响应时间
            brt=Baseline.getwcrt(task,MS)
            # 总的运行时间
            tbl=tbl+time.time()-t0
            # print ("brt=",brt)
            # 响应时间小于等于任务集的截止时间，成功次数accbrt+1
            if brt<= task.Di:
                accbrt=accbrt+1

            t0 = time.time()
            brt1=ImpBL.getwcrt(task,MS)
            timp= timp + time.time() - t0
            # print ("imprt=",brt1)
            # 相对于baseline的响应时间的比例
            rtimp = rtimp+brt1 /brt
            if brt1<=task.Di:
                accbrt1 = accbrt1 + 1

            t0 = time.time()
            bprt=Approx.findRT(task,MS)
            tdp = tdp + time.time() - t0
            # print("dprt=", bprt)
            rtdp=rtdp+bprt/brt
            if bprt<task.Di:
                accrtdp=accrtdp+1

            # t0 = time.time()
            # tprt=schedulingtuple.findRT(task,MS)
            # ttp = ttp + time.time() - t0
            # # 不知道ExactpDP？？？
            # exactrt=ExactpDP.findRT(task,MS)
            # # print("tprt=", tprt)
            #
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



    return accbrt,accbrt1,accrtdp,accrttp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,N
def Run_Utest(tnum,Umin,Nummini, Nummax, Tmini, Tmax, Pr, numP,Mmin,Mmax,fpath):
    MS=[]

    # 生成任务集合每个任务的执行时间
    for i in range(numP):
        # m=random.randint(Mmin,Mmax)
        m = 2+i
        # if m - (Nummini / numP) > 1:
        #     m = int(Nummini / numP)
        MS.append(m)
    # M=0
    # for i in range(numP+1):
    #
    #         M =M+ MS[i]
    print("MS",MS)

    Umax=21
    # for i in range(0,len(MS)):
    #     if MS[i]>M:
    #         M=MS[i]
    # Umax=3
    # print Umax
    # 设置步长
    Ustep=(Umax-Umin)/20

    U=Umin
    # U=3
    # Umax=3
    X=[]
    accbrt=[]
    accimp=[]
    accdp = []
    acctp=[]

    rtimp=[]
    rtdp=[]
    rttp=[]

    tbl=[]
    timp=[]
    tdp=[]
    ttp=[]

    Tsetsnum=[]
    irt=0

    while U <= Umax and irt<3:
        X.append(U)
        print("U=", U)

        print("irt=",irt)

        umin=U-Ustep
        re=UexperienmentsMS(tnum,umin,U,Nummini, Nummax, Tmini, Tmax, Pr, numP,MS)

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

        # 没有成功运行Approx
        if re[2]==0:
            irt=irt+1

        U=U+Ustep

    results=[X,accbrt,accimp,accdp,acctp,rtimp,rtdp,rttp,tbl,timp,tdp,ttp,Tsetsnum,Umax]
    file=open(fpath,'wb')
    pickle.dump(results,file)
    file.close()
    print(("results=",results))
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
    Mmax = 3
    for i in range(0,pn):
        ms = random.randint(Mmin, Mmax)
        # 分配核心的个数
        MS.append(ms)
        if len(MS)==pn:
            break
    # Run_Utest(10, 1, 80, 81, 100, 1000, 0.1, pn, MS, '.\\tt', 13)
    # def Run_Utest(tnum,Umin,Nummini, Nummax, Tmini, Tmax, Pr, numP,Mmin,Mmax,fpath):
    # Run_Utest(100,1,70,71,100,1000,0.1,10,2,11,'.\\tupleresult\\M=2-11pn=10pr=01n=70t.pickle')、
    Run_Utest(10, 1, 70, 71, 100, 1000, 0.1, 10, 2, 11, '.\\test.pickle')
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
