import randomDAG
import copy


# 通过分析任务图中的依赖关系，从给定的任务中生成的前驱结点列表。
def refinefaV(task):
    # 获取任务图中每个结点的祖先结点列表，存储在变量 anceV 中。
    anceV= randomDAG.findpcoDAG().findpa(task.V, task.E)
    # 存储所有的前驱结点的列表
    preV = []
    # 任务图中结点的数量
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            # 判断依赖关系，是否存在边（j,i）
            if (j, i) in task.E:
                temp.append(j)
        # 更新前驱结点列表
        preV.append(temp)
    # print('preV=',preV)
    # 复制preV的数据到faV
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

# 计算任务的ui值,ui类似于权重决定任务调度的优先级
def cal_ui(task):
    tU=0.0
    for v in task.V:
        # 求累计的ui值，ui=结点的执行时间v/任务周期task.Ti
        tU=tU+v/task.Ti
    return tU

def Sche_hp(Thp,Ms):
    lens = len(Thp)
    U=[]
    for i in range(lens):
        # 获取任务结点数量
        lent = len(Thp[i].V)
        Ui = []
        # 计算出结点的ui值并且将其放在Ui列表中
        for j in range(0, lent):
            u = Thp[i].V[j] / Thp[i].Ti
            Ui.append(u)
        U.append(Ui)
    Mhp=[]
    Mr=Ms
    lenp=len(Ms)
     #     initial Mhp and Mr




# 计算响应时间（response time）
def findRT(Tsets,Ms):
    # 先获取任务的数量
    lens = len(Tsets)
    # 存储高优先级任务
    Thp=[]
    # 存储低优先级任务
    Tlp=[]
    for i in range (lens):
        # 利用函数cal_ui计算出ui值存储在Ui列表里
        Ui=cal_ui(Tsets[i])
        # 依据任务的ui值对任务进行分类在
        # ui>1时，归于Thp；在ui<1时，归于Tlp
        if Ui>1:
            Thp.append(Tsets[i])
        else:
            Tlp.append(Tsets[i])
    # assiment cores to tasks in Thp
    re_hp=Sche_hp(Tlp,Ms)
    if re_hp[0]==0:
        return 0
    else:
        re_lp=Sche_lp(Tlp,re_hp[1])
    if re_lp==0:
        return 0
    else:
        # get the response time of each task.
        return 1
