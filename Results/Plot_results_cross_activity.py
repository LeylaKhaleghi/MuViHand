#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Result on MuViHand dataset for cross-activity test protocol

import numpy as np
import matplotlib.pyplot as plt

# UPDATA the main root
root = '/home/...'


color_list = ['steelblue', 'orange', 'green', 'mediumorchid', 'violet', 'brown', 'lightsteelblue', 'aquamarine', 'palegoldenrod']

plt.figure()

#Loading the data
All_threshold = np.load(root + 'All_threshold_cross_act.npy')
All_pck_curve = np.load(root + 'All_pck_curve_cross_act.npy')


plt.plot(All_threshold[0], All_pck_curve[0] ,  color=color_list[2], label='Boukhayma et al.' )
plt.plot(All_threshold[1], All_pck_curve[1] ,  color=color_list[5],  label='Hasson et al.')
plt.plot(All_threshold[2], All_pck_curve[2] , color=color_list[3],  label='Doosti et al.')
plt.plot(All_threshold[3], All_pck_curve[3] , color=color_list[0], label='Baseline 2')
plt.plot(All_threshold[4], All_pck_curve[4] , color=color_list[1],  label='Baseline 1')
plt.plot(All_threshold[5], All_pck_curve[5] , color=color_list[6], label='MuViHandNet')



plt.legend(loc='upper left',  facecolor="white")
plt.xlabel("Threshold in mm")
plt.title('cross-activity')
plt.ylabel("PCK")
plt.ylim(-0.05, 1.05)
plt.xlim(-0.05, 50.05)

plt.grid()

# plt.savefig('.../act'+ '.pdf')
plt.show()
plt.clf()