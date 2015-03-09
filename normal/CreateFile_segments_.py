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
