import os,re,sys

if len(sys.argv) != 2 :
	print "Usage: " + sys.argv[0] + " [options] <lang-dir>"
	print "e.g.: " + sys.argv[0] + " data/lang"
	print "options: "
	print "			"
else :
	print 'creating file data/lang/G.txt ...'
	ofp = open(sys.argv[1] + '/G.txt', 'w')
	ofp.write('0\t1\t<eps>\t<eps>\n')
	ofp.write('1\t2\tT1\tT1\t0\n')
	ofp.write('1\t3\tT2\tT2\t0\n')
	ofp.write('1\t4\tT3\tT3\t0\n')
	ofp.write('1\t5\tT4\tT4\t0\n')
	ofp.write('1\t6\tT5\tT5\t0\n')
	ofp.write('2\t7\t<eps>\t<eps>\n')
	ofp.write('3\t7\t<eps>\t<eps>\n')
	ofp.write('4\t7\t<eps>\t<eps>\n')
	ofp.write('5\t7\t<eps>\t<eps>\n')
	ofp.write('6\t7\t<eps>\t<eps>\n')
	ofp.write('7')
	ofp.close()