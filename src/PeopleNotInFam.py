#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-8
# @Author    : evi
# @Comment   : 查找在个人信息中出现但是未在家庭信息中出现的 fid
# @File      : PeopleNotInFam.py

import sys
import util
import json

try:
    famInfoFile    = sys.argv[1]
    famFidCol      = int(sys.argv[2])
    peopleInfoFile = sys.argv[3]
    peopleFidCol   = int(sys.argv[4])
    exportJsonFile = sys.argv[5]
except:
    print('Error: Arg Ill')
    exit(-1)

# Read all fids from family info
print('Reading %s...'%famInfoFile)
fIdsFromFamInfo    = util.readCSVColums(famInfoFile, cols=[famFidCol])[0]
print('Reading %s finished'%famInfoFile)

# Read all fids from family info
print('Reading %s...'%peopleInfoFile)
fIdsFromPeopleInfo = util.readCSVColums(peopleInfoFile, cols=[peopleFidCol])[0]
print('Reading %s finished'%peopleInfoFile)

# Convert strings in list to integers
print('Data Converting...')
util.listStrToInt(fIdsFromFamInfo)
util.listStrToInt(fIdsFromPeopleInfo)

# The missing fids
print('Looking for missing fids...')
missFids = []

for x in fIdsFromPeopleInfo:
    if not x in fIdsFromFamInfo:
        if not x in missFids: # Will not append duplicate fid
            missFids.append(x)

print('共计 %d 个 fid 在 个人信息中出现而未在家庭信息中出现'%len(missFids))

print('家庭信息中含有 %d 个 fid，'%len(set(fIdsFromFamInfo)))
print('个人信息中含有 %d 个 fid，'%len(set(fIdsFromPeopleInfo)))

print('数据校验...')
if len(missFids) == len(set(fIdsFromPeopleInfo)) - len(set(fIdsFromFamInfo)):
    print('数据校验成功')
    with open(exportJsonFile, 'w+') as fp:
        fp.write(json.dumps(missFids))
    print('保存 fid 到文件 %s'%exportJsonFile)
else:
    print('数据校验错误： 家庭信息数据中含有个人信息数据中未出现的 fid')
    