# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""

import os, sys
import sqlite3

def initDB():
	db_name = 'db.sqlite'
	cur = os.path.split(sys.argv[0])[0]
	db_path = os.path.join(cur, db_name)
	conn = sqlite3.connect(db_path)
	return conn


def sqlite_manager(db_conn):
	headers = ['type','name','tbl_name','rootpage','sql']
	pass


def dealInnerCommand(conn, command):
	cmds = command.strip().split()
	if cmds[0] == '.load':
		# load file into DB
		print(os.getcwd())
		print(cmds[1:])


def dealInnerSQL(conn, command):
	pass