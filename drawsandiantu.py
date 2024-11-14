
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import pickle

plt.figure(figsize=(6, 6))



def draw( filename):
    ofile = open(filename, 'rb')
    results= pickle.load(ofile, encoding='bytes')
    # m=results[len(results)-1]


    X = [tmp  for tmp in results[0]]
    Tsetnum=results[3]
    ttp=results[1]
    tte=results[2]
    Z1=[]
    Z2=[]
    for i in range(len(X)):
        Z2.append(ttp[i]/Tsetnum[i])
        Z1.append(tte[i] / Tsetnum[i])

    # Z
    # Z1 = [tmp * 100 for tmp in results[1]]
    # Z2 = [tmp * 100 for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    # Z4 = [tmp * 100 for tmp in results[4]]
    # print(X)
    # print(Z1)
    # print(Z2)
    # print (Z3)
    # print(Z4)
    # X=[1, 1.3666666666666667, 1.7333333333333334, 2.1, 2.466666666666667, 2.8333333333333335, 3.2, 3.566666666666667, 3.9333333333333336,
    #    4.3, 4.666666666666666, 5.033333333333332, 5.399999999999999]
    #
    # Z2=[39.933283591270445, 41.017245984077455, 40.52001819610596, 40.7225301027298, 40.79733304977417, 39.92188391685486, 40.06219091415405,
    #     40.477514719963075, 40.09329302310944, 41.06734952926636, 40.49761712551117, 39.88758101463318, 40.4428130865097]
    #
    # Z1=[107.00141990184784, 102.76517717838287, 103.44601731300354, 99.94231650829315, 103.34941074848174,
    #  105.20651752948763, 104.15215616226196, 100.6652582168579, 104.53167934417723, 103.76193437576293,
    #  105.51243443489075, 101.9034292936325, 103.40791463851929]


    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)
    plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=4, label='Eff-Exact')
    plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=4, label='Eff-EffExa')


    plt.xlabel('The utilization range', fontsize=40)
    # plt.xlabel('The range of pr', fontsize=40)
    # plt.xlabel('The number of vertexes', fontsize=40)
    # plt.xlabel('The range of pn', fontsize=40)
    plt.ylabel('Average execution time(s)', fontsize=40)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="upper left", title='', fontsize=30,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.ylim(0, 120)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

def drawscatterpr( filename):
    ofile = open(filename, 'rb')
    results= pickle.load(ofile, encoding='bytes')
    # m=results[len(results)-1]


    X = [tmp  for tmp in results[0]]

    ttp=results[1]
    tte=results[2]

    pr1=results[5]
    pr2=results[6]

    tt3 = results[7]
    pr3=results[9]

    fig = plt.figure(figsize=(11, 8))
    # plt.subplots_adjust(left=0.15, right=0.9, wspace=0.22, hspace=0.22, bottom=0.16, top=0.88)
    for i in range(len(ttp[1])):
        # print ("i=",i)
        Z1 = []
        Z2 = []
        Z3=[]
        X1=[]
        X2=[]
        X3=[]
        # C1=[]
        # C2=[]
        for j in range(len(X)):
            # print("j=",j)
            Z1.append(ttp[j][i])
            Z2.append(tte[j][i])
            Z3.append(tt3[j][i])
            X1.append(pr1[j][i])
            X2.append(pr2[j][i])
            X3.append(pr3[j][i])
            # C1.append('red')
            # C2.append('green')

        # plt.scatter(X1, Z1,marker='*',color='red')
        plt.semilogy(X3, Z3, linewidth=0,marker='o', color='steelblue')
        plt.semilogy(X2, Z2, linewidth=0,marker='x', color='red')

        # plt.scatter(X3, Z3,s=30, marker='o', color='steelblue')
        # plt.scatter(X2, Z2, s=50, marker='s', color='red')

        # print (X2)
        # print(X3)




    # for i in range(len(X)):
    #     Z2.append(ttp[i]/Tsetnum[i])
    #     Z1.append(tte[i] / Tsetnum[i])

    # Z
    # Z1 = [tmp * 100 for tmp in results[1]]
    # Z2 = [tmp * 100 for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    # Z4 = [tmp * 100 for tmp in results[4]]
    # print(X)
    # print(Z1)
    # print(Z2)
    # print (Z3)
    # print(Z4)
    # X=[1, 1.3666666666666667, 1.7333333333333334, 2.1, 2.466666666666667, 2.8333333333333335, 3.2, 3.566666666666667, 3.9333333333333336,
    #    4.3, 4.666666666666666, 5.033333333333332, 5.399999999999999]
    #
    # Z2=[39.933283591270445, 41.017245984077455, 40.52001819610596, 40.7225301027298, 40.79733304977417, 39.92188391685486, 40.06219091415405,
    #     40.477514719963075, 40.09329302310944, 41.06734952926636, 40.49761712551117, 39.88758101463318, 40.4428130865097]
    #
    # Z1=[107.00141990184784, 102.76517717838287, 103.44601731300354, 99.94231650829315, 103.34941074848174,
    #  105.20651752948763, 104.15215616226196, 100.6652582168579, 104.53167934417723, 103.76193437576293,
    #  105.51243443489075, 101.9034292936325, 103.40791463851929]


    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    # plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=4, label='Eff-Exact')
    # plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=4, label='Eff-EffExa')
    # fakebase = plt.plot([0], [0], linestyle="none", c='red', marker='*', label='Num-Ori')
    fakeimp = plt.plot([0], [0], linestyle="none", c='red', marker='x', label='New-B-2')
    fakepath = plt.plot([0], [0], linestyle="none", c='steelblue', marker='o', label='Enu-path')
    # plt.legend([fakeimp,fakepath], [ 'New-B-2','Enu-path'],
    #           numpoints=1, fontsize=27, markerscale=2,
    #           loc='upper right', bbox_to_anchor=(0.5, 1))


    plt.xlabel('$pr$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=40)
    # plt.xlabel('The number of vertexes', fontsize=40)
    # plt.xlabel('The range of pn', fontsize=40)
    plt.ylabel('number of paths (tuples)', fontsize=30)

    plt.legend(loc="upper left", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    # plt.legend(loc="upper left", title='', fontsize=27,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    plt.xlim(0, 1)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])


def drawscatterpn( filename):
    ofile = open(filename, 'rb')
    results= pickle.load(ofile, encoding='bytes')
    # m=results[len(results)-1]


    X = [tmp  for tmp in results[0]]

    ttp=results[1]
    tte=results[2]

    pr1=results[5]
    pr2=results[6]

    tt3 = results[7]
    pr3=results[9]

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.2, right=0.9, wspace=0.22, hspace=0.22, bottom=0.15, top=0.88)
    for i in range(len(ttp[1])):
        # print ("i=",i)
        Z1 = []
        Z2 = []
        Z3=[]
        # X1=[]
        # X2=[]
        # X3=[]
        # C1=[]
        # C2=[]
        for j in range(len(X)):
            # print("j=",j)
            Z1.append(ttp[j][i]/100)
            Z2.append(tte[j][i]/100)
            Z3.append(tt3[j][i]/100)
            # X1.append(pr1[j][i])
            # X2.append(pr2[j][i])
            # X3.append(pr3[j][i])
            # C1.append('red')
            # C2.append('green')

        # plt.scatter(X1, Z1,marker='*',color='red')
        plt.scatter(X, Z2, marker='*',color='yellow')
        plt.scatter(X, Z3, marker='o', color='blue')

        # print (X2)
        # print(X3)




    # for i in range(len(X)):
    #     Z2.append(ttp[i]/Tsetnum[i])
    #     Z1.append(tte[i] / Tsetnum[i])

    # Z
    # Z1 = [tmp * 100 for tmp in results[1]]
    # Z2 = [tmp * 100 for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    # Z4 = [tmp * 100 for tmp in results[4]]
    # print(X)
    # print(Z1)
    # print(Z2)
    # print (Z3)
    # print(Z4)
    # X=[1, 1.3666666666666667, 1.7333333333333334, 2.1, 2.466666666666667, 2.8333333333333335, 3.2, 3.566666666666667, 3.9333333333333336,
    #    4.3, 4.666666666666666, 5.033333333333332, 5.399999999999999]
    #
    # Z2=[39.933283591270445, 41.017245984077455, 40.52001819610596, 40.7225301027298, 40.79733304977417, 39.92188391685486, 40.06219091415405,
    #     40.477514719963075, 40.09329302310944, 41.06734952926636, 40.49761712551117, 39.88758101463318, 40.4428130865097]
    #
    # Z1=[107.00141990184784, 102.76517717838287, 103.44601731300354, 99.94231650829315, 103.34941074848174,
    #  105.20651752948763, 104.15215616226196, 100.6652582168579, 104.53167934417723, 103.76193437576293,
    #  105.51243443489075, 101.9034292936325, 103.40791463851929]


    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    # plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=4, label='Eff-Exact')
    # plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=4, label='Eff-EffExa')
    # fakebase = plt.plot([0], [0], linestyle="none", c='red', marker='*', label='Num-Ori')
    fakeimp = plt.plot([0], [0], linestyle="none", c='yellow', marker='*', label='New-B-2')
    fakepath = plt.plot([0], [0], linestyle="none", c='blue', marker='o', label='Enu-path')
    plt.legend([fakeimp,fakepath], [ 'New-B-2','Enu-path'],
              numpoints=1, fontsize=17, markerscale=2,
              loc=2, bbox_to_anchor=(0.05, 1))


    # plt.xlabel('$|pr|$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=40)
    # plt.xlabel('The number of vertexes', fontsize=40)
    plt.xlabel('$|S|$', fontsize=30)
    plt.ylabel('number of paths (tuples)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="upper left", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(0.2, 1)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])


def drawscatterN( filename):
    ofile = open(filename, 'rb')
    results= pickle.load(ofile, encoding='bytes')
    # m=results[len(results)-1]


    X = [tmp  for tmp in results[0]]

    ttp=results[1]
    tte=results[2]

    pr1=results[5]
    pr2=results[6]

    tt3 = results[7]
    pr3=results[9]

    plt.figure(figsize=(11, 8))
    plt.subplots_adjust(left=0.2, right=0.9, wspace=0.22, hspace=0.22, bottom=0.15, top=0.88)
    for i in range(len(ttp[1])):
        # print ("i=",i)
        Z1 = []
        Z2 = []
        Z3=[]
        # X1=[]
        # X2=[]
        # X3=[]
        # C1=[]
        # C2=[]
        for j in range(len(X)):
            # print("j=",j)
            Z1.append(ttp[j][i]/100)
            Z2.append(tte[j][i]/100)
            Z3.append(tt3[j][i]/100)
            # X1.append(pr1[j][i])
            # X2.append(pr2[j][i])
            # X3.append(pr3[j][i])
            # C1.append('red')
            # C2.append('green')

        # plt.scatter(X1, Z1,marker='*',color='red')
        plt.scatter(X, Z2,s=30, marker='s',color='red')
        plt.scatter(X, Z3, s=50,marker='o', color='steelblue')

        # print (X2)
        # print(X3)




    # for i in range(len(X)):
    #     Z2.append(ttp[i]/Tsetnum[i])
    #     Z1.append(tte[i] / Tsetnum[i])

    # Z
    # Z1 = [tmp * 100 for tmp in results[1]]
    # Z2 = [tmp * 100 for tmp in results[2]]
    # Z3 = [tmp * 100 for tmp in results[3]]
    # Z4 = [tmp * 100 for tmp in results[4]]
    # print(X)
    # print(Z1)
    # print(Z2)
    # print (Z3)
    # print(Z4)
    # X=[1, 1.3666666666666667, 1.7333333333333334, 2.1, 2.466666666666667, 2.8333333333333335, 3.2, 3.566666666666667, 3.9333333333333336,
    #    4.3, 4.666666666666666, 5.033333333333332, 5.399999999999999]
    #
    # Z2=[39.933283591270445, 41.017245984077455, 40.52001819610596, 40.7225301027298, 40.79733304977417, 39.92188391685486, 40.06219091415405,
    #     40.477514719963075, 40.09329302310944, 41.06734952926636, 40.49761712551117, 39.88758101463318, 40.4428130865097]
    #
    # Z1=[107.00141990184784, 102.76517717838287, 103.44601731300354, 99.94231650829315, 103.34941074848174,
    #  105.20651752948763, 104.15215616226196, 100.6652582168579, 104.53167934417723, 103.76193437576293,
    #  105.51243443489075, 101.9034292936325, 103.40791463851929]


    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    # plt.plot(X, Z1, 'r', linestyle='solid', marker='*', lw=4, label='Eff-Exact')
    # plt.plot(X, Z2, 'g', linestyle='solid', marker='s', lw=4, label='Eff-EffExa')
    # fakebase = plt.plot([0], [0], linestyle="none", c='red', marker='*', label='Num-Ori')
    fakeimp = plt.plot([0], [0], linestyle="none", c='red', marker='s', label='New-B-2')
    fakepath = plt.plot([0], [0], linestyle="none", c='steelblue', marker='o', label='Enu-path')
    plt.legend([fakeimp,fakepath], [ 'New-B-2','Enu-path'],
              numpoints=1, fontsize=17, markerscale=2,
              loc=2, bbox_to_anchor=(0.05, 1))


    # plt.xlabel('$|pr|$', fontsize=30)
    # plt.xlabel('The range of pr', fontsize=40)
    plt.xlabel('$|V|$', fontsize=30)
    # plt.xlabel('$|S|$', fontsize=40)
    plt.ylabel('number of paths (tuples)', fontsize=30)

    # plt.legend(loc="upper left", title='', fontsize=20,
    #            shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)

    plt.legend(loc="upper left", title='', fontsize=27,
               shadow=False, handlelength=3, fancybox=False, frameon=True, ncol=1, numpoints=1, borderaxespad=1)
    # plt.xlim(0.2, 1)
    plt.grid(True)
    plt.show()
        #        plt.yticks(range(0, 101, 5), ['%d' % d for d in range(0, 101, 5)])

if __name__ == '__main__':
    drawscatterpr( '.\\tupleresult\\fresult\\sandiantu\\efftuple60-65.pickle')
    # drawscatterpn( '.\\tupleresult\\fresult\\sandiantu\\efftuple70-75pn.pickle')
    # drawscatterN( '.\\tupleresult\\fresult\\sandiantu\\efftuple02-03N.pickle')




