# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""

from . import ruleDealer

import os, sys
import sqlite3

def initDB():
	db_name = 'db.sqlite'
	cur = os.path.split(sys.argv[0])[0]
	db_path = os.path.join(cur, db_name)
	db_conn = sqlite3.connect(db_path)
	return db_conn


def sqlite_manager(db_conn):
	headers = ['type','name','tbl_name','rootpage','sql']
	pass

def format_output(db_conn, sql):
	(table_name, col_names) = ruleDealer.sql_parser(db_conn,sql)
	return col_names

def dealInnerCommand(db_conn, command):
	cmds = command.strip().split()
	if cmds[0] == '.load':
		# load file into DB
		print(os.getcwd())
		print(cmds[1:])

def dealInnerSQL(db_conn, command):
	pass


def dealWithSQL(db_conn, command):
    c = db_conn.cursor()
    try:
    	cursor = c.execute(command)
    	col_names = format_output(db_conn, command)
    	if col_names == []:
    		print('no column info found!')
    	else:
    		print('|'.join(col_names))
    	for row in cursor:
    		print("|".join(['%s' for _ in range(len(row))]) % row)
    except Exception as e:
    	print(repr(e))