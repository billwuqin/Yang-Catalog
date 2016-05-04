#!/usr/bin/python
import argparse
import os.path
import re
import sys, getopt

__author__ = 'Anurag Bhargava, Qin Wu'
__email__ = "anuragb@cisco.com, bill.wu@huawei.com"
__version__ = "1.0"
	
def extract_type(input_file, dst_path, dst_file, type, mode):
	
    finput=open(input_file, "r")
    alllines=finput.readlines()
    finput.close();
    foutput = 0
    ismatch = 0
    nextmatch= 0
    #TYPE_TAG_1 = r"^[\t]*" + re.escape(type)+ r"/s .*$"
    #TYPE_TAG = re.compile(TYPE_TAG_1)

    output_file = dst_path + dst_file

    if mode == 'False':
            foutput = open(output_file, 'a')
    else:
            foutput = open(output_file, 'w')
    print ('type = '+ type)
    foutput.writelines(type +':')
    for eachline in alllines:
        spos = eachline.find(type,)
        first = eachline.split()
        if nextmatch == 1:
            for p in first:
                foutput.writelines('\t'+p)
            nextmatch = 0
            break
        if spos >= 0 and first[0] == type and len(first)>1:
        #match = TYPE_TAG.match(eachline)
        #if match:
            ismatch = 1
            foutput.writelines('\t'+first[1]+'\n')
            break
        elif spos >=0 and first[0]==type and len(first)==1:
            nextmatch =1
            #next(alllines)
            #foutput.writelines('\t'+nt+'\n')
        else:
            continue
    if ismatch == 0:
        foutput.writelines('\n')
    foutput.close
	
	
def extract(argv):
    input_file = ''
    dst_file = ''
    type = 'all'
    mode = ''
	
    try:
        opts, args = getopt.getopt(argv,"hi:o:t:m:",["ifile=","ofile=","type=", "mode="])
    except getopt.GetoptError:
        print ('yang_data_model_catalog.py -i <inputfile> -o <outputfile> -t <type> -m <mode>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('yang_data_model_catalog.py -i <inputfile> -o <outputfile> -t <type> -m <True for overwite or False for append>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            dst_file = arg
        elif opt in ("-t", "--type"):
            type = arg
        elif opt in ("-m", "--mode"):
             mode = arg
                
    print ('Input file is ', input_file)
    print ('Output file is ', dst_file)
    print ('Mode is "', mode)
    dst_path = './'
    if type == 'all':
            extract_type(input_file, dst_path, dst_file, 'prefix', 'True')
            extract_type(input_file, dst_path, dst_file, 'namespace', 'False')
            extract_type(input_file, dst_path, dst_file, 'module_version', 'False')
            extract_type(input_file, dst_path, dst_file, 'revision', 'False')
            extract_type(input_file, dst_path, dst_file, 'module', 'False')
            extract_type(input_file, dst_path, dst_file, 'contact', 'False')
    else:
            extract_type(input_file, dst_path, dst_file, type, mode)
	
if __name__ == "__main__":
    extract(sys.argv[1:])


