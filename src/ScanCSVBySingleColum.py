#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-12
# @Author    : evi
# @Comment   : 根据 CSV 中的某一列元素匹配记录并保存到文件
# @File      : ScanCSVBySingleColum.py

import sys
import json
import util

try:
    keyFile        = sys.argv[1]
    peopleInfoFile = sys.argv[2]
    fidColId       = int(sys.argv[3])
    exportFile     = sys.argv[4]
except:
    exit(-1)
    print('Error: Arg Ill')

keys = []

with open(keyFile, 'r') as fp:
    keys = json.loads(fp.read())

util.listIntToStr(keys)

print('Scaning %s...'%peopleInfoFile)
res = util.scanCSVRecordByOneColum(peopleInfoFile, keys, fidColId)
print('Scaning %s finished'%peopleInfoFile)

print('Saving file %s...'%exportFile)
with open(exportFile, 'w+') as fp:
    for x in res:
        fp.write(x)
        fp.write('\n')
print('Saving file %s Successed'%exportFile)