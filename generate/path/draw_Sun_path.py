import matplotlib.pyplot as plt
import random
from matplotlib.font_manager import FontProperties
import numpy as np
from pylab import mpl

# def draw_2_plots(ret):
#     # 设置显示中文字体
#
#
#     mpl.rcParams["font.sans-serif"] = ["SimHei"]
#
#     temp=ret
#
#     t1=temp[0]
#     accpet1=temp[1]
#     x=temp[2]
#     name = temp[-2]
#     namepic = temp[-1]
#     #if (name == 'U'):
#     #    xlable = x
#     #    for i in range(len(x)):
#     #        x[i] *= 10
#
#     #elif (name == 'HP'):
#
#     #elif (name == 'numP'):
#
#    # elif (name == 'Ndag'):
#
#     #elif (name == 'Pr'):
#
#     for i in range(len(x)) :
#         accpet1[i]*= 10
#
#
#     #输入两个曲线的信息
#     plt.figure( figsize=(8,7))
#     plt.rcParams.update({"font.size":26})
#     ################################################################################################
#
#     plt.plot(x, accpet1, marker='o',color='g', linestyle='-')
#
#
#     #显示图例
#     #plt.legend() #默认loc=Best
#
#     #设置刻度及步长
#     z = range(0,11)
#     ylable=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#     plt.xticks(x[::1])
#     plt.yticks(z[::1],ylable[::1])  #5是步长
#     ax = plt.gca()
#     xmin=ax.xaxis.get_ticklocs()[0]
#     ax.set_xlim(left=xmin)
#     ymin = ax.yaxis.get_ticklocs()[0]
#     ax.set_ylim(ymin)
#     print(xmin,ymin)
#     #添加网格信息
#     plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度
#
#     #添加标题
#     plt.xlabel('${'+name+'}$')
#     plt.ylabel('接受率/%')
#     # plt.title('接受率')
#     plt.savefig("./path_PICTUREs/path1.png".format(namepic),format="png",bbox_inches='tight')
#     #plt.savefig('./调度率比较.png')
#     ###############################################################################################
#
#
#     #################################################################################################
#     plt.figure(figsize=(8, 7))
#     #plt.rcParams.update({"font.size": 26})
#     plt.plot(x, t1, color='g', marker='o',linestyle='-')
#
#     #显示图例
#     #plt.legend() #默认loc=Best
#     plt.xticks(x[::1])
#     ax = plt.gca()
#     xmin = ax.xaxis.get_ticklocs()[0]
#     ax.set_xlim(left=xmin)
#     ymin = ax.yaxis.get_ticklocs()[0]
#     ax.set_ylim(max(ymin,0))
#     #添加网格信息
#     plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度
#
#     #添加标题
#     plt.xlabel('${'+name+'}$')
#     plt.ylabel('执行时间/ms')
#     # plt.title('执行时间')
#
#     plt.savefig("./path_PICTUREs/path2.png".format(namepic),bbox_inches='tight',format="png")
#
#
#     plt.show()
def draw_2_plots(begin,end,ret,options,names,which_parameter):
    # 设置显示中文字体


    mpl.rcParams["font.sans-serif"] = ["Times New Roman"]


    # 进行归一化处理，原版
    # temp =ret
    # [makeTable_Pr,totalrt]
    # [RATE, TIME, RATE_fake, TIME_fake]
    # makeTable_Pr {[RATE][RATE1]
    #               [TIME][TIME1]
    #               [RATE_fake][RATE_fake1]
    #               [TIME_fake][TIME_fake1]
    #               [X值的取值]
    #               pr
    #               pr
    #               }
    temp=ret[0]

    accept=[]
    t=[]
    line_name=[]
    # print("temp",temp)
    for rrr in range(options.count(1)):
        t.append(temp[2*rrr+1])
        accept.append(temp[2*rrr])
    for rrr in range(len(options)):
        if options[rrr] == 1:
            line_name.append(names[rrr])

    # print("path in draw",accept,t,line_name)

    #
    # 原版x间隔1
    x=temp[-3]

    # #修改版X间隔0.5
    # x = []
    # pace = 0.1
    # for i in np.arange(begin, end+pace, pace):
    #     x.append(i)

    name = temp[-2]
    namepic = temp[-1]
    for accept_p in accept:
        for i in range(len(x)):
            accept_p[i]*= 10
    #输入两个曲线的信息
    plt.figure(figsize=(8,7))
    plt.rcParams.update({
        "axes.labelsize": 40,  # 设置轴标签的字体大小
        "xtick.labelsize": 35,  # 设置x轴刻度标签的字体大小
        "ytick.labelsize": 35,  # 设置y轴刻度标签的字体大小
        "legend.fontsize": 30  # 设置图例的字体大小"
    })

    line_style=['-' ,'--','-.', ':']
    color = ['#0000FF', '#A52A2A', '#F5F5DC', '#F0F8FF']
    ################################################################################################
    print("准确性",accept)
    for i in range(len(accept)):
        plt.plot(x, accept[i], color=color[i], marker='o', linestyle=line_style[i], label=line_name[i])

    #显示图例
    plt.legend() #默认loc=Best

    #设置刻度及步长
    z = range(0,11)
    ylable=[0,10,20,30,40,50,60,70,80,90,100]
    plt.xticks(x[::1])
    plt.xticks(rotation=45)
    plt.yticks(z[::1],ylable[::1])  #5是步长
    ax = plt.gca()
    xmin = ax.xaxis.get_ticklocs()[0]
    ax.set_xlim(left=xmin)
    ymin = ax.yaxis.get_ticklocs()[0]
    ax.set_ylim(max(ymin,0))
    #添加网格信息
    plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度
    # 自动调整子图参数，使之填充整个图像区域
    #添加标题
    plt.xlabel(name)
    plt.ylabel('acceptance ratio(%)')
    plt.title('acceptance ratio',fontsize=30)
    plt.savefig("./path_PICTUREs/path1.png".format(namepic),format="png",bbox_inches='tight')
    #plt.savefig('./调度率比较.png')
    # 自动调整子图参数，使之填充整个图像区域
    plt.tight_layout()
    plt.show()




    #################################################################################################
    plt.figure(figsize=(8, 7))
    #plt.rcParams.update({"font.size": 26})
    # plt.plot(x, t1, color='g', marker='o',linestyle='-')
    print("时间",t)
    for i in range(len(t)):
        plt.plot(x, t[i], color=color[i], marker='o', linestyle=line_style[i], label=line_name[i])

    #显示图例
    plt.legend() #默认loc=Best
    plt.xticks(x[::1])
    plt.xticks(rotation=45)
    ax = plt.gca()
    xmin = ax.xaxis.get_ticklocs()[0]
    ax.set_xlim(left=xmin)
    ymin = ax.yaxis.get_ticklocs()[0]
    ax.set_ylim(max(ymin,0))
    #添加网格信息
    plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度

    #添加标题
    plt.xlabel(name)

    plt.ylabel('execution time(ms)')
    plt.title('execution time',fontsize=30)

    plt.savefig("./path_PICTUREs/path3.png".format(namepic),bbox_inches='tight',format="png")

    plt.tight_layout()
    plt.show()



    # # 归一化计算部分
    # print(len(ret[1]))
    #
    #
    # plt.figure(figsize=(8, 7))
    # # plt.rcParams.update({"font.size": 26})
    # # plt.plot(x, t1, color='g', marker='o',linestyle='-')
    #
    # y_values = ret[1]
    #
    # for i in range(len(x)):
    #     y_values[i] = y_values[i] * 100
    #
    # plt.plot(x, y_values, color='#0000FF', marker='o', linestyle='-', label = '归一化处理结果')
    # # # 添加数据标签显示归一化程度的百分比
    # # for i in range(len(x)):
    # #     plt.text(x[i], y_values[i], f'{y_values[i]:.2f}%', ha='center', va='bottom', fontsize=24)
    #
    # # 图例
    # plt.legend()
    # plt.xticks(x[::1])
    #
    # # # 在对于MS的实验里面间隔是5
    # # plt.xticks(x[::5])
    #
    # plt.xticks(rotation=45)
    # # 添加标题和坐标轴标签
    # # plt.title("归一化处理结果")  # 图形标题
    # plt.xlabel(name)  # x轴标签
    # plt.ylabel('归一化处理结果(%)')  # y轴标签
    # # 设置网格线
    # plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # 显示网格线
    # plt.savefig("./path_PICTUREs/path4.png".format(namepic), bbox_inches='tight', format="png")
    # # 自动调整子图参数，使之填充整个图像区域
    # plt.tight_layout()
    # plt.show()

    ################################################################################################
    # 关于ntuple的散点图

    plt.figure(figsize=(8, 7))
    num1 = ret[2]
    num2 = ret[3]
    # 生成一个小的随机偏移
    offset = 2 * (np.random.rand(len(x)) - 0.5)

   # 绘制 num1 散点图
    first_label_set = False
    for xe, ye in zip(x + offset, num1):
        label = "ddd" if not first_label_set else ""
        plt.scatter([xe] * len(ye), ye, color='#0000FF', marker='o', linestyle='-', label=label)
        if not first_label_set:
            first_label_set = True

# 绘制 num2 散点图
    first_label_set = False
    for xe, ye in zip(x - offset, num2):
        label = "eeew" if not first_label_set else ""
        plt.scatter([xe] * len(ye), ye, color='#FF0000', marker='x', linestyle='-', label=label)
        if not first_label_set:
            first_label_set = True

    # 显示图例
    plt.legend()  # 默认loc=Best

    # 显示图例
    plt.legend()  # 默认loc=Best
    plt.xticks(x[::1])
    plt.xticks(rotation=45)

    # 添加网格信息
    plt.grid(True, linestyle='--', alpha=0.5)  # 默认是True，风格设置为虚线，alpha为透明度

    # 添加标题
    # plt.xlabel(name)
    plt.xlabel(r'$M^\gamma$')
    plt.ylabel("number of ntuple")


    plt.savefig("./path_PICTUREs/path.pdf".format(namepic), bbox_inches='tight', format="pdf")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    temp=[

        # [5.94, 7.66, 9.41, 11.46, 14.24, 16.26, 16.18, 16.08, 14.13, 11.87, 10.58, 7.93, 7.57, 5.77, 5.09],
        # [1.0, 1.0, 0.98, 0.95, 0.88, 0.75, 0.47, 0.29, 0.12, 0.03, 0.01, 0.0, 0.0, 0.0, 0.0],
        # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        # "N",
        # "numtask"
        [1.0, 1.0, 0.98, 0.94, 0.85, 0.73, 0.57, 0.39, 0.24, 0.13],
        [110.16, 140.18, 177.34, 223.29, 273.56, 339.86, 405.89, 405.73, 433.28, 452.73],
        [1.0, 1.0, 0.99, 0.97, 0.88, 0.8, 0.63, 0.47, 0.31, 0.16],
        [126.83, 168.51, 222.16, 273.44, 322.67, 394.22, 468.55, 479.46, 511.73, 542.79],
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        'N',
        'numtask'

    ]
    names = ["Basic_FP", "Imp_FP"]
    draw_2_plots(15,31,temp,[1,1],names,1)

    temp=[[1.0, 1.0, 0.98, 0.94, 0.85, 0.73, 0.57, 0.39, 0.24, 0.13],
          [110.16, 140.18, 177.34, 223.29, 273.56, 339.86, 405.89, 405.73, 433.28, 452.73],
          [1.0, 1.0, 0.99, 0.97, 0.88, 0.8, 0.63, 0.47, 0.31, 0.16],
          [126.83, 168.51, 222.16, 273.44, 322.67, 394.22, 468.55, 479.46, 511.73, 542.79],
          [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
          'N', 'numtask'
          ]
    # path in draw[
    #     [1.0, 1.0, 0.98, 0.94, 0.85, 0.73, 0.57, 0.39, 0.24, 0.13], [1.0, 1.0, 0.99, 0.97, 0.88, 0.8, 0.63, 0.47, 0.31,
    #                                                                  0.16]][
    #     [110.16, 140.18, 177.34, 223.29, 273.56, 339.86, 405.89, 405.73, 433.28, 452.73], [126.83, 168.51, 222.16,
    #                                                                                        273.44, 322.67, 394.22,
    #                                                                                        468.55, 479.46, 511.73,
    #                                                                                        542.79]][
    #     'Basic_FP', 'Imp_FP']



