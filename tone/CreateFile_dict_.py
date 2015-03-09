import os,re

print 'creating file data/local/dict/extra_questions.txt ...'
ofp = open('local/tone/dict/extra_questions.txt', 'w')
ofp.write('')
ofp.close()

print 'creating file data/local/dict/lexicon.txt ...'
ofp = open('local/tone/dict/lexicon.txt', 'w')
ofp.write('<SIL> SIL\n')
ofp.write('T1 t1\n')
ofp.write('T2 t2\n')
ofp.write('T3 t3\n')
ofp.write('T4 t4\n')
ofp.write('T5 t5\n')
ofp.close()

print 'creating file data/local/dict/nonsilence_phones.txt ...'
ofp = open('local/tone/dict/nonsilence_phones.txt', 'w')
ofp.write('t1\n')
ofp.write('t2\n')
ofp.write('t3\n')
ofp.write('t4\n')
ofp.write('t5\n')
ofp.close()

print 'creating file data/local/dict/optional_silence.txt ...'
ofp = open('local/tone/dict/optional_silence.txt', 'w')
ofp.write('SIL\n')
ofp.close()

print 'creating file data/local/dict/silence_phones.txt ...'
ofp = open('local/tone/dict/silence_phones.txt', 'w')
ofp.write('SIL\n')
ofp.close()
