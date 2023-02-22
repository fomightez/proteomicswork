#!/usr/bin/env python
# extract_gene_list_from_screen_copied_MitCOM_data.py
__author__ = "Wayne Decatur" #fomightez on GitHub
__license__ = "MIT"
__version__ = "0.1.0"


# extract_gene_list_from_screen_copied_MitCOM_data.py by 
# Wayne Decatur
# ver 0.1
#
#*******************************************************************************
# Verified compatible with both Python 2.7 and Python 3.6; written initially in 
# Python 3. 
#
#
# PURPOSE: Takes data in a file copy-pasted from MitCOM 
# (https://www.complexomics.org/datasets/mitcom) and extracts the standard gene 
# names to a new file. One gene name to each line.
# It will process any file in the same directory that ends in `.md` (setting at 
# momemnt), and so save the input files with that extension and without spaces.
#
# Initially main code developed in 
# `MitCOM_data_extractor_initial_development.ipynb`
#
#
# 
#
# Written to run from command line or imported into/pasted/loaded inside a 
# Jupyter notebook cell. 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Dependencies beyond the mostly standard libraries/modules:
# NONE
#
#
# VERSION HISTORY:
# v.0.1. basic working version. 
#
# To do:
# - verify compatible with Python 2.7
# - ??
#
#
#
# TO RUN:
# Examples,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python extract_gene_list_from_screen_copied_MitCOM_data.py
#-----------------------------------
#
# Issue `extract_gene_list_from_screen_copied_MitCOM_data.py -h` for details.
# 
#
#
# To use this after importing/pasting or loading into a cell in a Jupyter 
# notebook, call the main function similar to below:
# extract_gene_list_from_screen_copied_MitCOM_data.py()
#
# 
#
'''
CURRENT ACTUAL CODE FOR RUNNING/TESTING IN A NOTEBOOK WHEN IMPORTED/LOADED OR 
PASTED IN ANOTHER CELL:
extract_gene_list_from_screen_copied_MitCOM_data.py()
'''
#
#
#*******************************************************************************
#





#*******************************************************************************
##################################
#  USER ADJUSTABLE VALUES        #

##################################
#

extension_for_processing = ".md"
suffix_for_saving = "_EXTRACTEDgenes"
extension_for_saving = ".tsv"

#
#*******************************************************************************
#**********************END USER ADJUSTABLE VARIABLES****************************






















#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###

import sys
import os
from pathlib import Path
import glob
 

###---------------------------HELPER FUNCTIONS-------------------------------###

def generate_output_file_name(file_name,suffix_for_saving):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file name.


    Specific example
    =================
    Calling function with
        ("data.md", "_EXTRACTEDgenes")
    returns
        "data_EXTRACTEDgenes.tsv"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        file_name) #from 
    #http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    if '.' in file_name:  #I don't know if this is needed with the os.path.splitext method but I had it before so left it
        return main_part_of_name + suffix_for_saving  + extension_for_saving
    else:
        return file_name + suffix_for_saving + extension_for_saving


def extract_gene_names_to_file(file_name):
    '''
    Takes a file name as an argument and extracts from the copied-pasted text 
    the gene names for the proteins to a new file. The generated name of the 
    output files is based on the original file name.

    Specific example
    =================
    Calling function with
        ("data.md")
    generates
        "data_EXTRACTEDgenes.tsv"
    '''
    # Feedback
    sys.stderr.write("Processing {}...\n".format(file_name))
    #input_file_name = Path("file_name")
    #input_file_name_main_stem = input_file_name.stem # see https://stackoverflow.com/a/47496703/8508004
    #output_file_name_suffix = "_EXTRACTEDgenes"
    #output_file_name = f"{input_file_name_main_stem}_{output_file_name_suffix}.tsv"
    output_file_name = generate_output_file_name(file_name,suffix_for_saving)
    

    # Read entire input file into memory at once so can use strip to remove the initial whitespace usualy present
    with open(file_name, 'r') as file_handle:
        input_data=file_handle.read().strip()
        #input_data = [x for x in input_data.split("\n") if x] # remove blank lines
        input_data = [x for x in input_data.split("\n") if x.strip()] # remove blank lines & lines that are just tabs and empty spaces
    # prepare output file for saving so it will be open and ready
    with open(output_file_name, 'w') as output_file_handle:
        # print header to the tsv file
        output_file_handle.write("gene_name"+"\n")

        # iterate over ithe input file data
        cycle_len = 3 # number of lines of content, i.e., discounting lines with no text, each gene has in the copied data
        for indx,line in enumerate(input_data):
            #count_within_gene_section = int(indx/cycle)
            count_within_gene_section = indx%cycle_len 
            if count_within_gene_section == 1:
                output_file_handle.write(line.strip()+"\n")
            #if count_within_gene_section == 2:
            #   cycle += 1
    sys.stderr.write("Saved gene names in {}.\n".format(output_file_name))




###--------------------------END OF HELPER FUNCTIONS-------------------------###
###--------------------------END OF HELPER FUNCTIONS-------------------------###



#*******************************************************************************
###------------------------'main' function of script--------------------------##

def extract_gene_list_from_screen_copied_MitCOM_data():
    '''
    Main function of script.
    Iterates on an file in same directory that matches extension setting for 
    input and extracts the gene names for the proteins to a new file.
    Each new file will be based on the input file.
    '''
    # ITERATE ON INPUT FILES:
    #--------------------------------------------------------------------------#
    files_ending_in_md = glob.glob(os.path.join('.','*.md')) 
    for file_name in files_ending_in_md:
        extract_gene_names_to_file(file_name)
    

    
###--------------------------END OF MAIN FUNCTION----------------------------###
###--------------------------END OF MAIN FUNCTION----------------------------###










#*******************************************************************************
###------------------------'main' section of script---------------------------##
def main():
    """ Main entry point of the script """
    # placing actual main action in a 'helper'script so can call that easily 
    # with a distinguishing name in Jupyter notebooks, where `main()` may get
    # assigned multiple times depending how many scripts imported/pasted in.
    kwargs = {}
    #kwargs['case_sensitive'] = case_sensitive
    extract_gene_list_from_screen_copied_MitCOM_data(*kwargs)
    # using https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/#calling-a-function
    # to build keyword arguments to pass to the function above
    # (see https://stackoverflow.com/a/28986876/8508004 and
    # https://stackoverflow.com/a/1496355/8508004 
    # (maybe https://stackoverflow.com/a/7437238/8508004 might help too) for 
    # related help). Makes it easy to add more later.






if __name__ == "__main__" and '__file__' in globals():
    """ This is executed when run from the command line """
    # Code with just `if __name__ == "__main__":` alone will be run if pasted
    # into a notebook. The addition of ` and '__file__' in globals()` is based
    # on https://stackoverflow.com/a/22923872/8508004
    # See also https://stackoverflow.com/a/22424821/8508004 for an option to 
    # provide arguments when prototyping a full script in the notebook.
    ###-----------------for parsing command line arguments-------------------###
    import argparse
    
    parser = argparse.ArgumentParser(prog=
        'extract_gene_list_from_screen_copied_MitCOM_data.py',
        description="extract_gene_list_from_screen_copied_MitCOM_data.py \
        estracts standard gene names from text files containing data \
        copy-pasted from screen seen when working with MitCOM. \
        **** Script by Wayne Decatur   \
        (fomightez @ github) ***")

    

    args = parser.parse_args()



    
    main()

#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************