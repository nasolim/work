# developer: Milo Sanu
# date: 2016-01-08
# version: 1
# description: Create a new directory and moves all
# client faxes to a new directory.

import subprocess as s
from os import path,system,getcwd,chdir
from time import sleep
from commands import getstatusoutput as gso
import csv
import functools


def dir_creator(dir_name):
	"""Create a new directory""" 
	s.call(["mkdir",dir_name])
	sleep(2)
	print "\nDirectory Created: %s \n" % (dir_name)
	return dir_name
	

def mv_files(search_term,direc_name):
	"""Move files to name directory using terminal command line."""
	print "Preparing to send files to %s" % (direc_name)
	system('mv *_%s* %s' % (search_term,direc_name)) 
	print "File Transfer Complete"

def search_list(f_path,file_name):
	print "searching..."
	f = open(path.join(f_path,file_name))
	csvreader = csv.reader(f)
	#reader is a list of lists, row[0] ensures you are grabbing only text
	repo = [row[0] for row in csvreader]
	f.close()
	return repo


def file_count():
	"""Count the number of files within specified directory."""
	count = gso('ls | wc -l')[1]
	return count

def main():
        dir_name = str(raw_input("New Directory Name?\n>   "))
		#create your new directory
        dir_creator(dir_name)
        #determine total number of files to be scanned
        total_count = file_count()
        #provide search term list and it's location
        f_path = str(raw_input("What is the path to your list file?\n>"))
        file_name = str(raw_input("\nWhat is the name and ext of your file?\n>"))
        ids = search_list(f_path, file_name)
        #map files names through move process
        print "Sending files to: %s" % dir_name
        map(functools.partial(mv_files, direc_name = dir_name), ids)
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


#print main()