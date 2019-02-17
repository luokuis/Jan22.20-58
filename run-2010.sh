#! /usr/bin/bash

echo 查找所有出现在个人信息数据中但是未出现在家庭信息数据中的 fid
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	family=2010/cfps2010family_report_nat092014.dta.csv
	people=2010/cfps2010famconf_report_nat092014.csv
	fidColName=fid
	exportFile=PeopleNotInFam2010.fid.json

	python ./src/PeopleNotInFam.py $family $people $fidColName $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 将所有出现在个人信息数据中但是未出现在家庭信息数据中的个人信息保存到 CSV 文件
read -p "是否进行操作，输入 y 进行操作(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	keyFile=PeopleNotInFam2010.fid.json
	people=2010/cfps2010famconf_report_nat092014.csv
	peopleFidCol=1
	exportFile=PeopleNotInFam2010.csv

	python ./src/ScanCSVBySingleColum.py $keyFile $people $peopleFidCol $exportFile
fi