from __future__ import division
import math

#求 vol（s）（Gi）
def vol(s,task,cpunum):
    sum=0
    length=len(task.typeddag[s])
    for i in range(length):
        sum+=task.typeddag[s][i]
    return sum


# Calculate total Interrupt time of task set
# def TotalInt(s,cpunum, Tsets, RT, x):
#
#     sum = 0
#     n = len(Tsets)
#     # 打印Tsets
#     print(Tsets)
#     for i in range(0, n):
#
#         voli = vol(s,Tsets[i],cpunum)
#
#
#         # 打印基础信息
#         print((x-voli/cpunum),"&&&",Tsets[i].Ti)
#         a=min(voli,max(0,cpunum*((x-voli/cpunum)%Tsets[i].Ti-(Tsets[i].Ti-RT[i]))))
#
#         b=(math.floor((x-voli/cpunum)/Tsets[i].Ti) + 1)*voli
#
#         sum=sum+a+b
#
#     return sum



#Wi
def TotalInt(s,cpunum, Tsets, RT, x):

    sum = 0
    n = len(Tsets)
    # 打印Tsets
    # print(Tsets)
    for i in range(0, n):

        voli = vol(s,Tsets[i],cpunum)


        # 打印基础信息
        # print((x-voli/cpunum),"&&&",Tsets[i].Ti)
        a=min(voli,max(0,cpunum*((x-voli/cpunum)%Tsets[i].Ti-(Tsets[i].Ti-RT[i]))))

        b=(math.floor((x-voli/cpunum)/Tsets[i].Ti) + 1)*voli

        sum=sum+a+b

    return sum


def totalInt1(s, cpunum, Tsets, RT, x):

    sum = 0
    n = len( Tsets)
    for i in range(0,n):
        voli = vol(s,Tsets[i],cpunum)

        a = min(voli,cpunum*((x + RT[i] - voli / cpunum)%Tsets[i].Ti))
        b = (math.floor(max(0, x + RT[i] -voli)/Tsets[i].Ti)) * voli /cpunum

        sum = sum + a + b
    return sum


# Wi_edf
def totalInt2(s, cpunum, Tsets,RT,D_k):

    sum = 0
    n = len(Tsets)
    for i in range (0,n):
        voli = vol(s, Tsets[i], cpunum)
        a = min(voli , cpunum*max(0, D_k % Tsets[i].Ti - Tsets[i].Di + RT[i]))
        b = (math.floor((D_k - Tsets[i].Di) / Tsets[i].Ti) + 1)*voli

        sum =sum + a + b

    return sum
