#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-8
# @Author    : evi
# @Comment   : utilities
# @File      : util.py

# Convert all string items in list to integers
def listStrToInt(l):
    for x in range(len(l)):
        l[x] = int(l[x])

# Read some colums from csv file
def readCSVColums(filename, tableHead=False, cols=None, decode='GBK'):
    if cols == None:
        return None
    with open(filename, 'rb') as fp:
        if not tableHead:
            fp.readline().decode(decode)
        raw = fp.readline().decode(decode)
        items = raw.split(',')
        if len(cols) == 0:
            return None
        res = []
        for i in range(len(cols)):
            res.append([])
        while raw:
            items = raw.split(',')
            c = 0
            for i in cols:
                res[c].append(items[i])
                c = c + 1
            raw = fp.readline().decode(decode)
        return res