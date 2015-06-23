import os

dic = []
glist = []

def prepare_dic():
    f = open('list_in.txt', 'r')
    while 1:
        s = f.readline().decode('gbk')
        if not s: break
        if len(s) < 2: continue
        dic.append(s)
    print 'prepare dic finished'

def findStrWord(s):
    for k in dic:
        if k.split('\t')[1] == s:
            return k.replace('\t', '_')
    return s

def load_autogroup(filename):
    f = open(filename, 'r')
    while 1:
        s = f.readline().decode('gbk')
        if not s: break
        
        s = s.split(',')
        if len(s) <= 3: continue
        
        item1 = s[0] + '_' + s[1]
        ulist = [item1]
        
        for k in s[2:]:
            ulist.append(k.strip())
            
        glist.append(ulist)
    print 'load glist finished'

def load_autogroups():
    flist = os.listdir('.')
    for k in flist:
        if k.lower().find('autogroup')!=-1:
            print 'loading ', k
            load_autogroup(k)
    'load autogroups finished'

def writeFile():
    f = open('conn2_out.txt', 'w')
    i = 0
    for k in glist:
        i+=1;
        if i%10==0:
            print 'writing group ', i, '\\', len(glist)   
        
        f.write(k[0].encode('gbk')+'\n\n')
        for k1 in k[1:]:
            f.write( findStrWord(k1).encode('gbk') )
        f.write('\n')
    print 'writing file finished'

prepare_dic()
load_autogroups()
writeFile()