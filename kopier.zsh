#!/bin/zsh -x
for i in {1..1000}
do
    newpath="data/data_$i.parquet"
    cp data/data.parquet $newpath
done