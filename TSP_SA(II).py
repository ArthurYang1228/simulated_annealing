# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:42:00 2017

@author: sunlite
"""


import random
import math
import pandas as pd
from matplotlib import pyplot as pl
import sys

li = []
train = pd.read_csv("a280.csv")
for i in train['n'].str.split(" "):
    li.append( [n for n in i if n != ''])    

X = [x[1] for x in li ]
Y = [y[2] for y in li ]






def distance(list):
    num = len(list)
    arr = [[ col for col in range(num)] for row in range(num)]
    valstr = ""
    for row in range(num):
        for col in range(num):
            if col == row:
                arr[row][col] = 0
            else:
                p1 = list[row]
                p2 = list[col]
                arr[row][col] = round(math.sqrt(math.pow((int(p1[1]) - int(p2[1])),2) + math.pow((int(p1[2]) - int(p2[2])),2)),2) ### 求歐式距離，保留2位小數
    return arr



def costfunction(list):
    dis_matrix = distance(list)
    totaldis = 0
    for i in range(len(list)-2):
        ori = int(list[i][0]) - 1
        des = int(list[i+1][0]) -1
        totaldis += dis_matrix[ori][des]
    return  totaldis + dis_matrix[int(list[0][0])-1][int(list[-1][0])-1]




def annealingoptimize( curnode ,next_list ,cost, T=10000.0, cool=0.97):
    
    nextnode = next_list[0]
    while T>0.1:
        
        i=random.randint(0, len(next_list)-1)
        if nextnode[0] == next_list[i][0]:
            continue
        else:
            trynode = next_list[i]
        ea=cost[int(curnode[0])-1][int(nextnode[0])-1]
        eb=cost[int(curnode[0])-1][int(trynode[0])-1]
        #p=pow(math.e,-(eb-ea)/T)

        #Is it better, or does it make the probability cutoff?
        if(eb<ea or random.random()<pow(math.e, -(eb-ea)/T)):
            nextnode = trynode

        #Decrease the temperature
        T=T*cool

    return nextnode
count = 1

while len(li)>0:
    
    if len(li) ==1:
        way.append(li[0])
        break
    
    
    print(count)
    nextnode = annealingoptimize(way[-1],li,cost)
    way.append(nextnode)
    
    
    
    li.remove(nextnode)
    print('end')
    count +=1
    
print(costfunction(way))
print(way)
pl.plot([x[1] for x in way],[y[2] for y in way])
