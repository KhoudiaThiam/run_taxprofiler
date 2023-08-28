##################################################
##################################################
#####	   Author : Ndèye khoudia THIAM	 #####
#####		 Khoudiathiampro@gmail.com	  #####
#####										#####
#####			  August 2023			   #####
#####										#####
##################################################
##################################################

import argparse

def diffstrings(s1, s2):

	"""

	Parameters
	============
	s1 : string1
	s2 : string2

	Return
	============

	The number of different characters between 2 strings

	"""
	if len(s1) != len(s2):
		distance=2
		return distance
		
	distance = 0
	for char1, char2 in zip(s1, s2):
		if char1 != char2:
			distance += 1

	return distance

if __name__ == "__main__":

	#Arguments parser
	parser=argparse.ArgumentParser(
		description='''This program generate the main samplesheet  for \
						the pipeline nf-core/taxprofiler \
		\n Take a look''',
		epilog=""" Have fun ! ^_^ """, usage="%(prog)s [-i filename] [-o samplesheet.csv] [-t 'I']")
	parser.add_argument('-i','--in',dest='filein', help='List of the samples')
	parser.add_argument('-o','--out',dest='fileout', help='Name of the samplesheet')
	parser.add_argument('-t','--type',dest='type', help='Type of NGS used')

	args=parser.parse_args()

	#Short reads case
	if args.type== 'I':
		type_s=',ILLUMINA'
	#Long reads	case
	elif args.type== 'N':
		type_s=',OXFORD_NANOPORE'

	with open(args.fileout,'w') as samplesheet:

		samplesheet.write('sample,run_accession,instrument_platform,fastq_1,fastq_2,fasta'+'\n')

		with open(args.filein, 'r+') as sample_file:
			all_datas=[] #List of All the samples in our directory
			paired_end=[] #List of the paired end files
			already_used=[] #List of the added files (in the samplesheet) 
			for line in sample_file:
				line=line.rstrip()
				all_datas.append(line)
			for i in range(len(all_datas)):
				if diffstrings(all_datas[i-1],all_datas[i]) == 1:
					#Paired End files usually differs from one character ( The numbers 1 et 2 following the sample name)
					paired_end.append([all_datas[i-1],all_datas[i]])
					already_used.append(all_datas[i-1]) ; already_used.append(all_datas[i])	
			#List of the single end files
			single_end=list(set(all_datas)-set(already_used))	

		#Writing the Single End files on the samplesheet
		i=1
		for element in single_end:
			samplesheet.write((str(i)+',')+'run'+str(i)+type_s+','+'./'+element+','+','+'\n')
			i+=1
		#Writing the Paired End files on the samplesheet	
		for element in paired_end:
			samplesheet.write((str(i)+',')+'run'+str(i)+type_s+','+'./'+element[0]+','+'./'+element[1]+','+'\n')
			i+=1
print(" Congrats , the main samplesheet is generated !")
