#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os,sys
import  MySQLdb

try:
   db = MySQLdb.connect(host ='127.0.0.1', user='wordpress', passwd='wordpress6826', db ='wordpress')
except MySQLdb.ERROR,e:
   print "Error %d:%s"%(e.args[0],e.args[1])
   exit(1)
cursor = db.cursor()
cursor.execute('select * from wp_post')
result_set=cursor.fetchall()
print result_set
cursor.close()
db.close()