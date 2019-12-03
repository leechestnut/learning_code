#!/user/bin/env python
'''
上面这行话在unix系统才起作用，
目的是告诉操作系统使用哪个Python解释器来执行这个py文件。
为了防止操作系统用户没有将python装在默认的/usr/bin路径里。
'''
# coding=UTF-8
from networkx import *
from nose.tools import *
import time
import os
import re


# 函数到这里把结点v对w的影响力设为p0=1/w关注的人数，并把p0放在（v,w）上,并初始化每个结点的影响力为0
def notono(G):
   # G1 = G
    Greverse=networkx.DiGraph()
    for edg in G.edges:
        a,b=edg
        Greverse.add_edge(b,a)
        G.nodes[a]['inf']=0
        G.nodes[b]['inf']=0
    for edg in G.edges:
        a, b = edg
        G.edges[edg]['p0']=1/len(Greverse[b])
    return G

# 以下两个函数组合计算每个单个结点的影响力
def singleinftotal(G):
    for nd in G.nodes:
        G.nodes[nd]['inf']=singleinf(G,nd)

def singleinf(G,nd):
    if len(G[nd]) == 0:
        return 0
    if G.nodes[nd]['inf']>0:
        return G.nodes[nd]['inf']
    for w in G[nd]:
        #print('Gnode' + str(nd) + '的inf此时加上' + str(w) + "d inf")
        G.nodes[nd]['inf'] += G[nd][w]['p0'] * (1 + singleinf(G,w))

    return G.nodes[nd]['inf']

#计算结点集合的影响力
def seedset_toatal_inf(G,seedset):
    sum=0
    fans=set()
    Greverse=networkx.DiGraph()
    for seed in seedset:
        for w in G[seed]:
            fans.add(w)
            Greverse.add_edge(w,seed)

    for fan in fans:
        if len(Greverse[fan])==1:

            for r in Greverse[fan]:
                sum+=G[r][fan]['p0']*(1+G.nodes[fan]['inf'])
        else:
            p1=1
            for seed in Greverse[fan]:
                p1=p1*(1-G[seed][fan]['p0'])
            p1=1-p1
            sum+=p1*(1+G.nodes[fan]['inf'])
    return sum