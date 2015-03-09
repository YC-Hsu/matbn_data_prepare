import os,re
'''
ifp1 = open('data/train/text', 'r')
ofp1 = open('data/train/wav.scp', 'w')
wav_dir = '/home/deer/kaldi-trunk/egs/matbn/t3/train_wave/'

while True:
	line = ifp1.readline()
	if not line: 
		break
	list = re.split('_| |-',line)
	ofp1.write(list[0]+'_'+list[1]+'_'+list[2]+'_'+list[3]+'-'+list[4]+' ')
	ofp1.write(wav_dir+list[0]+'_'+list[1]+'_'+list[2]+'.wav\n')

ifp1.close()
ofp1.close()
'''
'''
ofp1 = open('data/test/wav.scp', 'w')
wav_dir = '/home/deer/kaldi-trunk/egs/matbn/t3/eval_wave/'

print 'prepare data/test/wav.scp ...'
for root, dirs, files in os.walk(wav_dir):
	for f in files:
		fname = re.split('\.', f)
		ofp1.write(fname[0]+' '+wav_dir+f+'\n')

ofp1.close()
'''

ofp1 = open('data/train/wav.scp', 'w')
wav_dir = '/home/deer/kaldi-trunk/egs/matbn/t3/train_wave/'

print 'prepare data/train/wav.scp ...'
for root, dirs, files in os.walk(wav_dir):
	for f in files:
		fname = re.split('\.', f)
		ofp1.write(fname[0]+' '+wav_dir+f+'\n')

ofp1.close()
