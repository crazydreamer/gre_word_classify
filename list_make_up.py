#coding: utf8

f = open("list.txt", 'r')
fw = open("list1.txt", 'w')

for i in range(0,9999):
	s = f.readline()
	s = s.replace('\n', '')
	sq = s.split('\t')
	if len(sq) < 2:
		fw.write(' ' + s)
	else:
		fw.write('\n')
		fw.write(s)