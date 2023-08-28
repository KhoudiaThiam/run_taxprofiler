##################################################
##################################################
#####       Author : Ndèye khoudia THIAM     #####
#####         Khoudiathiampro@gmail.com      #####
#####                                        #####
#####              August 2023               #####
#####                                        #####
##################################################
##################################################

import argparse
if __name__ == "__main__":

    #Arguments parser
    parser=argparse.ArgumentParser(
        description='''This program generate a database samplesheet for \
                        the pipeline nf-core/taxprofiler \
        \n ''',
        epilog=""" Have fun ! ^_^ """, usage='%(prog)s [-t TOOL1,TOOL2] [-d database.csv]')
    parser.add_argument('-t','--tools_list',dest='tools', help='List of the classifier we want to use for the pipeline. Make sure all your databases are well installed in your work device. If not, please refer to the nf-core/taxprofiler documentation. ')
    parser.add_argument('-d','--database_ss',dest='database', help='Name of the databases samplesheet file')
    args=parser.parse_args()

    with open (args.database,'w') as dbs:
        dbs.write ('tool,db_name,db_params,db_path'+'\n')
        #Creation of the tool list
        args.tools=args.tools.split(',')
        # A string containing the databases expression for the pipeline parameters
        pipeline=''
        for tool in args.tools:
            tool=tool.lower()
            pipeline+='--run_'+str(tool)+' '
            print(tool)
            if tool == 'kraken2':

                dbs.write('kraken2,'+'db2,'+'--quick'+','+input('/<path>/<to>/kraken2/testdb-kraken2.tar.gz : '))
            
            elif tool == 'bracken':

                Bracken_message ="For Bracken, if you wish to supply any parameters to either the Kraken or Bracken step \
                you must have a semi-colon ; list as in db_params \n. This is to allow to specify the\
                Kraken2 parameters before, and Bracken parameters after the ; as Bracken is a two \
                step process \n. This is particularly important if you supply a Bracken database with \
                a non-default read length parameter\n. If you do not have any parameters to specify,\
                you can leave this as empty.For more information, please take a look at the nf-core/taxprofiler\
                documentation"       
                print(Bracken_message)
                dbs.write('bracken,'+'db1,'+';'+'-r '+input ('database number : ')+','+input('/<path>/<to>/bracken/testdb-bracken.tar.gz : '))

            elif tool == 'malt':
                id_db=input('id : ')
                dbs.write('malt,'+'malt'+str(id_db)+','+'-id '+str(id_db)+','+input('<path>/<to>/malt/testdb-malt/ : '))

            elif tool == 'diamond' or 'kaiju':
                dbs.write(tool.lower()+','+input('database_name: ')+',,'+input('<path>/<to>/tool/ : ')+'\n')
            elif tool == 'centrifuge':
                dbs.write(tool.lower()+','+input('database_name: ')+',,'+input('/<path>/<to>/centrifuge/minigut_cf.tar.gz : ')+'\n')
            elif tool == 'krakenuniq':
                dbs.write(tool.lower()+','+input('database_name: ')+',,'+input('/<path>/<to>/krakenuniq/testdb-krakenuniq.tar.gz : ')+'\n')
            elif tool == 'motus':
                dbs.write(tool.lower()+','+input('database_name: ')+',,'+input('/<path>/<to>/motus/motus_database/ ')+'\n') 
            elif tool == 'metaphlan3':
                dbs.write(tool.lower()+','+input('database_name: ')+',,'+input('/<path>/<to>/metaphlan3/metaphlan_database/' )+'\n') 
            else :
                raise Exception('The tool you gave is not supported by the pipeline. please check the documentation ! ')
    with open('pip.txt','w') as pip:
        pip.write(pipeline)
        
    print("Congrats , the database's samplesheet is generated ! ")



