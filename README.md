# run_nf-core-taxprofiler

![image](https://github.com/KhoujSunshine/run_nf-core-taxprofiler/assets/100375394/c53c2cbe-36bb-4ec6-a37f-d6e145ace858)


## Automation script for running the pipeline nf-core/taxprofiler

[nf-core/taxprofiler](https://github.com/nf-core/taxprofiler) is a bioinformatics best-practice analysis pipeline for taxonomic classification and profiling of shotgun metagenomic data. It allows for in-parallel taxonomic identification of reads or taxonomic abundance estimation with multiple classification and profiling tools against multiple databases, produces standardised output tables.


This project is a automation script for creating the input needed to run the pipeline nf-core/taxprofiler. 

- The folder **scripts** is the folder containing the python scripts:
  - Samplesheet_generator.py
  - Database_generator.py
- The file **run_taxprofiler.sh** allows the execution of the python files and the nf-core/taxprofiler pipeline

## Description

The main script takes two positionnal arguments:

- The first one is the path to the directory containing the samples you want to analyze
- the second argument is the chain of the profiling tools you want to use (Kraken2,Bracken,KrakenUniq,MetaPhlan3,Malt,DIAMOND,Centrifuge,Kaiju,mOTUs).

It's allow the generation of the main samplesheet(Samplesheet_generator.py) and the database samplesheet from the profilers chain (database_generator.py)

- The first python script take as arguments a list of samples, the NGS type (*ILLUMINA* or *NANOPORE*) and returns the main samplesheet. 
- The second one takes profiling tools chain as argument and return the database samplesheet.
  
The resulting files of those two scripts : *samplesheet.csv* & *database.csv* will be used as input for the pipeline.

![image](https://github.com/KhoujSunshine/run_nf-core-taxprofiler/assets/100375394/ff128eff-1eac-4cf8-accb-45666fea6b45)

## Usage

```
./run_taxprofiler.sh  data_directory/ <TOOL1>,<TOOL2>
```
Example :
```
./run_taxprofiler.sh  data/ Centrifuge,Motus,Kaiju
```

If you want to generate the samplesheet separately, you need a file containing all your samples :

data.txt

<p align="center">
   <img width="658" alt="image" src="https://github.com/KhoujSunshine/run_nf-core-taxprofiler/assets/100375394/2847aaeb-320d-412f-8f95-d5d78bf29de5">
</p>

```
./scripts/Samplesheet_generator.py -i data_file.txt -o samplesheet.csv -t ['I'/'N']
```
example :
```
./scripts/Samplesheet_generator.py -i data.txt -o samplesheet.csv -t 'I'
```
 will return the samplesheet :
 
 <p align="center">
<img width="667" alt="image" src="https://github.com/KhoujSunshine/run_nf-core-taxprofiler/assets/100375394/926c0cd8-676a-4c24-8e3b-28867a39a2b0">
 </p>
 

## Contact

If you found an issue or would like to submit an improvment to this project , you can contact me via [LinkedIn](https://www.linkedin.com/in/ndeye-khoudia-thiam/) or by email (khoudiathiampro@gmail.com)

