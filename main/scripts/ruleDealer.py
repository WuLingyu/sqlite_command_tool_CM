# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:21:26 2017

@author: lingyu
"""

import re

def sql_parser(db_conn,sql):
	# format sql
	# remove comments
	p = re.compile(r'\/\*.*\*\/')
	comments = p.findall(sql)
	for comment in set(comments):
		sql.replace(comment, ' ')

	# remove unnecessary space
	while sql.find('  ') != -1:
		sql = sql.replace('  ',' ')
	print(sql)
	if True:
		return ('sqlite_master', ['type','name','tbl_name','rootpage','sql'])
	else:
		return ('',[])
