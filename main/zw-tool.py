# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 20:47:00 2017

@author: lingyu
"""

from scripts import commandTool
from scripts import sqliteUtils
from scripts import utils

from datetime import datetime

import argparse
import configparser
import readline

# DEBUG_MODE will clear cache before the program runs
DEBUG_MODE = True

def volatility(files):
    if len(files) < 2: print("PROMOT: Required at least two files")
    output_file_name = input("Result file name (default: result_yyyymmddhhmmss.txt): ")
    if output_file_name == '':
        output_file_name = 'result_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
    utils.genVol(files,output_file_name)
    
def main():
    db_conn = sqliteUtils.initDB()
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
    group.add_argument('-vol', nargs='*',
                       help='''volatility of files with same structure. 
                       tips: -vol file1 ,file2, [file3, ...]''',
                       required=False)
    
    # parse args
    args = parser.parse_args()
    
    if args.s:
        try:
            commandTool.commandToolMode(db_conn)
        except KeyboardInterrupt:
            db_conn.commit()
            db_conn.close()
            print("\n"+ "Goodbye".center(50,'='))
    elif args.vol:
        volatility(args.vol)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
    # if debug mode is True, clear cache everytime
    if DEBUG_MODE:
        utils.clearCache()

