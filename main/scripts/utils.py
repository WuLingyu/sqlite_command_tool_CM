# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""

import configparser
import os
import sys

def fullFile(full_path, files):
    temp = []
    for f in files:
        temp.append(os.path.join(full_path, f))
    return temp

def clearCache():
    q_list = [] # common queue
    t_list = [] # list used to store target file 

    # current folder as root
    cur = os.path.split(sys.argv[0])[0]
    q_list.extend(fullFile(cur,os.listdir(cur)))

    # find all .pyc files
    while 1:
        if q_list == []:
            break;
        f = q_list.pop()
        if os.path.isdir(f) == True:
            q_list.extend(fullFile(f, os.listdir(f)))
        else:
            if f.endswith('.pyc'):
                t_list.append(f)
    # remove all these files
    for f in t_list:
        os.remove(f)

def checkout(files):
    # 
    print('checking start...')
    for f in files:
        sep = input('seperator of : %s (default:"|")' % (f))
        if sep == '': sep='|'
        rows = 0
        cols = {}
        with open(f, 'r') as fd:
            for line in fd:
                rows = rows + 1
                col_num = len(line.strip().split(sep))
                cols[col_num] = cols.get(col_num, 0) + 1
        print('filename: %s\nrows: %d' % (f, rows))
        for k in cols.keys():
            print('col: %d, count: %d' % (k, cols[k]))

    print('checking finished...')

def genVol(files, out_file_name):

    with open(out_file_name,'w') as fd:
        fd.write("Hello World")
