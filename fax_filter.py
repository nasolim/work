# developer: Milo Sanu
# date: 2016-01-08
# version: 1.1
# description: Create a new directory and moves all
# client faxes to a new directory.

import subprocess as s
from os import path, system, getcwd, chdir, mkdir
from time import sleep
from commands import getstatusoutput as gso
import csv
import functools


def dir_creator(dir_name):
    """Create a new directory"""
    mkdir(dir_name)
    sleep(2)
    print "\nDirectory Created: %s \n" % (dir_name)
    return dir_name


def mv_files(search_term, direc_name):
    """Move files to name directory using terminal command line."""
    print "Preparing to send files to %s" % (direc_name)
    system('ls >> my_temp_list.txt')  #sent file list to .txt
    a = lambda x: system('grep %s my_temp_list.txt >> my_refined_temp_list.txt' % x)
    map(a, search_term)  #search for file of interest, add to new .txt
    path = getcwd()
    refined_list = search_list(path, 'my_refined_temp_list.txt')  #extract name to iter list
    s = lambda x: system('mv %s %s' % (x, direc_name))
    map(s, refined_list)
    system('rm my_temp_list.txt my_refined_temp_list.txt')
    print "File Transfer Complete"


def search_list(file_path, file_name):
    print "\nsearching..."
    f = open(path.join(file_path, file_name))
    csvreader = csv.reader(f)
    # reader is a list of lists, row[0] ensures you are grabbing only text.
    repo = [row[0] for row in csvreader]
    f.close()
    return repo


def file_count():
    """Count the number of files within specified directory."""
    count = gso('ls | wc -l')[1]
    return count


def main():
    working_path = str(raw_input("Provide absolute path to the files that need to be filtered?\n>	"))
    chdir(working_path)
    dir_name = str(raw_input("Directory Name for filtered files?\n>   "))
    # create your new directory
    dir_creator(dir_name)
    # determine total number of files to be scanned
    total_count = file_count()
    # provide search term list and it's location
    file_name = str(raw_input("\nWhat is the name and ext of your file?\n>	"))
    f_path = str(raw_input("Provide absolute path to your search list?\n>"))
    ids = search_list(f_path, file_name)
    # map files names through move process
    print "Sending files to: %s" % dir_name
    mv_files(ids, dir_name)
    new_count = file_count()
    path = getcwd() + "/" + dir_name
    chdir(path)
    new_dir_count = file_count()

    return '''
New Directory and Transfer Process Complete.
Total Files Before Transfer:  %s
Total Files After Transfer:   %s
Total Files In New Directory: %s
''' % (total_count, new_count, new_dir_count)


print main()
