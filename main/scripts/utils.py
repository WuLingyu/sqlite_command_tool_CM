# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""
import os

def fullFile(full_path, files):
    temp = []
    for f in files:
        temp.append(os.path.join(full_path, f))
    return temp

def clearCache():
    q_list = [] # common queue
    t_list = [] # list used to store target file 

    # current folder as root
    cur = os.getcwd()
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

def genVol(files, out_file_name):
    
    with open(out_file_name,'w') as fd:
        fd.write("Hello World")
