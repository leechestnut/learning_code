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
from IC import *
def Greedyforseed(G,k):
    G = notono(G)
    singleinftotal(G)
    seedset=[]
    sum=0
    nodes=G.nodes

    nodes=list(nodes)
    seedset.append(nodes[2])
    for node in G.nodes:
        if(G.nodes[node]['inf']>G.nodes[seedset[0]]['inf']):
            seedset.pop()
            seedset.append(node)

    nodes=[node for node in nodes if node!=seedset[0]]

    sum=G.nodes[seedset[0]]['inf']
    k-=1
    nodex=0#用来保存每一次选择的种子节点
    while k>0:
        for node in nodes:#此循环用来找每次加进来增益最大的node
            seedset.append(node)
            t=seedset_toatal_inf(G,seedset)
            if t>sum:
                nodex=node
                sum=t
            seedset.pop()
        nodes=[no for no in nodes if no!=nodex]
        seedset.append(nodex)
        k-=1
    return seedset,sum
