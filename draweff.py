
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import readpickle

# plt.figure(figsize=(6, 6))



def drawu( filename):


    results = readpickle.cal_eff(filename)
    # m=results[len(results)-1]

    X = [tmp  for tmp in results[0]]
    Z1 = [tmp*1000  for tmp in results[1]]
    Z2 = [tmp*1000  for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    Z4 = [tmp*1000 for tmp in results[4]]
    print(X)
    print(Z1)
    print(Z2)
    # print (Z3)
    print(Z4)

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.semilogy(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.semilogy(X, Z2, 'g', linestyle='solid', marker='s', lw=1, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='Eff-Approx')
    plt.semilogy(X, Z4, 'y', linestyle='solid', marker='.', lw=1, label='NEW-B-2')

    plt.xlabel('$U$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    # plt.xlabel('The number of vertexes', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Average execution time(s)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="lower right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    plt.ylim(0, 100000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawpr( filename):


    results = readpickle.cal_eff(filename)
    # m=results[len(results)-1]

    X = [tmp   for tmp in results[0]]
    Z1 = [tmp*1000   for tmp in results[1]]
    Z2 = [tmp*1000   for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    Z4 = [tmp*1000 for tmp in results[4]]
    print(X)
    print(Z1)
    print(Z2)
    # print (Z3)
    print(Z4)



    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.semilogy(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.semilogy(X, Z2, 'g', linestyle='solid', marker='s', lw=1, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='Eff-Approx')
    plt.semilogy(X, Z4, 'y', linestyle='solid', marker='o', lw=1, label='NEW-B-2')

    # plt.xlabel('$U$', fontsize=30)
    plt.xlabel('$pr$', fontsize=30)
    # plt.xlabel('The number of vertexes', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Average execution time(ms)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="lower left", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.ylim(0, 400)
    plt.ylim(0, 100000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawN( filename):


    results = readpickle.cal_eff(filename)
    # m=results[len(results)-1]

    X = [tmp  for tmp in results[0]]
    Z1 = [tmp*1000  for tmp in results[1]]
    Z2 = [tmp*1000   for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    Z4 = [tmp*1000  for tmp in results[4]]
    print(X)
    print(Z1)
    print(Z2)
    # print (Z3)
    print(Z4)
    X = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
    Z1 = [3.408646583557129, 4.612445831298828, 4.110383987426758, 5.314183235168457, 5.113983154296875,
          7.5202226638793945,
          7.720661163330078, 7.419371604919434, 8.522915840148926, 10.227394104003906]
    Z2 = [3.309011459350586, 4.812741279602051, 4.412627220153809, 4.812741279602051, 5.113410949707031,
          7.118988037109375,
          7.520151138305664, 7.921242713928223, 9.224224090576172, 10.828995704650879]
    Z4 = [840.5350208282471, 1640.692400932312, 4078.953576087952, 5612.789642333984, 5636.3884925842285,
          7849.50966835022,
          11824.70018863678, 21759.5867395401, 25760.847449302673, 59432.972264289856]
    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.semilogy(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.semilogy(X, Z2, 'g', linestyle='solid', marker='s', lw=1, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='Eff-Approx')
    plt.semilogy(X, Z4, 'y', linestyle='solid', marker='o', lw=1, label='NEW-B-2')

    # plt.xlabel('$U$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    plt.xlabel('$|V|$', fontsize=30)
    # plt.xlabel('The range of pn', fontsize=30)
    plt.ylabel('Average execution time(ms)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="center right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.ylim(0, 400)
    plt.ylim(0, 100000)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])
# 关于任务集合大小S的图表
def drawpn( filename):


    results = readpickle.cal_eff(filename)
    # m=results[len(results)-1]

    X = [tmp  for tmp in results[0]]
    Z1 = [tmp*1000  for tmp in results[1]]
    Z2 = [tmp*1000  for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    Z4 = [tmp*1000 for tmp in results[4]]
    print(X)
    print(Z1)
    print(Z2)
    # print (Z3)
    print(Z4)

    X=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Z1=[6.316924095153809, 4.913449287414551, 5.715084075927734, 4.812788963317871, 5.715346336364746, 6.1138153076171875,
     4.409027099609375, 4.911446571350098, 4.211068153381348, 4.514837265014648, 4.612064361572266]
    Z2=[6.31716251373291, 5.213451385498047, 6.116199493408203, 4.812717437744141, 6.216263771057129, 6.82072639465332,
     4.818558692932129, 4.80952262878418, 4.718422889709473, 4.9102783203125, 5.715155601501465]
    Z4=[2095.057487487793, 3410.5687856674194, 3415.9175634384155, 3762.446069717407, 3873.5825061798096,
     5650.731515884399, 5926.939630508423, 9274.238777160645, 16680.274081230164, 34945.650577545166,
     37895.681643486023]

    # X1=[4.810287952423096, 4.480252265930176, 4.440274238586426, 4.41023588180542, 4.810280799865723, 4.460270404815674,
    #  3.9202070236206055, 3.9702248573303227, 3.920204639434814, 3.9101862907409664, 3.8302206993103027,
    #  3.890235424041748, 3.850235939025879]
    # Z2= [4.960272312164307, 4.480266571044922, 4.47023868560791, 4.560282230377197, 4.820306301116943, 4.660248756408691,
    #  4.070217609405518, 4.06022310256958, 4.1302490234375, 4.030253887176514, 4.20027494430542, 4.130222797393799,
    #  4.020218849182129]
    # Z4=[1200, 1231.7804718017578, 1510.206367969513, 1935.9007263183594, 2584.297831058502, 3337.510931491852,
    #  4909.440801143646, 6037.395334243774, 10949.34624671936, 14420.244781970978, 27109.89057302475, 53521.0112452507,
    #  56772.307176589966]
    # y=[]
    # for i in range(7):
    #     if i==0:
    #         y.append(0)
    #     else:
    #         y.append(10**i)
    # print (y)


    fig=plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
    # ax = fig.add_subplot(1, 1, 1, frameon=False)
    # ax.set_ylim(0,100000)
    # ax.set_yticks([0, 10, 100, 1000, 10000, 100000])
    # ax.set_yticklabels([0,"","","","","",100000],fontsize=30)
    # ax.set_yticklabels(["10 100 1000 10000"], minor=True)
    # for line in ax.yaxis.get_majorticklines():
    #     line.
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.semilogy(X, Z1, 'r', linestyle='solid', marker='*', lw=2, label='OLD-B')
    plt.semilogy(X, Z2, 'g', linestyle='solid', marker='s', lw=1, label='NEW-B-1')
    # plt.plot(X, Z3, 'b', linestyle='solid', marker='+', lw=2, label='Eff-Approx')
    plt.semilogy(X, Z4, 'y', linestyle='solid', marker='o', lw=1, label='NEW-B-2')

    # plt.xlabel('$U$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=30)
    # plt.xlabel('The number of vertexes', fontsize=30)
    plt.xlabel('$|S|$', fontsize=30)
    plt.ylabel('Average execution time(ms)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="center right", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)


    plt.ylim(0,100000)
    # plt.semilogy
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

if __name__ == '__main__':
    # drawu('.\\tupleresult\\fresult\\M=2-11pn=5-10pr=008-04n=70-100.pickle')
    # drawpr('.\\tupleresult\\fresult\\range\\rpr=005-1n=100-105pn=8-10ms=2-11u=1-3t.pickle')
    # drawN('.\\tupleresult\\fresult\\effN=65-10pn=5-10pr=008-01ms=2-11u=1-3.pickle')
    drawpn('.\\tupleresult\\fresult\\effpn=2-12n=70-100pr=0.08-0.1ms=2-11u=1-3.pickle')





