

'''

Remove Repeated Words in conn2_out.txt

INPUTS:

conn2_out.txt

OUTPUTS:

conn2_lv2.txt

'''


f = open('conn2_out.txt', 'r')
fw = open('conn2_lv2.txt', 'w')

pastlist = []

sta = ''

while 1:
	s = f.readline().decode('gbk')
	if not s: break
	sq = s.split('_')
	if len(sq) >= 3:
		if sq[1] in pastlist:
			continue
		pastlist.append(sq[1])
		
		if sta != '':
			fw.write(sta)
			sta = ''
		
		fw.write(s.encode('gbk'))
	elif len(s) ==1:
		# blank return
		pass
	else:
		sta = s.encode('gbk')
	
	
	