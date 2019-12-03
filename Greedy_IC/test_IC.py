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
from Greedy import *
from IC import *

if __name__=='__main__':
    start=time.clock()
    '''
    #用来删除文件中不符合要求的结点，这里删除了结点id>200的
    with open('Wiki-Vote.txt', 'r') as r:
        lines = r.readlines()

    with open('Wiki-Vote.txt', 'w') as w:
        for l in lines:
            print(l.split('\t'))

            [a,b]=l.split('\t')
            a=int(a)
            b=int(b)
            if a<200 and b<200:
                w.write(l)
    print(len(lines))
    '''
    f=open('Wiki-Vote.txt','r')
    '''
    read()  ： 一次性读取整个文件内容。推荐使用read(size)方法，size越大运行时间越长
    readline()  ：每次读取一行内容。内存不够时使用，一般不太用
    readlines()   ：一次性读取整个文件内容，并按行返回到list，方便我们遍历
    一般小文件我们都采用read()，不确定大小你就定个size，大文件就用readlines()
    '''
    dataset=[]
    rows=list(f.readlines())
    for row in rows:
        [a,b]=row.split('\t')
        dataset.append((int(a),int(b)))
    '''上面是将TXT中的结点对信息每对都存到set中再存到list中'''
    G=networkx.DiGraph() #建立一个空的有向图
    G.add_edges_from(dataset)#len(G)输出端是G中有多少个结点
    '''
    for edge in G.edges:
        a,b=edge
        if (a,b) in G.edges and (b,a) in G.edges:
            G.remove_edge(b,a)
    '''
        #print(row)
    f.close()


    '''for w in G[3]:
        print(w)
    '''

    '''for ed in G.edges:
        print(str(ed)+'  '+str(G.edges[ed]['p0']))
    '''
    print(G.edges)
    seedset,sum=Greedyforseed(G,4)
    print(seedset)
    print(sum)
    end=time.clock()

