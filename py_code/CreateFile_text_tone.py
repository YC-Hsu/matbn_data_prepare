# -*- coding: utf-8 -*-
import os,re,sys

def trans2tone(phone):
	if syllable_label(phone) == 'FINAL' :
		return 'T'+str(phone[len(phone)-1])
	else :
		return 'T0'
		
def syllable_label(phone):
	if phone == 'SIL' :
		return 'SIL'
	elif phone[len(phone)-1].isdigit() :
		return 'FINAL'
	else :
		return 'INITIAL'
	
		
def CleanName(name):
	list = re.split('_',name)
	return str(list[0]+'_'+str(list[1]))


if len(sys.argv) != 4 :
	print "Usage: " + sys.argv[0] + " [options] <transitions-state> <ali-file> <output-file>"
	print "e.g.: " + sys.argv[0] + " data/lang/tmp/state_and_phone.txt exp/mono0a_train_ali/tmp/mono0a_train_ali.txt data/train/text"
	print "options: "
	print "			"
else :
	ifp = open(sys.argv[1], 'r')
	current_phone=''
	index=0
	phone_index=['1']
	for i in range(0,10000) :
		phone_index.append(0)
	
	while True:
		line = ifp.readline()
		if not line: 
			break
		line_list = re.split(' ',line)
		if line_list[0] == 'Transition-state' :
			current_phone = line_list[4]
		elif line_list[1] == 'Transition-id' :
			index = int(line_list[3],10)
			phone_index[index] = current_phone
		else :
			ssss=0
			
	ifp.close()

	#產生一般text，以每個聲母韻母為切割點，each segments可能小於0.05秒，過小的片段make_mfcc_pitch似乎是不接受的
	ifp = open(sys.argv[2], 'r')
	ofp = open(sys.argv[3] + '_haveT0', 'w')
	current_phone='init'
	current_wave='init'
	start=0
	end=-1
	while True:
		line = ifp.readline()
		if not line: 
			break
		line_list = re.split(' ',line)
		record_id = line_list[0]
		current_phone='init'
		if current_wave != record_id :
			start = 0
			end = -1
			current_wave = record_id
		for i in range(1,len(line_list)-1) :
			if current_phone != phone_index[int(line_list[i])] :
				if i > 1 :
					ofp.write(str(end)+' '+str(trans2tone(current_phone))+'\n')
				current_phone = phone_index[int(line_list[i])]
				start=end+1
				end+=1
				ofp.write(str(record_id)+'_'+str(start)+'-')
			else :
				end+=1
		ofp.write(str(end)+' '+str(trans2tone(current_phone))+'\n')
	ifp.close()
	ofp.close()

	ifp = open(sys.argv[3] + '_haveT0', 'r')
	ofp = open(sys.argv[3], 'w')
	skip_count=0
	
	while True:
		line = ifp.readline()
		if not line: 
			break
		line_list = re.split('-|_| |\n',line)
		if len(line_list) == 7 :
			if line_list[5] != 'T0' :
				if int(line_list[4]) - int(line_list[3]) > 0 :
					ofp.write(str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '_' + str(line_list[3]) + '-' + str(line_list[4]))
					ofp.write(' ' + str(line_list[5]) + '\n')
				else :
					print '[Warning] Segment' + str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '_' + str(line_list[3]) + '-' + str(line_list[4]) + ' too short, skipping it.'
					skip_count+=1
		elif len(line_list) == 6 :
			if line_list[4] != 'T0' :
				if int(line_list[3]) - int(line_list[2]) > 0 :
					ofp.write(str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '-' + str(line_list[3]))
					ofp.write(' ' + str(line_list[4]) + '\n')
				else :
					print '[Warning] Segment' + str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '-' + str(line_list[3]) + ' too short, skipping it.'
					skip_count+=1
		else :
			print '[ERROR!] some format error ! possibly serious !'
			break

	print 'Total skip ' + str(skip_count) + ' texts.'
	ifp.close()
	ofp.close()


'''
#
ifp = open('data/train/text_phone', 'r')
ofp = open('data/train/text', 'w')

label0_flag = 0
text_label = ''
last_name = ''			#上一個segments的音檔需與當前的(current_name)相同，否則不合併
current_name = ''
start = 0
end = -1
while True:
	line = ifp.readline()
	if not line: 
		break
	line_list = re.split('-|_| |\n',line)
	if syllable_label(line_list[5]) == 'SIL' :
		#do nothing
		label0_flag = 0
		text_label = ''
		start = 0
		end = -1
	elif syllable_label(line_list[5]) == 'INITIAL' :
		label0_flag = 1
		text_label = trans2tone(line_list[5])
		start = int(line_list[3])
		end = int(line_list[4])
		last_name = str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2])
	else :
		current_name = str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2])
		if label0_flag == 1 and current_name == last_name :
			text_label += ' ' + trans2tone(line_list[5])
			end = int(line_list[4])
			ofp.write(str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '_' + str(start) + '-' + str(end))
			ofp.write(' ' + text_label + '\n')
		else :
			#do nothing
			label0_flag = 0
			text_label = ''
			start = 0
			end = -1

ifp.close()
ofp.close()
'''