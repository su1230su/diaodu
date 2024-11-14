from __future__ import division
import math


INF = 100000


# import workloadcal
# ICI（Interrupt Time of Current Task） 任务的中断时间
def ICI(task, Ri, x):
    t=task[1]
    c=task[0]
    # t = task.Ti
    # c = task.Ci
    # math.floor x向下取整
    #中断时间=等待时间+任务执行时间+等待周期时间
    # c:任务的执行时间
    # t：周期
    # Ri：上一个任务的响应时间
    # x：当前时间
    Ici = math.floor(max((x - c), 0) / t) * c + c + min(max(max((x - c), 0) % t - (t - Ri), 0), c)

    return Ici


# Calculate Interrupt time of task set which do not includes carry in tasks
# 计算不包括Carry-in任务的任务集中的中断时间
def NCI(task, x):
    t = task[1]
    c = task[0]
    # t = task.Ti
    # c = task.Ci
    Nci = math.floor(x / t) * c + min(x % t, c)
    return Nci


# Calculate total Interrupt time of task set
# 计算任务集的总中断时间
# cpunum:cpu的个数、Tests:任务集、RT:任务的响应时间、C_k:任务的执行时间、X:当前时间
def TotalInt(cpunum, Tsets, RT,C_k, x):
    Idiff = []
    sum1 = 0
    sum2 = 0
    n = len(Tsets)                 # 任务集合中任务个数
    limited=max(0,x - C_k + 1)      # 计算的限制值

    # 循环遍历每一个任务
    for i in range(0, n):
        # Calculate total Interrupt time of task set which do not include carry in tasks
        wnci = NCI(Tsets[i], x)
        nci = min(wnci, limited)
        # print ("NC%d=%d"%(i+1,nci))
        sum1 = sum1 + nci
    # 循环遍历任务（除了最后一个任务）
    for i in range(0, n - 1):
        # Calculate total Interrupt time of task set which includes carry in tasks
        nci = min(NCI(Tsets[i], x), limited)
        wici = ICI(Tsets[i], RT[i], x)
        # print wici
        ici = min(wici, limited)
        # print ("IC%d=%d"%(i+1,ici))
        # print "Idiff%d=%d"%(i+1,ici-nci)
        # 时间差异值，包含carry-in的减去不包含carry-in的
        Idiff.append(ici - nci)
        # if ResponseTSet[len(ResponseTSet)-1]==0:

        # total=INF
    # else:
    # 循环到CPU个数等于1
    while cpunum - 1:
        d = max(Idiff)
        sum2 = sum2 + d
        Idiff.remove(d)
        cpunum -= 1
    # print "sum1=%d"%(sum1)
    # print "sum2=%d"%(sum2)
    total = sum1 + sum2
    return total

# 计算响应时间
# M:CPU的个数、Tests:任务集合
def cal_RT(M, Tsets):

    # n = len(Tsets)

    # print "n=%d"%(n)

    # if len(ResponseTSet) == 0:
    ResponseTSet = []
    for i in range(0, len(Tsets)):
        # 对于前 M 个任务，直接将任务的执行时间 Ci 作为响应时间
        if i<M:
            # print("i=%d"%i)
            rt = Tsets[i][0]
            # ResponseTSet.append(rt)
            # print ("R%d=%d"%(i+1,rt))
    # if n <= M:
    #     x = ResponseTSet[n - 1]
        else:
            if ResponseTSet[i-1]==0:
                rt=0
            else:
                C_k = Tsets[i][0]       # C_K执行时间
                D_k = Tsets[i][2]       # D_K截止时间
                # C_k = Tsets[n - 1].Ci
                # D_k = Tsets[n - 1].Ti
                Tsets_tmp = []          # 存储优先级高的任务
                y = 0
                x = C_k
                # 取出高优先级任务集
                for j in range(0, i):
                    Tsets_tmp.append(Tsets[j])

                while (x != y and x <= D_k):
                    # if x>D:break
                    y = x
                    # print ("x=%d"%(x))
                    total = TotalInt(M, Tsets_tmp, ResponseTSet,C_k, y)
                    # print ("total=%d"%(total))
                    x = math.floor(total / M) + C_k
                    rt=x
                    # print ("x=%d"%(x))

                if x != y:
                    rt = 0
        ResponseTSet.append(rt)
    return ResponseTSet


if __name__ == '__main__':
    M = 2
    str="CPUNUM=%d" % (M)
    print (str)
    Tsets = [(13, 15,15), (41, 45,45), (52, 53,53), (48, 94,94), (38, 98,98)]
    # M=1
    # Tsets=[(41, 45, 45), (52, 53, 53)]
    rk = cal_RT(M, Tsets)
    print (rk)

