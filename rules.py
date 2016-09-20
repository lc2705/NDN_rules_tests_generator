import random

rules_num = 1024
blocks = []

def write_rules(fp,block_num):
    i = 0
    while i < rules_num:
        j = 0
        rule = ''
        while j < block_num:
            rule = rule + random.choice(blocks) + '/'
            j = j+1
        rule = rule + '\n'
       # print rule
        i = i+1
        fp.write(rule)
    return

fr = open('words.txt','r')
while True:
    s = fr.readline()
    if(len(s) <= 0):
        break 
    blocks.append(s.split()[0])
fr.close()

block_num = 2
while block_num <= 32:
    filename = 'rules/rules_' + str(block_num) + '.txt'
    fw = open(filename,'w')
    write_rules(fw,block_num)
    fw.close()
    block_num = block_num + 1
    

