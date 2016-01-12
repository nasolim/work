# developer: Milo Sanu
# date: 2015-12-07
# version: 1
# description: Create a new directory and moves all
# pdf files with the FL marker into the new directory.

import subprocess as s
from os import system,getcwd,chdir
from time import sleep
from commands import getstatusoutput as gso

def process(date):
	"""Create a new directory.
returns SUNSHINE_FAXES-date.""" 
	name = "SUNSHINE_FAXES-" + date
	s.call(["mkdir",name])
	sleep(2)
	print "\nDirectory Created: %s" % (name)
	return name
	

def mv_files(name):
	"""Move files to name directory using terminal command line."""
	print "Sending files to %s" % (name)
	sleep(1)
	system('mv *_FL* %s' % name) 
	print "File Transfer Complete"


def file_count():
	"""Count the number of files within specified directory."""
	count = gso('ls | wc -l')[1]
	return count

def main():
        date = str(raw_input("What date would you like to use? YYYY-MM-DD\n>   "))

        file = process(date)
        total_count = file_count()
        mv_files(file)
        new_count = file_count()
        path = getcwd() + "/" + file
        chdir(path)
        new_dir_count = file_count()

        return '''
New Directory and Transfer Process Complete.
Total Files Before Transfer:  %s
Total Files After Transfer:   %s
Total Files In New Directory: %s
''' % (total_count, new_count, new_dir_count)


#print main()
