import matplotlib.pyplot as plt
import random

import numpy as np
from pylab import mpl


def draw_2_plots(begin,end,pace,temp1,temp2,names,name,namepic,ret):
    # 设置显示中文字体


    mpl.rcParams["font.sans-serif"] = ["Times New Roman"]
    line_name =names
    accept = temp1

    # 控制横坐标X的范围
    x = []

    for i in np.arange(begin, end+pace, pace):
        x.append(i)
    print(x)

    #输入两个曲线的信息
    plt.figure(figsize=(8,7))
    # plt.rcParams.update({"font.size":35,})

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
    plt.yticks(z[::2],ylable[::2])
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

    # # 关于Ms的标签设置
    plt.xlabel(r'$M^\gamma$')

    plt.ylabel('acceptance ratio(%)')
    # plt.title('acceptance ratio', fontsize=30)
    plt.savefig("./path_PICTUREs/path1.pdf".format(namepic),format="pdf",bbox_inches='tight')
    #plt.savefig('./调度率比较.png')
    # 自动调整子图参数，使之填充整个图像区域
    plt.tight_layout()
    plt.show()



    #################################################################################################
    plt.figure(figsize=(8, 7))

    t=temp2
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

    plt.xlabel(r'$M^\gamma$')
    plt.ylabel('execution time(ms)')
    # plt.title('execution time', fontsize = 30)

    plt.savefig("./path_PICTUREs/path3.pdf".format(namepic),bbox_inches='tight',format="pdf")

    plt.tight_layout()
    plt.show()

    # 归一化计算部分
    print("lenret=",len(ret))
    plt.figure(figsize=(8, 7))


    y_values = ret



    plt.plot(x, y_values, color='#0000FF', linestyle='-')

    # 图例




    plt.xticks(x[::1])

    # # 在对于MS的实验里面间隔是5
    # plt.xticks(x[::5])

    plt.xticks(rotation=45)
    # 添加标题和坐标轴标签
    # plt.title("归一化处理结果")  # 图形标题

    plt.xlabel(name)  # x轴标签
    plt.xlabel(r'$M^\gamma$')

    plt.ylabel('normalization degree(%)')  # y轴标签

    # 设置网格线
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # 显示网格线
    plt.savefig("./path_PICTUREs/path4.pdf".format(namepic), bbox_inches='tight', format="pdf")
    # 自动调整子图参数，使之填充整个图像区域
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    temp1 =  [[0.6, 2.1, 3.9000000000000004, 5.8, 7.7, 8.7, 9.200000000000001, 9.5, 9.8, 9.9, 10.0], [0.8, 2.6, 4.4, 6.5, 8.299999999999999, 9.1, 9.5, 9.7, 9.9, 10.0, 10.0]]
    temp2 =  [[195.14, 228.88, 241.82, 254.33, 256.64, 256.84, 255.1, 251.82, 250.96, 253.02, 247.3], [234.85, 274.09, 288.74, 305.56, 307.79, 308.11, 303.8, 301.31, 302.95, 305.9, 300.15]]
    begin = 10
    end = 30
    pace = 2
    # names = ["G-EDF", "YANG"]
    names = ["Basic-FP", "Imp-FP"]
    name = "N"
    namepic = "N"

    ret = [2.8, 2.83, 2.5, 2.23, 1.82, 1.5, 0.91, 0.75, 0.51, 0.245, 0.2]
    draw_2_plots(begin,end,pace,temp1,temp2,names,name,namepic,ret)




