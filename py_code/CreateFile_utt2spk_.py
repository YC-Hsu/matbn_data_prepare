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
		list = re.split(' ',line)
		ofp.write(list[0]+' '+list[0]+'\n')

	ifp.close()
	ofp.close()
