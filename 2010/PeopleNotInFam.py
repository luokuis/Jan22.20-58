#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-8
# @Author    : evi
# @Comment   : 查找在个人信息中出现但是未在家庭信息中出现的 fid
# @File      : PeopleNotInFam.py

import util
import json

exportJsonFile = 'PeopleNotInFam.fid.json'
famInfoFile    = 'cfps2010family_report_nat092014.dta.csv'
peopleInfoFile = 'cfps2010famconf_report_nat092014.csv'

# Read all fids from family info
print('Reading %s...'%famInfoFile)
fIdsFromFamInfo    = util.readCSVColums(famInfoFile, cols=[0])[0]
print('Reading %s finished'%famInfoFile)

# Read all fids from family info
print('Reading %s...'%peopleInfoFile)
fIdsFromPeopleInfo = util.readCSVColums(peopleInfoFile, cols=[1])[0]
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
        s = json.dumps(missFids)
        fp.write(s)
    print('保存 fid 到文件 %s'%exportJsonFile)
else:
    print('数据校验错误： 家庭信息数据中含有个人信息数据中未出现的 fid')
    