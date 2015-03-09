# -*- coding: utf-8 -*-
import os,re,sys

if len(sys.argv) != 3 :
	print "Usage: " + sys.argv[0] + " [options] <wav-dir> <output-file>"
	print "e.g.: " + sys.argv[0] + " /mnt/corpus/MATBN/MATBN_DEV_292 data/dev/wav.scp"
	print "options: "
	print "			"
else :
	ofp = open(sys.argv[2], 'w')
	wav_dir = sys.argv[1]
	
	for root, dirs, files in os.walk(wav_dir):
		for f in files:
			fname = re.split('\.', f)
			ofp.write(fname[0]+' '+wav_dir+f+'\n')
	
	ofp.close()
