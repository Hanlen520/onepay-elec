#!C:\Python27\python
# -*- coding: utf-8 -*-
import datetime
import time,re
ltime=time.localtime()
timeStr=time.strftime("%Y%m%d", ltime)
print timeStr

ss="[123]"
if re.search('^\[',ss):
    print "123"