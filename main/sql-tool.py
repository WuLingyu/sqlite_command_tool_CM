# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 20:47:00 2017

@author: lingyu
"""

from scripts import sqliteTool

import argparse
import readline

def command_tool_mode():
    while 1:
        input = raw_input("command >> ")
        if input in ['exit','exit()']:
            break
        sqliteTool.dealWithCommand()

def volatility(files):
    if len(files) < 2: print "Required at least two files"
    

def initialize():
    print "init"

def main():
    # create parser
    descStr = """
    This program provides some helpful functions for ZW group in CM-GZ
    """
    parser = argparse.ArgumentParser(description=descStr)
    
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()
    
    # add expected arguments
    group.add_argument('-s', action='store_true', 
                       help='shell mode',required=False)
    group.add_argument('-init',action='store_true',
                       help='create sqlite file and configuration file',
                       required=False)
    group.add_argument('-vol', nargs='*',
                       help='''volatility of files with same structure. 
                       tips: -vol file1 ,file2, [file3, ...]''',
                       required=False)

    # parse args
    args = parser.parse_args()
    
    if args.s:
        try:
            command_tool_mode()
        except KeyboardInterrupt:
            print("Goodbye~")
    elif args.vol:
        volatility(args.vol)
    elif args.init:
        initialize()
    else:
        parser.print_help()
    

if __name__ == '__main__':
    main()

