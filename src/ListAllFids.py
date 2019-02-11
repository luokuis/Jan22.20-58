#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-10
# @Author    : evi
# @Comment   : 收集所有不同的 fid 保存到文件
# @File      : ListAllFids.py

import sys
import json
import util

try:
    fileName = sys.argv[1]
    columId  = int(sys.argv[2])
    exportTo = sys.argv[3]
except:
    print('Error: Arg Ill')
    exit(-1)


# Read all fids from file
print('Reading %s...'%fileName)
fIds   = util.readCSVColums(fileName, cols=[columId])[0]
print('Reading %s finished'%fileName)

util.listStrToInt(fIds)
print('Read %d fids'%len(fIds))

# Convert strings in list to integers
print('Data Converting...')
uniqueFids = list(set(fIds))

print('Got %d unique fids'%len(uniqueFids))

with open(exportTo, 'w+') as fp:
    fp.write(json.dumps(uniqueFids))
