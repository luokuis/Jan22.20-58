#! /usr/bin/bash

echo 查找所有出现在个人信息数据中但是未出现在家庭信息数据中的 fid
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	family=2012/cfps2012family_092015.csv
	people=2012/cfps2012famros_092015.csv
	fidColName=fid12
	exportFile=PeopleNotInFam2012.fid.json

	python ./src/PeopleNotInFam.py $family $people $fidColName $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 查找 2010 年到 2012 年流失的 fid
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	people12=2012/cfps2012famros_092015.csv
	people10=2010/cfps2010famconf_report_nat092014.csv
	fidColName10=fid
	fidColName12=fid10
	exportFile=MissFids2010-2012.fid.json

	python ./src/ListMissFids.py $people12 $people10 $fidColName12 $fidColName10 $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 列出 2010 年到 2012 流失的人
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	keyFile=MissFids2010-2012.fid.json
	people10=2010/cfps2010famconf_report_nat092014.csv
	fidColId=1
	exportFile=MissPeople2010-2012.csv

	python ./src/ScanCSVBySingleColum.py $keyFile $people10 $fidColId $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 列出 2010 年到 2012 流失的家庭
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	keyFile=MissFids2010-2012.fid.json
	people10=2010/cfps2010family_report_nat092014.dta.csv
	fidColId=0
	exportFile=MissFamily2010-2012.csv

	python ./src/ScanCSVBySingleColum.py $keyFile $people10 $fidColId $exportFile
fi
