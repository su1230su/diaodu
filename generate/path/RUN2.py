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


    # path(data=["10","8","10","100","1000","15","30","15","20","0.1","10","5"],[1,1],3,1,begin,end,pace)
    ret = Experiment_rt_Sun_path.run_all(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],options,which_parameter,task_save,begin,end,pace)
    # draw_Sun_path.draw_2_plots(ret,options,names,which_parameter)
    draw_Sun_path.draw_2_plots(begin,end,ret, options, names, which_parameter)

if __name__ == '__main__':
    begin = 15
    end = 31
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
    # ret=Experiment_rt_Sun_path.run_all(tasknum,Umin,Umax,Tmin,Tmax,Ndagmin,Ndagmax,Msmin,Msmax,Pr,numP,TURN)
    # draw_Sun_path.draw_2_plots(ret)
    # #print(random.sample(list(range(0, 10)), 10))
    #        tasknum,Umin,Umax,Tmin,Tmax, Ndagmin,Ndagmax,Msmin,Msmax, Pr,  numP,   TURN,   ×   options,task_save,begin, end, pace
    # nump的实验

    #data = ["11", "4", "8", "100", "1000", "25", "30", "15", "22", "0.9", "15", "100"]
    # 其他组实验
    # U的实验
    # data = ["11", "6", "6", "100", "100", "25", "30", "15", "15", "0.9", "15", "100"]


    # pr的实验
    # data = ["11", "6", "8", "100", "100", "25", "30", "10", "15", "0.9", "15", "1000"]



    # tasknum实验
    # data = ["11", "6", "6", "100", "100", "5", "20", "30", "30", "0.9", "5", "10"]

    # 关于U
    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "1000"]

    # 关于G-EDF的ndag的实验
    # data = ["11", "4",  "8", "100", "100", "25", "25", "10", "15", "0.9", "15", "400"]

    # data = ["11", "4", "8", "100", "100", "25", "30", "15", "22", "0.9", "15", "10"]


    data = ["11", "4", "8", "100", "100", "25", "25", "15", "22", "0.9", "15", "100"]

    path(data,[1,1],5,1,begin,end,pace)
