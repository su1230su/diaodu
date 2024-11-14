
import matplotlib.pyplot as plt

import pickle

plt.figure(figsize=(6, 6))


def readpickles(filename):
    ofile=open(filename,'rb')
    lines=pickle.load(ofile,encoding='bytes')

    return lines


# [X,accbrt1,accnrt2,accnrt4,rt12,rt14,rt24,diff12,diff14,diff24,Tsetsnum,Umax]
#methods has bs,imp,dp,tp
# 计算准确率
def cal_acc(filename):
    bl_acc_ratio = []
    imp_acc_ratio=[]
    # dp_acc_ratio= []
    # tp_acc_ratio = []
    lines=readpickles(filename)

    X=lines[0]
    bl=lines[1]
    # nw=lines[2]
    imp=lines[2]
    # dp = lines[3]
    # tp = lines[4]
    tsetsnum=lines[6]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_acc_ratio.append(bl[i] / tsetsnum[i])
        imp_acc_ratio.append(imp[i] / tsetsnum[i])
        # dp_acc_ratio.append(dp[i] / tsetsnum[i])
        # tp_acc_ratio.append(tp[i] / tsetsnum[i])
    # , dp_acc_ratio, tp_acc_ratio
    return X, bl_acc_ratio,imp_acc_ratio

# 同时计算多个准确率
def cal_yacc(filename):
    bl_acc_ratio = []
    imp_acc_ratio=[]
    dp_acc_ratio= []
    tp_acc_ratio = []
    yd_acc_ratio=[]
    lines=readpickles(filename)

    X=lines[0]
    bl=lines[1]
    # nw=lines[2]
    imp=lines[2]
    dp = lines[3]
    tp = lines[4]
    yd=lines[13]
    tsetsnum=lines[12]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_acc_ratio.append(bl[i] / tsetsnum[i])
        imp_acc_ratio.append(imp[i] / tsetsnum[i])
        dp_acc_ratio.append(dp[i] / tsetsnum[i])
        tp_acc_ratio.append(tp[i] / tsetsnum[i])
        yd_acc_ratio.append(yd[i]/tsetsnum[i])
    return X, bl_acc_ratio,imp_acc_ratio, dp_acc_ratio,tp_acc_ratio,yd_acc_ratio

# 计算效率
def cal_eff(filename):
    bl_eff_ratio = []
    imp_eff_ratio=[]
    # dp_eff_ratio= []
    # tp_eff_ratio = []
    lines=readpickles(filename)
    X=lines[0]
    bl=lines[4]
    # nw=lines[2]
    imp=lines[5]
    # dp = lines[10]
    # tp = lines[11]
    tsetsnum=lines[6]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        # dp_eff_ratio.append(dp[i] / tsetsnum[i])
        # tp_eff_ratio.append(tp[i] / tsetsnum[i])
    # , dp_eff_ratio, tp_eff_ratio
    return X, bl_eff_ratio,imp_eff_ratio
# 计算响应时间
def cal_rtr(filename):

    imp_eff_ratio=[]
    # dp_eff_ratio= []
    # tp_eff_ratio = []
    lines=readpickles(filename)

    X=lines[0]
    # nw=lines[2]
    imp=lines[3]
    # dp = lines[6]
    # tp = lines[7]
    tsetsnum=lines[6]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        # bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        # dp_eff_ratio.append(dp[i] / tsetsnum[i])
        # tp_eff_ratio.append(tp[i] / tsetsnum[i])
 # , dp_eff_ratio, tp_eff_ratio
    return X, imp_eff_ratio

# 同时计算多个响应时间
def cal_yrtr(filename):

    imp_eff_ratio=[]
    dp_eff_ratio= []
    tp_eff_ratio = []
    yd_eff_ratio=[]
    lines=readpickles(filename)

    X=lines[0]
    # nw=lines[2]
    imp=lines[5]
    dp = lines[6]
    tp = lines[7]
    tsetsnum=lines[12]
    yd=lines[14]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        # bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        dp_eff_ratio.append(dp[i] / tsetsnum[i])
        tp_eff_ratio.append(tp[i] / tsetsnum[i])
        yd_eff_ratio.append(yd[i]/tsetsnum[i])

    return X, imp_eff_ratio, dp_eff_ratio,tp_eff_ratio,yd_eff_ratio

#3-d plot
# 计算准确率指标
def cal_accprpn(filename):
    bl_acc_ratio = []
    imp_acc_ratio=[]
    dp_acc_ratio= []
    tp_acc_ratio = []
    lines=readpickles(filename)

    X=lines[0]
    Y=lines[1]
    bl=lines[2]
    # nw=lines[2]
    imp=lines[3]
    dp = lines[4]
    tp = lines[5]
    tsetsnum=lines[13]
    # m=lines[11]
    for i in range(0, len(bl)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_acc_ratio.append(bl[i] / tsetsnum[i])
        imp_acc_ratio.append(imp[i] / tsetsnum[i])
        dp_acc_ratio.append(dp[i] / tsetsnum[i])
        tp_acc_ratio.append(tp[i] / tsetsnum[i])

    return X,Y, bl_acc_ratio,imp_acc_ratio, dp_acc_ratio,tp_acc_ratio

# 计算效率指标
def cal_effprpn(filename):
    bl_eff_ratio = []
    imp_eff_ratio=[]
    dp_eff_ratio= []
    tp_eff_ratio = []
    lines=readpickles(filename)

    X=lines[0]
    Y=lines[1]
    bl=lines[9]
    # nw=lines[2]
    imp=lines[10]
    dp = lines[11]
    tp = lines[12]
    tsetsnum=lines[13]
    # m=lines[11]
    for i in range(0, len(dp)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        dp_eff_ratio.append(dp[i] / tsetsnum[i])
        tp_eff_ratio.append(tp[i] / tsetsnum[i])

    return X, Y,bl_eff_ratio,imp_eff_ratio, dp_eff_ratio,tp_eff_ratio

# 计算响应时间指标
def cal_rtrprpn(filename):

    imp_rtr_ratio=[]
    dp_rtr_ratio= []
    tp_rtr_ratio = []
    lines=readpickles(filename)

    X=lines[0]
    Y=lines[1]
    imp=lines[6]
    dp = lines[7]
    tp = lines[8]
    tsetsnum=lines[13]

    for i in range(0, len(dp)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        # bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_rtr_ratio.append(imp[i] / tsetsnum[i])
        dp_rtr_ratio.append(dp[i] / tsetsnum[i])
        tp_rtr_ratio.append(tp[i] / tsetsnum[i])

    return X, Y,imp_rtr_ratio, dp_rtr_ratio,tp_rtr_ratio


#with the exect wcrt results
'''
计算不同算法/方法的准确性指标，同时考虑了额外的响应时间数据。
从pickle文件中读取数据并计算每种方法的准确性，包括额外的响应时间数据。
返回X坐标和每种方法的准确性值，包括额外的响应时间数据
'''
def cal_accrt(filename):
    bl_acc_ratio = []
    imp_acc_ratio=[]
    dp_acc_ratio= []
    tp_acc_ratio = []
    wc_acc_ratio=[]
    lines=readpickles(filename)

    X=lines[0]
    bl=lines[1]
    # nw=lines[2]
    imp=lines[2]
    dp = lines[3]
    tp = lines[4]
    wc=lines[14]
    tsetsnum=lines[12]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_acc_ratio.append(bl[i] / tsetsnum[i])
        imp_acc_ratio.append(imp[i] / tsetsnum[i])
        dp_acc_ratio.append(dp[i] / tsetsnum[i])
        tp_acc_ratio.append(tp[i] / tsetsnum[i])
        wc_acc_ratio.append(wc[i]/tsetsnum[i])

    return X, bl_acc_ratio,imp_acc_ratio, dp_acc_ratio,tp_acc_ratio,wc_acc_ratio
'''
计算不同算法/方法的效率指标，同时考虑了额外的响应时间数据。
'''
def cal_effrt(filename):
    bl_eff_ratio = []
    imp_eff_ratio=[]
    dp_eff_ratio= []
    tp_eff_ratio = []
    wc_eff_ratio=[]
    lines=readpickles(filename)

    X=lines[0]
    bl=lines[8]
    # nw=lines[2]
    imp=lines[9]
    dp = lines[10]
    tp = lines[11]
    wc=lines[16]
    tsetsnum=lines[12]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        dp_eff_ratio.append(dp[i] / tsetsnum[i])
        tp_eff_ratio.append(tp[i] / tsetsnum[i])
        wc_eff_ratio.append(wc[i]/tsetsnum[i])

    return X, bl_eff_ratio,imp_eff_ratio, dp_eff_ratio,tp_eff_ratio,wc_eff_ratio
def cal_rtrrt(filename):

    imp_eff_ratio=[]
    dp_eff_ratio= []
    tp_eff_ratio = []
    wc_eff_ratio=[]
    lines=readpickles(filename)

    X=lines[0]
    # nw=lines[2]
    imp=lines[5]
    dp = lines[6]
    tp = lines[7]
    wc=lines[15]
    tsetsnum=lines[12]
    # m=lines[11]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        # bl_eff_ratio.append(bl[i] / tsetsnum[i])
        imp_eff_ratio.append(imp[i] / tsetsnum[i])
        dp_eff_ratio.append(dp[i] / tsetsnum[i])
        tp_eff_ratio.append(tp[i] / tsetsnum[i])
        wc_eff_ratio.append(wc[i]/tsetsnum[i])

    return X, imp_eff_ratio, dp_eff_ratio,tp_eff_ratio,wc_eff_ratio

# prpn readickle





def cal_accpr(filename):
    orta_acc_ratio = []
    nta_acc_ratio2=[]
    nta_acc_ratio5= []
    nta_acc_ratiolp= []
    lines=readpickles(filename)

    X=lines[0]
    no=lines[1]
    # nw=lines[2]
    ng=lines[2]
    ng4 = lines[3]
    ng5=lines[4]
    tsetsnum=lines[9]
    for i in range(0, len(X)):
        # if tsetsnum[i]==0:
        #     tsetsnum[i]=3000
        orta_acc_ratio.append(no[i] / tsetsnum[i])
        # wrta_acc_ratio.append(nw[i] / tsetsnum[i])
        # gta_acc_ratio.append(ng[i] / tsetsnum[i])
        nta_acc_ratio2.append(ng[i]/tsetsnum[i])
        # nta_acc_ratio3.append(ng3[i] / tsetsnum[i])
        nta_acc_ratio5.append(ng4[i] / tsetsnum[i])
        nta_acc_ratiolp.append(ng5[i] / tsetsnum[i])
    return X, orta_acc_ratio,nta_acc_ratio2,nta_acc_ratio5,nta_acc_ratiolp



# 平均准确率指标
def cal_averimp(filename):
    # [X, on, gn, nn, dog, nog, don, non, dgn, ngn, TN, TNS]
    ogratio=[]
    onratio=[]
    ngratio=[]
    results =readpickles(filename)
    X = results[0]
    ogd = results[4]
    ogn = results[5]
    ond = results[6]
    onn = results[7]
    ngd = results[8]
    ngn = results[9]
    for i in range(0,len(ogd)):
        if ogn[i]==0:
            ogn[i]=1
        if onn[i]==0:
            onn[i]=1
        if ngn[i]==0:
            ngn[i]=1
        ogratio.append(ogd[i]/ogn[i])
        onratio.append(ond[i]/onn[i])
        ngratio.append(ngd[i]/ngn[i])
    return X,ogratio,onratio,ngratio

# 计算多种情况下的平均准确率
def cal_averimpallT(filename):
    imprt12=[]
    imprt14 = []
    imprt24 = []
    results = readpickles(filename)
    X = results[0]
    rt12 = results[4]
    rt14 = results[5]
    rt24 = results[6]
    Tsetsnum=results[10]
    for i in range(0, len(X)):
        imprt12.append(rt12[i] / Tsetsnum[i])
        imprt14.append(rt14[i] / Tsetsnum[i])
        imprt24.append(rt24[i] / Tsetsnum[i])
    return X, imprt12,imprt14,imprt24

# 计算不同方法性能提升指标
def cal_imp(filename):
    # [X, on, gn, nn, dog, nog, don, non, dgn, ngn, TN, TNS]
    imp12=[]
    imp14=[]
    imp24 = []
    results =readpickles(filename)
    X = results[0]
    ogd = results[1]
    ogn = results[2]
    ond = results[3]
    Tsetsnum=results[10]
    for i in range(0,len(ogd)):
        imp12.append((ogn[i]-ogd[i])/Tsetsnum[i])
        imp14.append((ond[i] - ogd[i]) / Tsetsnum[i])
        imp24.append((ond[i] - ogn[i]) / Tsetsnum[i])
    return X,imp12,imp14,imp24




