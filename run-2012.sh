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
	people10=2012/cfps2012famros_092015.csv
	people12=2012/cfps2012famros_092015.csv
	fidColName10=fid
	fidColName12=fid12
	exportFile=MissFids2010-2012.fid.json

	python ./src/ListMissFids.py $people12 $people10 $fidColName12 $fidColName10 $exportFile
fi
