#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-15
# @Author    : evi
# @Comment   : 列出流失的 fid
# @File      : ListMissFids.py

import pandas as pd
import sys
import json
import util

try:
    File_CURR      = sys.argv[1]
    File_PREV      = sys.argv[2]
    ColName_CURR   = sys.argv[3]
    ColName_PREV   = sys.argv[4]
    exportJsonFile = sys.argv[5]
except:
    print('Error: Arg Ill')
    exit(-1)

illFid = set([-8])

print('Reading %s...'%File_PREV)
Data_PREV = pd.read_csv(File_PREV, low_memory=False, encoding='GBK')
print('Reading %s finished'%File_PREV)

print('Reading %s...'%File_CURR)
Data_CURR = pd.read_csv(File_CURR, low_memory=False, encoding='GBK')
print('Reading %s finished'%File_CURR)

print('Extracting %s in %s...'%(ColName_CURR, File_CURR))
sfid_CURR = set(Data_CURR[ColName_CURR]) - illFid

print('Extracting %s in %s...'%(ColName_PREV, File_PREV))
sfid_PREV = set(Data_PREV[ColName_PREV]) - illFid


missFids = sfid_PREV - sfid_CURR

if len(sfid_PREV) - len(sfid_CURR) == len(missFids):
    print('发现 %d 个流失的 fid'%len(missFids))
    print('数据校验成功')
else:
    print('%s 中含有 %d 个 %s，%s 中含有 %d 个 %s，发现 %d 个流失的 fid'%
        (File_CURR, len(sfid_CURR), ColName_CURR, File_PREV, len(sfid_PREV),
            ColName_PREV, len(missFids)))
    print('数据校验错误')
    exit(-2)
with open(exportJsonFile, 'w+') as fp:
    fp.write(json.dumps(list(missFids)))
    print('保存 fid 到文件 %s'%exportJsonFile)
    