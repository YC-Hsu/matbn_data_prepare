#-*- coding: utf-8 -*-
import os,re

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



ifp = open('local/src/state_and_phone.txt', 'r')
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
ifp = open('local/src/mono0a_ali.all', 'r')
ofp = open('data/train/text_haveT0', 'w')
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

ifp = open('data/train/text_haveT0', 'r')
ofp = open('data/train/text', 'w')
skip_count=0

while True:
	line = ifp.readline()
	if not line: 
		break
	line_list = re.split('-|_| |\n',line)
	if line_list[5] != 'T0' :
		if int(line_list[4]) - int(line_list[3]) > 2 :
			ofp.write(str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '_' + str(line_list[3]) + '-' + str(line_list[4]))
			ofp.write(' ' + str(line_list[5]) + '\n')
		else :
			print '[Warning] Segment' + str(line_list[0]) + '_' + str(line_list[1]) + '_' + str(line_list[2]) + '_' + str(line_list[3]) + '-' + str(line_list[4]) + ' too short, skipping it.'
			skip_count+=1

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