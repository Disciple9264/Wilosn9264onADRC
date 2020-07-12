#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:11:13 2020
Basic Math in ADRC
@author: Wilson
"""
import numpy as np


#获得安排过度的输入
def get_trns(T0,t_max=10,samplepoint=1000):
    t_cell=t_max/samplepoint
    t=t_cell*np.arange(samplepoint)
    trns=np.zeros(samplepoint)
    for i in range(samplepoint):
        if t[i]<=T0:
            trns[i]=0.5*(1+np.sin(np.pi*(t[i]/T0-0.5)))
        else: trns[i]=1
    return trns

#获得安排过度的输入的微分
def get_dtrns(T0,t_max=10,samplepoint=1000):
    t_cell=t_max/samplepoint
    t=t_cell*np.arange(samplepoint)
    trns=np.zeros(samplepoint)
    for i in range(samplepoint):
        if t[i]<=T0:
            trns[i]=0.5*np.pi/T0*np.cos(np.pi*(t[i]/T0-0.5))
        else: trns[i]=1
    return trns
