# developer: Milo Sanu
# date: 2016-01-28
# version: 1
# purpose: Rename results of a VBA docx split. Original format PMP0##.docx
# script currently needs to be in same dir as files ready for renaming

from os import system, getcwd, listdir, path
import csv



def search_list(file_path, sfile_name):
    print "Developing Search List"
    f = open(path.join(file_path, sfile_name))
    csvreader = csv.reader(f)
    # reader is a list of lists, row[0] ensures you are grabbing only text.
    repo = [row[0] for row in csvreader]
    f.close()
    return repo


# __file__ returns scripts name as a str
removal_list = ['.DS_Store', '.idea', __file__]


def file_names():
    ''' grab file names in current dir and convert them to lower case'''
    cwd = getcwd()
    nlist = listdir(cwd)
    for x in removal_list:
        try:
            nlist.remove(x)
        except ValueError:
            print "No %s Found" % x
            pass
    return nlist


def __main__(spath,scsv):
    print "Converting File Names"
    slist = search_list(spath, scsv)
    b = file_names()
    print "Moving Files..."
    try:
        for x in range(0, len(b)):
            # print x
            # print slist[int(b[x][3:].strip('.docx'))-1]
            system('mv -v %s %s' % (b[x], 'MTM_' + slist[int(b[x][3:].strip('.docx')) - 1]) + '.docx')
        print "Process Complete"
    except ValueError:
        print 'ValueError %s' % x


__main__()
