#coding=utf-8
from __future__ import division

import random

import Experiment_rt_Sun_path
import draw_Sun_path


def path(data,options,which_parameter,task_save,begin,end,pace):
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = int(data[3])
    data[4] = int(data[4])
    data[5] = int(data[5])
    data[6] = int(data[6])
    data[7] = int(data[7])
    data[8] = int(data[8])
    data[9] = float(data[9])
    data[10] = int(data[10])
    data[11] = int(data[11])

    # names=["imp","bl_fake"]

    names = ["Basic-FP", "Imp-FP"]

    # names = ["G-EDF", "YANG"]

                                        # path(data=["10","8","10","100","1000","15","30","15","20","0.1","10","5"],[1,1],3,1,begin,end,pace)
    ret = Experiment_rt_Sun_path.run_all(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],options,which_parameter,task_save,begin,end,pace)
    # draw_Sun_path.draw_2_plots(ret,options,names,which_parameter)
    draw_Sun_path.draw_2_plots(begin,end,ret, options, names, which_parameter)

if __name__ == '__main__':
    begin =10
    end = 30
    pace = 2
    # # tasknum=10
    # Umin=8   #4.5        #5 #9
    # Umax=10   #7           #8 #12
    # Tmin=100= 2`
    # Tmax=1000
    # Ndagmin=15
    # Ndagmax=30
    # Msmin=15
    # Msmax=20
    # Pr=0.1
    # numP=10
    # TURN=5
    #
    # ret=Experiment_rt_Sun_path.run_all(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
    # draw_Sun_path.draw_2_plots(ret)
    # #print(random.sample(list(range(0, 10)), 10))
    #        tasknum,Umin,Umax,Tmin,Tmax, Ndagmin,Ndagmax,Msmin,Msmax, Pr,  numP,   TURN,      options,task_save,begin, end, pace
    # nump的实验
    #data = ["13", "6", "6", "100", "100", "25", "30", "15", "15", "0.9", "4", "10"]
    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]



    # 其他组实验
    # U的实验
    # data = ["12", "6", "6", "100", "1000", "15", "30", "15", "15", "0.9", "15", "1000"]
    # data = ["13", "6", "6", "100", "100", "25", "25", "15", "15", "0.9", "15", "10"]
    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]
    #data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]

    # Ndag的实验
    # data = ["13", "6", "6", "100", "100", "25", "25", "15", "15", "0.9", "15", "700"]
    # pr的实验
    # data = ["13", "7", "7", "100", "100", "15", "20", "10", "10", "0.9", "10", "100"]

    # Ms的实验
    # data = ["11", "4", "10", "100", "100", "20", "25", "15", "15", "0.9", "15", "100"]

    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]


    # tasknum实验
    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "5", "1000"]


    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]
    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "500"]
    data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "5"]
    path(data,[1,1],2,1,begin,end,pace)
