#! /usr/bin/env python3
# -*-coding:Utf-8 -*

#exemple de ligne de commande: python mainSDF.py -t split -a test.sdf 

import os,sys 

import argparse
import analysis.split as sp_an   #import du module
import analysis.concatenate as cc_an
import analysis.update as up_an 
import analysis.extract as ex_an

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", help="""what type of task ? split, extract, concatenate or update""")
    parser.add_argument("-a","--datafile",help="""SDF files you want to manipulate""") 
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    datafile = args.datafile 
    if args.task == 'split':
        sp_an.launch_analysis(datafile)
    elif args.task == 'concatenate':
        cc_an.launch_analysis(datafile)
    elif args.task == 'extract':
        ex_an.launch_analysis(datafile)
    elif args.task == 'update':
        up_an.launch_analysis(datafile) 
    else :
        print("task argument is not acceptable")




