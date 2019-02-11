#! /usr/bin/bash

echo 查找所有出现在个人信息数据中但是未出现在家庭信息数据中的 fid
read -p "是否进行操作，输入 y 进行操作，否则跳过(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	fam=2010/cfps2010family_report_nat092014.dta.csv
	famFidCol=0
	people=2010/cfps2010famconf_report_nat092014.csv
	peopleFidCol=1
	exportFile=PeopleNotInFam2010.fid.json

	python ./src/PeopleNotInFam.py $fam $famFidCol $people $peopleFidCol $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 查找所有出现在家庭信息数据中的 fid
read -p "是否进行操作，输入 y 进行操作，否则跳过(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	fam=2010/cfps2010family_report_nat092014.dta.csv
	famFidCol=0
	exportFile=AllFamFids2010.fid.json

	python ./src/ListAllFids.py $fam $famFidCol $exportFile
fi

echo
echo ------------------ 我是分割线 ------------------
echo

echo 查找所有出现在个人信息数据中的 fid
read -p "是否进行操作，输入 y 进行操作，否则跳过(y/n): " choice
echo $choice

if [[ $choice == y ]]; then
	people=2010/cfps2010famconf_report_nat092014.csv
	peopleFidCol=1
	exportFile=AllPeopleFids2010.fid.json

	python ./src/ListAllFids.py $people $peopleFidCol $exportFile
fi