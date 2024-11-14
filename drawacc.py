
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import readpickle




# 任务调度的图表
def drawu( filelist):

    for (filename) in filelist:
        results = readpickle.cal_acc(filename)
        m=results[len(results)-1]

        X = [tmp  for tmp in results[0]]
        Z1 = [tmp * 100 for tmp in results[1]]
        Z2 = [tmp * 100 for tmp in results[2]]
        # Z3 = [tmp * 100 for tmp in results[3]]
        # Z4 = [tmp * 100 for tmp in results[4]]
        # Z5=[tmp*100 for tmp in results[5]]

        print(X)
        print(Z1)
        print(Z2)
        # print (Z3)
        # print(Z4)
        # print(Z5)

        plt.figure(figsize=(11, 8))
        plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
        plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
        # plt.plot(X, Z3, 'b', linestyle='-', marker='+', lw=2, label='Acc-Approx')
        # plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
        # plt.plot(X, Z5, 'b', linestyle='-.', marker='+', lw=2, label='Yang-Method')

        plt.xlabel('$U$', fontsize=30)
        # plt.xlabel('The range of pr', fontsize=30)
        # plt.xlabel('The number of vertices', fontsize=30)
        # plt.xlabel('The range of pn', fontsize=30)
        plt.ylabel('Acceptance ratio(%)', fontsize=30)

        plt.legend(loc="upper right", title='', fontsize=27,
                   shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

        # plt.legend(loc="lower right", title='', fontsize=20,
        #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
        plt.ylim(0, 100)
        plt.grid(True)
        plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

# 关于pr的图表，其中 x 轴表示 pr：任务生成概率，y 轴表示任务的接受率
def drawpr( filelist):

    for (filename) in filelist:
        results = readpickle.cal_yacc(filename)
        m=results[len(results)-1]

        X = [tmp  for tmp in results[0]]
        Z1 = [tmp * 100 for tmp in results[1]]
        Z2 = [tmp * 100 for tmp in results[2]]
        Z3 = [tmp * 100 for tmp in results[3]]
        Z4 = [tmp * 100 for tmp in results[4]]
        Z5=[tmp*100 for tmp in results[5]]

        print(X)
        print(Z1)
        print(Z2)
        print (Z3)
        print(Z4)
        print(Z5)

        plt.figure(figsize=(11, 8))
        plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
        plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
        # plt.plot(X, Z3, 'b', linestyle='-', marker='+', lw=2, label='Acc-Approx')
        plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
        plt.plot(X, Z5, 'b', linestyle='-.', marker='+', lw=2, label='Yang-Method')
        # plt.plot(X, Z3, 'b', linestyle='-.', marker='+', lw=4, label='Acc-Approx')

        # plt.xlabel('The utilization range', fontsize=30)
        plt.xlabel('$pr$', fontsize=30)
        # plt.xlabel('The number of vertices', fontsize=30)
        # plt.xlabel('The range of pn', fontsize=30)
        plt.ylabel('Acceptance ratio(%)', fontsize=30)

        plt.legend(loc="upper right", title='', fontsize=27,
                   shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

        # plt.legend(loc="lower right", title='', fontsize=20,
        #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
        plt.ylim(0, 100)
        plt.grid(True)
        plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

# 节点数量V的图表，
def drawN( filelist):

    for (filename) in filelist:
        results = readpickle.cal_yacc(filename)
        m=results[len(results)-1]

        X = [tmp  for tmp in results[0]]
        Z1 = [tmp * 100 for tmp in results[1]]
        Z2 = [tmp * 100 for tmp in results[2]]
        Z3 = [tmp * 100 for tmp in results[3]]
        Z4 = [tmp * 100 for tmp in results[4]]
        Z5=[tmp*100 for tmp in results[5]]

        print(X)
        print(Z1)
        print(Z2)
        print (Z3)
        print(Z4)
        print(Z5)

        plt.figure(figsize=(11, 8))
        plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
        plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
        # plt.plot(X, Z3, 'b', linestyle='-', marker='+', lw=2, label='Acc-Approx')
        plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
        plt.plot(X, Z5, 'b', linestyle='-.', marker='+', lw=2, label='Yang-Method')
        # plt.plot(X, Z3, 'b', linestyle='-.', marker='+', lw=4, label='Acc-Approx')

        # plt.xlabel('The utilization range', fontsize=30)
        # plt.xlabel('The range of pr', fontsize=30)
        plt.xlabel('$|V|$', fontsize=30)
        # plt.xlabel('The range of pn', fontsize=30)
        plt.ylabel('Acceptance ratio(%)', fontsize=30)

        plt.legend(loc="lower right", title='', fontsize=27,
                   shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

        # plt.legend(loc="lower right", title='', fontsize=20,
        #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
        plt.ylim(0, 100)
        plt.grid(True)
        plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])


# 关于任务集合大小S的图表
def drawpn( filelist):

    for (filename) in filelist:
        results = readpickle.cal_yacc(filename)
        m=results[len(results)-1]

        X = [tmp  for tmp in results[0]]
        Z1 = [tmp * 100 for tmp in results[1]]
        Z2 = [tmp * 100 for tmp in results[2]]
        Z3 = [tmp * 100 for tmp in results[3]]
        Z4 = [tmp * 100 for tmp in results[4]]
        Z5=[tmp*100 for tmp in results[5]]

        print(X)
        print(Z1)
        print(Z2)
        print (Z3)
        print(Z4)
        print(Z5)

        plt.figure(figsize=(11, 8))
        plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
        plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
        # plt.plot(X, Z3, 'b', linestyle='-', marker='+', lw=2, label='Acc-Approx')
        plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
        plt.plot(X, Z5, 'b', linestyle='-.', marker='+', lw=2, label='Yang-Method')

        # plt.xlabel('The utilization range', fontsize=30)
        # plt.xlabel('The range of pr', fontsize=30)
        # plt.xlabel('The number of vertices', fontsize=30)
        plt.xlabel('$|S|$', fontsize=30)
        plt.ylabel('Acceptance ratio(%)', fontsize=30)

        plt.legend(loc="upper right", title='', fontsize=27,
                   shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

        # plt.legend(loc="lower right", title='', fontsize=20,
        #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
        plt.ylim(0, 100)
        plt.grid(True)
        plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])


if __name__ == '__main__':
    drawu([('.\\test.pickle')
            ])
    # drawpr([('.\\tupleresult\\yresult\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle'),
    #         ])
    # drawN([('.\\tupleresult\\fresult\\range\\raneffN=65-10pn=8-10pr=008-04ms=2-11u=1-3.pickle'),
    #        # ('.\\tupleresult\\fresult\\tianqiu\\N=65-10pn=5-10pr=008-01ms=2-11u=1-3.pickle'),
    #        # ('.\\tupleresult\\fresult\\lipeixu\\N=65-10pn=5-10pr=008-01ms=2-11u=1-3.pickle')
    #         # (8,'D:\parallelclass\\result\\acc8.pickle'),
    #         ])
    # drawpn( [
    #          ('.\\tupleresult\\yresult\\M=2-11pn=8-10pr=008-01n=70-100.pickle')
    #         ])





