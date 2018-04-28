from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec
import sys

the_grid = GridSpec(1, 2)

def task1(name, variable):
    dataset = pd.read_csv(name)
    plt.figure(figsize=(8,6))
    
    markers = ['o', '+', '*', 'x', 'd', '2', '3', '4']
    colors = ['#DC143C', '#EE82EE', '#4B0082', '#4169E1', '#B0E0E6', '#3CB371', '#F0E68C', '#8B4513']
    length = len(dataset.columns)
    for i in range(1, length):
        plt.plot(dataset[dataset.columns[0]], dataset[dataset.columns[i]], color=colors[i],label=dataset.columns[i], marker = markers[0])
    #plt.plot(dataset.Pruning_ratio, dataset.Conv2, color='#EE82EE',label='Equally', marker = '+')
    #plt.plot(dataset.Pruning_ratio, dataset.Conv3, color='#4B0082',label='Balancing Transfer Time', marker = '*')
    #plt.plot(dataset.Pruning_ratio, dataset.Conv4, color='#4169E1',label='Balancing Processing Time', marker = 'x')
    #plt.plot(dataset.Pruning_ratio, dataset.Conv5, color='#B0E0E6',label='Optimum', marker = 'd')
    # plt.plot(dataset.Pruning_ratio, dataset.FC6, color='#3CB371',label='FC6', marker = '2')
    # plt.plot(dataset.Pruning_ratio, dataset.FC7, color='#F0E68C',label='FC7', marker = '3')
    # plt.plot(dataset.Pruning_ratio, dataset.FC8, color='#8B4513',label='FC8', marker = '4')
    
    plt.title('')
    plt.xlabel(variable)
    plt.ylabel('Job completion time (s)')
    plt.legend(loc='best')
 
print(sys.argv)
task1(sys.argv[1], sys.argv[2])
plt.show()
