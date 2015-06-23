f = open('list_in_gre.txt', 'r')

fw = open('list_in_gre1.txt','w')

line = 0

while 1:
    s = f.readline().decode('gbk')
    if not s: break
    s = s.split('\t')
    
    line+=1
    print line
    
    if len(s) > 1:
        q = []
        for k in s:
            q.append(k.encode('gbk'))
        
        fw.write(str(line) + '\t'+q[0]+'\t'+q[1]+'\n')

print 'fin'
    
f.close()
fw.close()