# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""
from functools import partial

from . import sqliteUtils
import sqlite3

def commandToolMode(db_conn):
	sentinel = ';'
	while 1:
		commands = []
		command = input("command >> ").strip()
		if command in ['exit','exit;','exit()']:
			db_conn.close()
			break
		if command == '':
			continue
		elif command in ['commit;','rollback;']:
			if command == 'commit;': db_conn.commit()
			if command == 'rollback;': db_conn.rollback()
		elif command[0] in ('@','.'):
			dealWithCommand(db_conn, command)
		elif command.find(';') != -1:
			dealWithSQL(db_conn,command)
		else:
			commands.append(command)
			input_new = partial(input, '\t... ')
			for command in iter(input_new, sentinel):
				commands.append(command)
				if command.find(';') != -1:
					break
			command = ' '.join(commands)
			dealWithSQL(db_conn,command)

def dealWithCommand(conn, command):
	if command[0] == '.':
		sqliteUtils.dealInnerCommand(conn, command)
	elif command[0] == '@':
		sqliteUtils.dealInnerSQL(conn,command)
	else:
		print('error: no such command')


def dealWithSQL(conn, command):
    c = conn.cursor()
    try:
    	cursor = c.execute(command)
    	for row in cursor:
    		print(row)
    except Exception as e:
    	print(repr(e))

