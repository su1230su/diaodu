#coding=utf-8
import randomDAG
import copy

def refinefaV(task):
    anceV= randomDAG.findpcoDAG().findpa(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)
    # print('preV=',preV)
    faV=copy.deepcopy(preV)
    for i in range(0,lenV):
        for u in preV[i]:
            for v in preV[i]:
                if v !=u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break
    # print ("faV=",faV)
    return faV



def findRT(task,MS):
    Xuhao=0
    chV=randomDAG.findpcoDAG().findchild(task.V,task.E)
    # paV = randomDAG.findpcoDAG().findpa(task.V, task.E)
    # print (paV)
    paraV = randomDAG.findpcoDAG().findnorelationV(task.V, task.E, task.P)

    lenV = len(task.V)
    E = task.E
    FGtemp = [[] * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV=refinefaV(task)
    # preV = [[]]
    # for i in range(1, lenV):  # 每个结点的直接父亲节点parVset
    #     temp = []
    #     for j in range(0, i):
    #         if (j, i) in E:
    #             temp.append(j)
    #     preV.append(temp)
    # print ("preV=",preV)
    # tuopuO = randomDAG.findpcoDAG().BfsOrder(task)
    for i in range(lenV):
        # print ("calculating vertex ",i)
        if i==0:
        # if it is a source node
            rt=task.V[i]
            nn_set=[]
            for j in range(len(MS)):
                nn_set.append(-1)
            ty_i=task.P[i]-1
            nn_set[ty_i]=i
            FGtemp[i]=[[rt,nn_set]]
        else:
            # print("preV=",preV)
            for j in preV[i]:
                # print("the vertex %d is a father vertex of %d"%(j,i))
                # print("FGtemp[j]=", FGtemp)
                for k in FGtemp[j]:
                    wi = task.V[i] + k[0]
                    # print ("wi=",wi)
                    tmpp=[]

                    cori=task.P[i]-1
                    scv=k[1][cori]
                    # print("scv=", scv)

                    tmset=copy.deepcopy(k[1])
                    if scv!=-1:
                        tmpp = list(set(paraV[i]) - set(paraV[scv]))
                    else:
                        tmpp=paraV[i]
                    lenw=0.0
                    for p in range(len(tmpp)):
                        # print("i=%d,j=%d,p=%d" % (i, j, tmpp[p]))
                        lenw=lenw+task.V[tmpp[p]]
                    # print ("lenw=",lenw)
                    rt=wi+ lenw/MS[cori]
                    # print ("rt=",rt)
                    # print("tmpp=",tmpp)

                    tmset[cori]=i
                    ntuple=[rt,tmset]
                    lenFg=len(FGtemp[i])
                    if lenFg==0:
                        FGtemp[i].append(ntuple)
                    else:
                        flagst=1
                        for fgn in range(0,lenFg):
                            if ntuple==FGtemp[i][fgn][1]:
                                flagst=0
                                if rt> FGtemp[i][fgn][0]:
                                    FGtemp[i][fgn][0]=rt
                            else:
                                flagds1 = 0
                                flagds2 = 0
                                ntuple2 = FGtemp[i][fgn]
                                for tmpv in range(len(MS)):
                                    # print("tmpv=",tmpv)
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
                                                # print("tmp1=", tmp1)
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
                                                        # tmpv = numP + 1
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
                                                        # tmpv = numP + 1
                                                        break
                                # ts=time.time()-t0
                                # print("nodiaoyong=",ts)
                                # t0 = time.time()
                                flagds = [flagds1, flagds2]
                                if ntuple[0] > FGtemp[i][fgn][0]:
                                    if flagds[0] == 1:
                                        flagst = 0
                                        FGtemp[i][fgn] = ntuple
                                        break
                                else:
                                    if ntuple[0] == FGtemp[i][fgn][0]:
                                        if flagds[0] == 1:
                                            if flagds[1] == 0:
                                                flagst = 0
                                                FGtemp[i][fgn] = ntuple
                                                break
                                            else:
                                                flagst = 0
                                                break
                                        else:
                                            if flagds[1] == 1:
                                                flagst = 0
                                                break
                                    else:
                                        if flagds[1] == 1:
                                            flagst = 0
                                            break


                        if flagst==1:
                            FGtemp[i].append(ntuple)
                    # if ntuple not in FGtemp[i]:
                    #      FGtemp[i].append(ntuple)
        print("第", Xuhao, "个节点的FGtemp为: ", FGtemp[i])
        Xuhao += 1
    rtv = []
    mart = 0
    nt = 0
    for i in range(lenV):
        nt = nt + len(FGtemp[i])
    # print ("the number of all tuple is",nt)
    for k in FGtemp[lenV - 1]:
        # print ("k[0]=",k[0])
        rtv.append(k[0])
    if len(rtv) != 0:
        mart = max(rtv)
    # print("mart=", mart)
    RT = mart
    nume = len(task.E)
    pr = nume / (lenV * (lenV) / 2)
    # nt = len(FGtemp[lenV - 1])
    return RT, nt, pr

#
def find_diff(ntuple,ntuple2,paraV,chV,numP):

    flagds1=0
    flagds2=0

    for tmpv in range(numP):
        # print("tmpv=",tmpv)
        if ntuple[1][tmpv] !=  ntuple2[1][tmpv]:
            if ntuple[0] == ntuple2[0]:
                tmpminV = ntuple2[1][tmpv]
                tmpmaxV = ntuple[1][tmpv]
                if tmpminV==-1:
                    flagds2=1
                if tmpmaxV==-1:
                    flagds1 = 1
                if tmpmaxV!=-1 and tmpminV!=-1:
                    tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                    tmp1 = [v for v in paraV[tmpminV] if v in chV[tmpmaxV]]
                    # print("tmp1=", tmp1)
                    if len(tmp)==0:
                        flagds1=1
                        if len(tmp1)==0:
                            flagds2=1
                        else:
                            flagds2=0
                            break

                    else:
                        flagds1 = 0
                        if len(tmp1)==0:
                            flagds2=1
                        else:
                            flagds2=0
                            break

            else:

                tmpminV = 0
                tmpmaxV = 0
                if ntuple[0] >  ntuple2[0]:
                    tmpminV =  ntuple2[1][tmpv]
                    tmpmaxV = ntuple[1][tmpv]
                    if tmpmaxV==-1:
                        flagds1=1
                    if tmpminV==-1:
                        flagds1=0
                        break
                    if tmpmaxV!=-1 and tmpminV!=-1:
                        tmp = [v for v in paraV[tmpmaxV] if v in chV[tmpminV]]
                        if len(tmp) == 0:
                            flagds1 = 1
                        else:

                            flagds1 = 0
                            # tmpv = numP + 1
                            break
                else:
                    tmpminV = ntuple[1][tmpv]
                    tmpmaxV =  ntuple2[1][tmpv]
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
                            # tmpv = numP + 1
                            break


    return flagds1,flagds2




if __name__ == '__main__':
    # for n in range(50):
        # task=RandomDAGtask(5,30,40,1000,0.2,7
        # T=task.createtask(0)
        # paV=findpcoDAG().findpa(T.V,T.E)
        # chV=findpcoDAG().findchild(T.V,T.E)
        # paraV=findpcoDAG().findnorelationV(T.V,T.E,T.P)
    # a=[[1,[1,2]],[2,[3,4]]]
    # b=[1,[3,4]]
    # if b not in a:
    #     print ("b is in a",b)


    # v= [0, 9.97110267871767, 20.90311912948286, 1.9933279812132199, 1.8187412670705996, 0.20122719235377673,
    #           9.649068643176783, 59.55155208008446, 4.730899084937292, 58.94808958270854, 84.59952914096789,
    #           14.935717020388637, 1.2359405581349705, 60.388112161354655, 52.40150368463725, 4.604518145913708,
    #           9.320404213603581, 1.432663095117757, 7.743357708071439, 10.142683433553017, 1.7920932098680822,
    #           3.1360705948521073, 5.887805680780907, 38.84573688648685, 4.045980162828283, 20.31725272032407,
    #           16.38548079733217, 1.2325933456386036, 10.306285863605245, 0.31672716587160643, 9.623685856951631,
    #           114.43250752674521, 2.0943007730500334, 20.642226935294005, 39.75872939923559, 8.925297702788555,
    #           1.7455763102937727, 14.662804860377014, 54.422789274205854, 64.34248952128414, 5.19209430894281,
    #           15.031394444601155, 4.263706304256209, 2.042433125052117, 3.9825791274725777, 12.615731573704577,
    #           3.467698460725983, 15.665761743867977, 1.940583559768645, 5.833493444830129, 5.1113117536434345]
    # e= [(0, 1), (0, 3), (1, 2), (1, 4), (1, 5), (1, 6), (1, 8), (1, 10), (1, 11), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 30), (1, 33), (1, 37), (1, 40), (1, 41), (1, 43), (1, 44), (1, 46), (1, 48), (1, 49), (2, 4), (2, 5), (2, 7), (2, 8), (2, 9), (2, 12), (2, 13), (2, 16), (2, 19), (2, 23), (2, 24), (2, 25), (2, 26), (2, 27), (2, 28), (2, 30), (2, 31), (2, 33), (2, 34), (2, 36), (2, 39), (2, 41), (2, 42), (2, 45), (3, 5), (3, 7), (3, 8), (3, 12), (3, 14), (3, 15), (3, 17), (3, 18), (3, 19), (3, 22), (3, 23), (3, 25), (3, 28), (3, 30), (3, 33), (3, 34), (3, 36), (3, 37), (3, 40), (3, 41), (3, 42), (3, 43), (3, 45), (3, 47), (3, 48), (4, 5), (4, 7), (4, 9), (4, 13), (4, 14), (4, 17), (4, 22), (4, 23), (4, 27), (4, 29), (4, 31), (4, 33), (4, 34), (4, 38), (4, 40), (4, 45), (4, 46), (4, 48), (5, 7), (5, 8), (5, 9), (5, 17), (5, 19), (5, 21), (5, 25), (5, 28), (5, 29), (5, 35), (5, 38), (5, 39), (5, 40), (5, 41), (5, 42), (5, 46), (6, 7), (6, 9), (6, 11), (6, 12), (6, 15), (6, 18), (6, 20), (6, 23), (6, 24), (6, 26), (6, 27), (6, 31), (6, 33), (6, 35), (6, 37), (6, 42), (6, 43), (6, 44), (6, 46), (6, 47), (6, 48), (7, 12), (7, 14), (7, 16), (7, 17), (7, 18), (7, 19), (7, 20), (7, 22), (7, 24), (7, 26), (7, 30), (7, 31), (7, 32), (7, 34), (7, 35), (7, 38), (7, 39), (7, 41), (7, 42), (7, 45), (7, 46), (7, 47), (7, 48), (8, 12), (8, 13), (8, 15), (8, 17), (8, 20), (8, 21), (8, 22), (8, 24), (8, 29), (8, 34), (8, 37), (8, 43), (8, 44), (8, 45), (8, 46), (8, 48), (9, 10), (9, 11), (9, 12), (9, 17), (9, 18), (9, 24), (9, 26), (9, 27), (9, 29), (9, 30), (9, 31), (9, 36), (9, 37), (9, 39), (9, 40), (9, 41), (9, 48), (10, 11), (10, 15), (10, 22), (10, 25), (10, 27), (10, 28), (10, 31), (10, 32), (10, 33), (10, 34), (10, 39), (10, 40), (10, 41), (10, 42), (10, 45), (10, 46), (10, 49), (11, 12), (11, 13), (11, 14), (11, 15), (11, 17), (11, 19), (11, 20), (11, 23), (11, 24), (11, 26), (11, 32), (11, 33), (11, 35), (11, 36), (11, 38), (11, 40), (11, 42), (11, 43), (11, 45), (11, 46), (11, 48), (11, 49), (12, 13), (12, 15), (12, 16), (12, 19), (12, 20), (12, 21), (12, 22), (12, 23), (12, 24), (12, 25), (12, 26), (12, 28), (12, 29), (12, 30), (12, 32), (12, 36), (12, 41), (12, 43), (12, 44), (12, 46), (12, 48), (12, 49), (13, 14), (13, 17), (13, 20), (13, 21), (13, 22), (13, 24), (13, 25), (13, 26), (13, 27), (13, 30), (13, 32), (13, 34), (13, 35), (13, 36), (13, 37), (13, 38), (13, 41), (13, 43), (13, 44), (13, 45), (13, 48), (14, 15), (14, 18), (14, 21), (14, 22), (14, 23), (14, 24), (14, 26), (14, 30), (14, 35), (14, 36), (14, 38), (14, 42), (14, 46), (15, 16), (15, 17), (15, 18), (15, 19), (15, 21), (15, 22), (15, 23), (15, 27), (15, 28), (15, 30), (15, 33), (15, 34), (15, 35), (15, 36), (15, 37), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (15, 45), (15, 47), (15, 49), (16, 18), (16, 19), (16, 21), (16, 24), (16, 27), (16, 31), (16, 33), (16, 34), (16, 35), (16, 36), (16, 37), (16, 41), (16, 44), (16, 46), (16, 47), (16, 48), (17, 18), (17, 19), (17, 21), (17, 22), (17, 26), (17, 29), (17, 30), (17, 34), (17, 35), (17, 37), (17, 39), (17, 40), (17, 41), (17, 42), (17, 43), (17, 44), (17, 45), (17, 46), (17, 49), (18, 23), (18, 26), (18, 27), (18, 28), (18, 29), (18, 31), (18, 33), (18, 34), (18, 37), (18, 41), (18, 42), (18, 43), (18, 45), (18, 47), (18, 49), (19, 20), (19, 21), (19, 22), (19, 23), (19, 24), (19, 29), (19, 31), (19, 38), (19, 41), (19, 42), (19, 43), (19, 44), (19, 45), (19, 49), (20, 23), (20, 24), (20, 25), (20, 30), (20, 32), (20, 33), (20, 36), (20, 37), (20, 38), (20, 39), (20, 40), (20, 41), (20, 42), (20, 44), (20, 47), (21, 22), (21, 23), (21, 27), (21, 30), (21, 31), (21, 32), (21, 33), (21, 38), (21, 41), (21, 42), (21, 43), (21, 49), (22, 23), (22, 24), (22, 25), (22, 26), (22, 29), (22, 33), (22, 36), (22, 37), (22, 43), (22, 45), (22, 46), (22, 48), (23, 24), (23, 25), (23, 29), (23, 32), (23, 33), (23, 34), (23, 35), (23, 36), (23, 37), (23, 40), (23, 43), (23, 47), (24, 26), (24, 27), (24, 28), (24, 32), (24, 33), (24, 34), (24, 36), (24, 38), (24, 42), (24, 43), (24, 44), (24, 48), (24, 49), (25, 26), (25, 27), (25, 28), (25, 29), (25, 30), (25, 31), (25, 33), (25, 34), (25, 35), (25, 36), (25, 37), (25, 39), (25, 40), (25, 42), (25, 43), (25, 44), (25, 46), (25, 47), (25, 48), (26, 27), (26, 31), (26, 34), (26, 38), (26, 39), (26, 41), (26, 42), (26, 44), (26, 45), (26, 48), (27, 29), (27, 31), (27, 33), (27, 34), (27, 35), (27, 41), (27, 43), (27, 46), (27, 47), (28, 29), (28, 31), (28, 33), (28, 34), (28, 35), (28, 38), (28, 40), (28, 44), (28, 47), (29, 31), (29, 32), (29, 33), (29, 34), (29, 35), (29, 37), (29, 38), (29, 41), (29, 44), (29, 45), (29, 49), (30, 32), (30, 33), (30, 34), (30, 37), (30, 39), (30, 42), (30, 43), (30, 46), (30, 47), (30, 48), (30, 49), (31, 32), (31, 33), (31, 34), (31, 36), (31, 39), (31, 40), (31, 43), (31, 45), (31, 46), (31, 49), (32, 36), (32, 37), (32, 38), (32, 39), (32, 41), (32, 43), (32, 44), (32, 47), (33, 34), (33, 38), (33, 39), (33, 41), (33, 43), (33, 44), (33, 47), (33, 49), (34, 35), (34, 37), (34, 38), (34, 39), (34, 40), (34, 42), (34, 46), (34, 49), (35, 36), (35, 38), (35, 41), (35, 42), (36, 38), (36, 43), (36, 47), (36, 49), (37, 38), (37, 39), (37, 42), (37, 44), (37, 46), (37, 47), (37, 48), (38, 39), (38, 40), (38, 42), (38, 43), (38, 44), (38, 45), (38, 47), (38, 48), (39, 41), (39, 43), (39, 46), (39, 47), (39, 48), (40, 41), (40, 43), (40, 44), (40, 49), (41, 42), (41, 43), (41, 44), (41, 46), (41, 48), (41, 49), (42, 45), (42, 46), (42, 47), (43, 44), (43, 48), (43, 49), (44, 45), (44, 47), (45, 47), (46, 47), (47, 48), (47, 49), (48, 49), (49, 50)]
    # type = [9, 5, 2, 10, 4, 9, 1, 2, 6, 7, 8, 1, 9, 5, 5, 4, 1, 1, 10, 6, 7, 10, 10, 6, 9, 4, 3, 9, 1, 9, 3, 2, 10, 2,
    #           5, 10, 4, 4, 8, 5, 10, 2, 3, 9, 1, 2, 9, 2, 10, 1, 1]
    # MS = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    v=[1,3,4,5,6,10,1,11,15,2,1 ]
    e=[(0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,10),(5,10),(6,8),(7,9),(8,10),(9,10) ]
    type=[1,1,2,1,1,2,2,2,1,1,1]
    MS=[2,3]

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
    # print (len(v))
    # print (len(e))
    T=randomDAG.DAGtask(v,e,100,100,0,type)
    rt=findRT(T,MS)
    print ("rt=",rt)


