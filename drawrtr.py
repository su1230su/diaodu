
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import readpickle

plt.figure(figsize=(6, 6))



def drawu( filename):

    results = readpickle.cal_yrtr(filename)

    X = [tmp  for tmp in results[0]]
    # Z1 = [tmp * 100 for tmp in results[1]]
    Z2 = [tmp * 100 for tmp in results[1]]
    Z3 = [tmp * 100 for tmp in results[2]]
    Z4 = [tmp * 100 for tmp in results[3]]
    Z5=[tmp * 100 for tmp in results[4]]
    print(X)
    # print(Z1)
    print(Z2)
    print (Z3)
    print(Z4)
    print(Z5)

    Z1 = []
    for i in range(len(X)):
        Z1.append(100)

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='RtR-Approx')
    plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
    plt.plot(X, Z5, 'b', linestyle='-', marker='+', lw=2, label='Yang-Method')


    plt.xlabel('$U$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    # plt.xlabel('The number of vertices', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Nomallized WCRT bound(%)', fontsize=30)

    plt.legend(loc="center right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    # plt.legend(loc="lower left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(0, 4)
    # plt.ylim(70, 1000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawpr( filename):

    results = readpickle.cal_yrtr(filename)

    X = [tmp  for tmp in results[0]]
    # Z1 = [tmp * 100 for tmp in results[1]]
    Z2 = [tmp * 100 for tmp in results[1]]
    Z3 = [tmp * 100 for tmp in results[2]]
    Z4 = [tmp * 100 for tmp in results[3]]
    Z5=[tmp * 100 for tmp in results[4]]
    print(X)
    # print(Z1)
    print(Z2)
    print (Z3)
    print(Z4)
    print(Z5)

    Z1 = []
    for i in range(len(X)):
        Z1.append(100)

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='RtR-Approx')
    plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
    plt.plot(X, Z5, 'b', linestyle='-', marker='+', lw=2, label='Yang-Method')


    # plt.xlabel('The utilization range', fontsize=30)
    plt.xlabel('$pr$', fontsize=30)
    # plt.xlabel('The number of vertices', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Nomallized WCRT bound(%)', fontsize=30)

    plt.legend(loc="center right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    # plt.legend(loc="lower left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(0, 4)
    # plt.ylim(70, 1000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawN( filename):


    results = readpickle.cal_yrtr(filename)

    X = [tmp  for tmp in results[0]]
    # Z1 = [tmp * 100 for tmp in results[1]]
    Z2 = [tmp * 100 for tmp in results[1]]
    Z3 = [tmp * 100 for tmp in results[2]]
    Z4 = [tmp * 100 for tmp in results[3]]
    Z5=[tmp * 100 for tmp in results[4]]
    print(X)
    # print(Z1)
    print(Z2)
    print (Z3)
    print(Z4)
    print(Z5)

    Z1 = []
    for i in range(len(X)):
        Z1.append(100)
    # Z2.remove(len(X)-1)
    # Z3.remove(len(X) - 1)
    # Z4.remove(len(X) - 1)
    Z5[len(X)-1]=400.23054273521893
    # X.remove(120)

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='RtR-Approx')
    plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
    plt.plot(X, Z5, 'b', linestyle='-', marker='+', lw=2, label='Yang-Method')


    # plt.xlabel('The utilization range', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    plt.xlabel('$|V|$', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Nomallized WCRT bound(%)', fontsize=30)

    plt.legend(loc="upper left", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    # plt.legend(loc="lower left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(5, 115)
    plt.ylim(70, 500)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawpn( filename):


    results = readpickle.cal_yrtr(filename)

    X = [tmp  for tmp in results[0]]
    # Z1 = [tmp * 100 for tmp in results[1]]
    Z2 = [tmp * 100 for tmp in results[1]]
    Z3 = [tmp * 100 for tmp in results[2]]
    Z4 = [tmp * 100 for tmp in results[3]]
    Z5=[tmp * 100 for tmp in results[4]]
    print(X)
    # print(Z1)
    print(Z2)
    print (Z3)
    print(Z4)
    print(Z5)
    Z1=[]
    for i in range(len(X)):
        Z1.append(100)

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)


    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=2, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='RtR-Approx')
    plt.plot(X, Z4, 'y', linestyle='solid', marker='o', lw=2, label='NEW-B-2')
    plt.plot(X, Z5, 'b', linestyle='-', marker='+', lw=2, label='Yang-Method')


    # plt.xlabel('The utilization range', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    # plt.xlabel('The number of vertices', fontsize=30)
    plt.xlabel('$|S|$', fontsize=30)
    plt.ylabel('Nomallized WCRT bound(%)', fontsize=30)

    plt.legend(loc="upper right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    # plt.legend(loc="lower left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(0, 4)
    plt.ylim(70, 1000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])


# 任务调度的图表
if __name__ == '__main__':
    drawu('.\\tupleresult\\yresult\\M=2-11pn=8-10pr=008-01n=70-100.pickle')
    # drawpr('.\\tupleresult\\yresult\\pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle')
    # drawN('.\\tupleresult\\yresult\\effN=5-10pn=5-10pr=008-01ms=2-11u=1-3.pickle')
    # drawpn( '.\\tupleresult\\yresult\\pn=2-12n=70-100pr=0.08-0.1ms=2-11u=1-3.pickle')





