#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-10-07 20:57:11
LastEditor: John
LastEditTime: 2021-03-31 18:47:28
Discription: 
Environment: 
'''
import matplotlib.pyplot as plt
import seaborn as sns
def plot_rewards(rewards,ma_rewards,tag="train",algo = "DQN",save=True,path='./'):
    sns.set()
    plt.title("average learning curve of {}".format(algo))
    plt.xlabel('epsiodes')
    plt.plot(rewards,label='rewards')
    plt.plot(ma_rewards,label='moving average rewards')
    plt.legend()
    if save:
        plt.savefig(path+"rewards_curve_{}".format(tag))
    plt.show()

def plot_losses(losses,algo = "DQN",save=True,path='./'):
    sns.set()
    plt.title("loss curve of {}".format(algo))
    plt.xlabel('epsiodes')
    plt.plot(losses,label='rewards')
    plt.legend()
    if save:
        plt.savefig(path+"losses_curve")
    plt.show()
   
