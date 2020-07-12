# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:09:24 2020

@author: Wilson
"""

import numpy as np
import control as ctl
import matplotlib.pyplot as plt
import WilsonMath_ADRC as wmadrc

sel=146;

if sel==141:
#------------------------------------
#图1.4.1：证明安排过度只和r有关，而r和a1、a2均有函数关系
    a1=np.zeros(4)
    k0=1#积分
    k1=2#比例
    k2=2#微分
    r=np.array([2,4,6,8])
    for i in range(4):
        a1[i]=np.square(r[i])#零次恢复力
    a2=r*2#一次阻尼
    a_1=a1+np.ones(4)*k1#零次
    a_2=a2+np.ones(4)*k2#一次
    
    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,sharex='col',sharey='row') # 开启subplots模式
    
    sys=ctl.tf([a_1[0],],[1,a_2[0],a_1[0]])
    t_step,y_step=ctl.step_response(sys)
    ax1.plot(t_step,y_step,'r',label='s1 Step Response',linewidth=0.5)
    ax1.set_title('s1 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[1],],[1,a_2[1],a_1[1]])
    t_step,y_step=ctl.step_response(sys)
    ax2.plot(t_step,y_step,'g',label='s2 Step Response',linewidth=0.5)
    ax2.set_title('s2 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[2],],[1,a_2[2],a_1[2]])
    t_step,y_step=ctl.step_response(sys)
    ax3.plot(t_step,y_step,'b',label='s3 Step Response',linewidth=0.5)
    ax3.set_title('s3 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[3],],[1,a_2[3],a_1[3]])
    t_step,y_step=ctl.step_response(sys)
    ax4.plot(t_step,y_step,'m',label='s4 Step Response',linewidth=0.5)
    ax4.set_title('s4 Step Response',fontsize=9)
    plt.grid()
    
    plt.show()

elif sel==142:
#------------------------------------
#图1.4.2：控制对象参数的摄动对控制性能的影响
    k0=1#积分
    k1=5#比例
    k2=2#微分
    a1=[3,1,2,2]#零次恢复力
    a2=[3,2,3,1]#一次阻尼
    a_1=a1+np.ones(4)*k1#零次
    a_2=a2+np.ones(4)*k2#一次
    
    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,sharex='col',sharey='row') # 开启subplots模式
    
    sys=ctl.tf([a_1[0],],[1,a_2[0],a_1[0]])
    t_step,y_step=ctl.step_response(sys)
    ax1.plot(t_step,y_step,'r',label='s1 Step Response',linewidth=0.5)
    ax1.set_title('s1 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[1],],[1,a_2[1],a_1[1]])
    t_step,y_step=ctl.step_response(sys)
    ax2.plot(t_step,y_step,'g',label='s2 Step Response',linewidth=0.5)
    ax2.set_title('s2 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[2],],[1,a_2[2],a_1[2]])
    t_step,y_step=ctl.step_response(sys)
    ax3.plot(t_step,y_step,'b',label='s3 Step Response',linewidth=0.5)
    ax3.set_title('s3 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[3],],[1,a_2[3],a_1[3]])
    t_step,y_step=ctl.step_response(sys)
    ax4.plot(t_step,y_step,'m',label='s4 Step Response',linewidth=0.5)
    ax4.set_title('s4 Step Response',fontsize=9)
    plt.grid()
    
    plt.show()

elif sel==143:
#------------------------------------
#针对公式1.4.7绘制安排过度函数,
    T0=5
    t=0.01*np.arange(1000, dtype = float)
    trns=np.zeros(len(t))
    for i in range(len(t)):
        if t[i]<=T0:
            trns[i]=0.5*(1+np.sin(np.pi*(t[i]/T0-0.5)))
        else: trns[i]=1
    plt.plot(t,trns)
    plt.title('trns(t)')
    plt.xlabel('t')
    plt.ylabel('trns')
    
    plt.grid()
    plt.show()
    
elif sel==144:
#------------------------------------
#图1.4.4：快速和超调不对立
    t_step=0.01*np.arange(1000,dtype=float)
    T0=[2,1]
    k0=1#积分
    k1=[800,400]#比例
    k2=0#微分
    a1=2#零次恢复力
    a2=2#一次阻尼
    a_1=[a1+k1[0],a1+k1[1],a1+k1[0],a1+k1[1]]#零次
    a_2=a2+k2#一次
    
    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,sharex='col',sharey='row') # 开启subplots模式
    
    sys=ctl.tf([a_1[0],],[1,a_2,a_1[0]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0[0]))
    ax1.plot(t_step,y_step,'r',label='s1 Step Response',linewidth=0.5)
    ax1.set_title('s1 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[1],],[1,a_2,a_1[1]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0[0]))
    ax2.plot(t_step,y_step,'g',label='s2 Step Response',linewidth=0.5)
    ax2.set_title('s2 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[2],],[1,a_2,a_1[2]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0[1]))
    ax3.plot(t_step,y_step,'b',label='s3 Step Response',linewidth=0.5)
    ax3.set_title('s3 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[3],],[1,a_2,a_1[3]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0[1]))
    ax4.plot(t_step,y_step,'m',label='s4 Step Response',linewidth=0.5)
    ax4.set_title('s4 Step Response',fontsize=9)
    plt.grid()
    
    plt.show()
    
elif sel==145:
#------------------------------------
#图1.4.4：快速和超调不对立
    t_step=0.01*np.arange(1000,dtype=float)
    T0=2
    k0=1#积分
    k1=600#比例
    k2=0#微分
    a1=2#零次恢复力
    a2=[2,10,30,50]#一次阻尼
    a_1=a1+k1#零次
    a_2=a2+k2*np.ones(4)#一次
    
    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,sharex='col',sharey='row') # 开启subplots模式
    
    sys=ctl.tf([a_1,],[1,a_2[0],a_1])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0))
    ax1.plot(t_step,y_step,'r',label='s1 Step Response',linewidth=0.5)
    ax1.set_title('s1 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1,],[1,a_2[1],a_1])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0))
    ax2.plot(t_step,y_step,'g',label='s2 Step Response',linewidth=0.5)
    ax2.set_title('s2 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1,],[1,a_2[2],a_1])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0))
    ax3.plot(t_step,y_step,'b',label='s3 Step Response',linewidth=0.5)
    ax3.set_title('s3 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1,],[1,a_2[3],a_1])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,wmadrc.get_trns(T0))
    ax4.plot(t_step,y_step,'m',label='s4 Step Response',linewidth=0.5)
    ax4.set_title('s4 Step Response',fontsize=9)
    plt.grid()
    
    plt.show()

elif sel==146:
#------------------------------------
#图1.4.6：PD????有问题
    T0=0.5*np.ones(4)
    k0=np.ones(4)#积分
    k1=[10,10,1000,1000]#比例
    k2=[12,120,120,12]#微分
    a1=2*np.ones(4)#零次恢复力
    a2=2*np.ones(4)#一次阻尼
    a_1=a1+k1#零次
    a_2=a2+k2#一次

    t_step=0.01*np.arange(1000,dtype=float)

    f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4,sharex='col',sharey='row') # 开启subplots模式
    
    sys=ctl.tf([a_1[0],],[1,a_2[0],a_1[0]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,a_1[0]*wmadrc.get_trns(T0[0])+a_2[0]*wmadrc.get_dtrns(T0[0]))
    ax1.plot(t_step,y_step,'r',label='s1 Step Response',linewidth=0.5)
    ax1.set_title('s1 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[1],],[1,a_2[1],a_1[1]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,a_1[1]*wmadrc.get_trns(T0[1])+a_2[1]*wmadrc.get_dtrns(T0[1]))
    ax2.plot(t_step,y_step,'g',label='s2 Step Response',linewidth=0.5)
    ax2.set_title('s2 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[2],],[1,a_2[2],a_1[2]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,a_1[2]*wmadrc.get_trns(T0[0])+a_2[2]*wmadrc.get_dtrns(T0[2]))
    ax3.plot(t_step,y_step,'b',label='s3 Step Response',linewidth=0.5)
    ax3.set_title('s3 Step Response',fontsize=9)
    plt.grid()
    
    sys=ctl.tf([a_1[3],],[1,a_2[3],a_1[3]])
    t_step,y_step,x_step=ctl.forced_response(sys,t_step,a_1[3]*wmadrc.get_trns(T0[0])+a_2[3]*wmadrc.get_dtrns(T0[3]))
    ax4.plot(t_step,y_step,'m',label='s4 Step Response',linewidth=0.5)
    ax4.set_title('s4 Step Response',fontsize=9)
    plt.grid()
    
    plt.show()
else:
    print('Error Input')