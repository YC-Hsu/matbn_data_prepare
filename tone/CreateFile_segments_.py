import os,re

ifp = open('data/train/text', 'r')
ofp = open('data/train/segments', 'w')

while True:
	line = ifp.readline()
	if not line: 
		break
	list = re.split('_| |-',line)
	ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'_'+list[3]+'-'+list[4]+' ')
	ofp.write(list[0]+'_'+list[1]+'_'+list[2]+' ')
	ofp.write(str(float(list[3])/100)+' '+str(float(list[4])/100)+'\n')

ifp.close()
ofp.close()


import os,re,sys

if len(sys.argv) != 2 :
	print "Usage: " + sys.argv[0] + " [options] <data-dir>"
	print "e.g.: " + sys.argv[0] + " data/train"
	print "options: "
	print "			"
else :
	ifp = open(sys.argv[1] + '/text', 'r')
	ofp = open(sys.argv[1] + '/segments', 'w')
	
	while True:
		line = ifp.readline()
		if not line: 
			break
		list = re.split('_| |-',line)
		if len(list) == 6 :
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'_'+list[3]+'-'+list[4]+' ')
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+' ')
			ofp.write(str(float(list[3])/100)+' '+str(float(list[4])/100)+'\n')
		elif len(list) == 5 :
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'-'+list[3]+' ')
			ofp.write(list[0]+'_'+list[1]+' ')
			ofp.write(str(float(list[2])/100)+' '+str(float(list[3])/100)+'\n')
		else :
			print '[ERROR!] some format error ! possibly serious !'
			break
			