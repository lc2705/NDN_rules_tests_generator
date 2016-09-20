fp = open('dict.txt','r')
fw = open('words.txt','w')

while True:
    s = fp.readline()
    s = s.lstrip()
    if(len(s) <= 0):
        break
    fw.write(s.split()[0] + '\n')

fp.close()
fw.close()
