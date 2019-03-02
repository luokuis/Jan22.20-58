
echo 查找 2014 - 2016 年流失的 fid
curr=filter/WORK_FILTER_FOR_CFPS2016FAMCONF_20180.csv
prev=filter/WORK_FILTER_FOR_CFPS2014FAMCONF_17063.csv
fidCurr=fid14
fidPrev=fid14
exportFile=MissFids2014-2016.fid.json

python ./src/ListMissFids.py $curr $prev $fidCurr $fidPrev $exportFile

echo 根据 2014 - 2016 年流失的 fid 的标签
File_RAW=filter/WORK_FILTER_FOR_CFPS2014FAMCONF_17063.csv
File_FIDS=MissFids2014-2016.fid.json
ColPos=0
exportFile=2014.label.csv
python ./src/LabelMaker.py $File_RAW $File_FIDS $ColPos $exportFile


