import random

rules_num = input("num of rules in each file:")
blocks = []
rules_file_num = 10

def write_rules(fp):
    i = 0
    while i < rules_num:
        i = i+1
        blocks_num = random.randint(2,32)  #num of blocks in one rule
        rule = ''
        j = 0
        while j < blocks_num:
            j = j+1
            rule = rule + random.choice(blocks) + '/'
        rule = rule + '\n'
        fp.write(rule)


fr = open('words.txt','r')
while True:
    s = fr.readline()
    if(len(s) <= 0):
        break
    blocks.append(s.split()[0])
fr.close()

while rules_file_num > 0:
    rules_file_num = rules_file_num-1
    filename = 'rules/rules_random_' + str(rules_num) + '_' + str(rules_file_num) + '.txt'
    fw = open(filename,'w')
    write_rules(fw)
    fw.close()
    
