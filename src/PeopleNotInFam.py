#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-8
# @Author    : evi
# @Comment   : 查找在个人信息中出现但是未在家庭信息中出现的 fid
# @File      : PeopleNotInFam.py

import sys
import pandas as pd
import json

try:
    familyInfoFile = sys.argv[1]
    peopleInfoFile = sys.argv[2]
    fidColName     = sys.argv[3]
    exportJsonFile = sys.argv[4]
except:
    print('Error: Arg Ill')
    exit(-1)

print('Reading %s...'%familyInfoFile)
FamData = pd.read_csv(familyInfoFile, low_memory=False, encoding='GBK')
print('Reading %s finished'%familyInfoFile)

print('Reading %s...'%peopleInfoFile)
PeopleData = pd.read_csv(peopleInfoFile, low_memory=False, encoding='GBK')
print('Reading %s finished'%peopleInfoFile)

FidsNotInFamilyData = []

print('Data Converting...')
UniqFidsInPeople = list(set(PeopleData[fidColName]))
UniqFidsInFamily = list(set(FamData[fidColName]))

print('Looking for missing fids...')
for fid in UniqFidsInPeople:
    if not fid in UniqFidsInFamily and not fid in FidsNotInFamilyData:
        FidsNotInFamilyData.append(fid)
FidsNotInFamilyData.sort()

print('共计 %d 个 fid 在 个人信息中出现而未在家庭信息中出现'%len(FidsNotInFamilyData))

print('家庭信息中含有 %d 个 fid，'%len(UniqFidsInFamily))
print('个人信息中含有 %d 个 fid，'%len(UniqFidsInPeople))

print('数据校验...')
if len(FidsNotInFamilyData) == len(UniqFidsInPeople) - len(UniqFidsInFamily):
    print('数据校验成功')
    with open(exportJsonFile, 'w+') as fp:
        fp.write(json.dumps(FidsNotInFamilyData))
    print('保存 fid 到文件 %s'%exportJsonFile)
else:
    print('数据校验错误： 家庭信息数据中含有个人信息数据中未出现的 fid')