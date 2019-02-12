#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-02-9
# @Author    : evi
# @Comment   : utilities
# @File      : util.py

# Check each colum's length same as the others
def checkColums(cols):
    lls = []
    for x in cols:
        lls.append(len(x))
    if len(set(lls)) == 1:
        return True
    return False

# Combine colums and wirte to CSV file
def writeCSVFromColums(filename, cols):
    if not checkColums(cols):
        return False
    with open(filename, 'w+') as fp:
        lines = len(cols[0])
        for c in range(lines):
            buf = ''
            for x in cols:
                buf += str(x[c])
                buf += ','
            fp.write(buf[:-1])
            fp.write('\n')
    return True

# If the string end with '\n', delete '\n'
def noEndlineSymbol(s):
    if s[-1:] == '\n':
        return s[:-1]
    else:
        return s

# Scan CSV file, using one colum as condition...
def scanCSVRecordByOneColum(filename, ls, cid, tableHead=False, decode='GBK'):
    rec = []
    with open(filename, 'rb') as fp:
        if not tableHead:
            fp.readline().decode(decode)
        raw = fp.readline().decode(decode)
        while raw:
            rawls = raw.split(',')
            if rawls[cid] in ls:
                rec.append(noEndlineSymbol(raw))
            raw = fp.readline().decode(decode)
    return rec

# Convert all string items in list to integers
def listStrToInt(l):
    for x in range(len(l)):
        l[x] = int(l[x])

# Convert all integers items in list to string
def listIntToStr(l):
    for x in range(len(l)):
        l[x] = str(l[x])

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