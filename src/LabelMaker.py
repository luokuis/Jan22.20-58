#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time      : 2019-03-2
# @Author    : evi
# @Comment   : 
# @File      : LabelMaker.py

import sys
import json
import util

try:
    File_RAW       = sys.argv[1]
    File_FIDS      = sys.argv[2]
    Fid_ColPos     = int(sys.argv[3])
    exportJsonFile = sys.argv[4]
except:
    print('Error: Arg Ill')
    exit(-1)

print(File_RAW, File_FIDS, exportJsonFile)

fids = []

with open(File_FIDS, 'r') as fp:
    fids = json.loads(fp.read())

# util.listIntToStr(fids)

outPut = open(exportJsonFile, 'w+')

with open(File_RAW, 'r') as fp:
	tableHead = fp.readline()
	outPut.write(util.noEndlineSymbol(tableHead))
	outPut.write(', label\n')
	raw = fp.readline()
	while raw:
		rawls = raw.split(',')
		if int(rawls[Fid_ColPos]) in fids:
			outPut.write(util.noEndlineSymbol(raw))
			outPut.write(', 1\n')
		else:
			outPut.write(util.noEndlineSymbol(raw))
			outPut.write(', 0\n')
		raw = fp.readline()

outPut.close()

