#!/user/bin/env python
'''
上面这行话在unix系统才起作用，
目的是告诉操作系统使用哪个Python解释器来执行这个py文件。
为了防止操作系统用户没有将python装在默认的/usr/bin路径里。
'''
# coding=UTF-8
from networkx import *
from pygraph.classes.digraph import digraph
from nose.tools import *
import time
import os
import re
if __name__=='__main__':
    #range(start包含，end不包含，step步长) 例如1,10,5输出1,6
    for i in range(5,101,5):
        print(i)
    dg=digraph()
    f