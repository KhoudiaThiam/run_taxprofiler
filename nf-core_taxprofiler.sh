#!/bin/bash

Help()
{
  
   echo "This project is a automation script for running the pipeline nf-core/taxprofiler. "
   echo
   echo "Usage : bash nf-core/taxprofiler.sh " directory/ TOOL1[TOOL1,TOOL2..]
   echo   
}
directory=$1
tools=$2

ls -v $directory*.fastq.gz > datas_file

#Samplesheet Creation

python3 ./scripts/Samplesheet_generator.py -i datas_file -o samplesheet.csv -t 'I'

#Database Creation

python3 ./scripts/databases_generator.py -t $tools -d database.csv  
tc=$(cat pip.txt)

#Lancement du pipeline

./nextflow run nf-core/taxprofiler --input samplesheet.csv --databases database.csv --outdir ./ -profile docker $tc-resume

while getopts ":h" option; do
   case $option in
      h) # display Help
         Help
         exit;;
     \?) # incorrect option
         echo "Error: Invalid option"
         exit;;
   esac
done


