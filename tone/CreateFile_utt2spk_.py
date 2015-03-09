import os,re

ifp = open('data/train/text', 'r')
ofp = open('data/train/utt2spk', 'w')

while True:
	line = ifp.readline()
	if not line: 
		break
	list = re.split('_| |-',line)
	ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'_'+list[3]+'-'+list[4]+' ')
	ofp.write(list[0]+'_'+list[1]+'_'+list[2]+'\n')

ifp.close()
ofp.close()
