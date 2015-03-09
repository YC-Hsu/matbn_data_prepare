import os,re,sys

if len(sys.argv) != 2 :
	print "Usage: " + sys.argv[0] + " [options] <data-dir>"
	print "e.g.: " + sys.argv[0] + " data/train"
	print "options: "
	print "			"
else :
	ifp = open(sys.argv[1] + '/text', 'r')
	ofp = open(sys.argv[1] + '/utt2spk', 'w')
	
	while True:
		line = ifp.readline()
		if not line: 
			break
		list = re.split('_| |-',line)
		if len(list) == 6 :
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'_'+list[3]+'-'+list[4]+' ')
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'\n')
		elif len(list) == 5 :
			ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'-'+list[3]+' ')
			ofp.write(list[0]+'_'+list[1]+'\n')
		else :
			print '[ERROR!] some format error ! possibly serious !'
			break

	ifp.close()
	ofp.close()
