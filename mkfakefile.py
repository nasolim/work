import subprocess as s
import random as r

i_name = str(raw_input("What name would you like to use?>\n"))
count = int(raw_input("How many files would you like made?>\n"))+1

def mkffile(i_name,count):
	'''Make a group of fake pdf files. Provide fake name'''
	number = "49934324%s" % (r.randint(1,99))
	date = "2015-12-04-17-35-14-613" 
	id_selection = r.randint(1,3)
	if id_selection == 1:
		in_id = "FLU"
	elif id_selection == 2:
		in_id = "FL0"
	else:
		in_id = "180"
	fake_member_number = r.randint(1,100000)
	file_name = number + "_" + i_name + "_" + in_id + str(fake_member_number)+ "_" + date + ".pdf"
	return file_name



for x in xrange(1,count):
	name = mkffile(i_name,count)
	s.call(["touch",name])
	print "File number %s created: %s" % (x, name) 
