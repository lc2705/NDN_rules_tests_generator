import random

sample_list = 'abcdefghijklmnopqrstuvwxyz'

def match_test(fr,fw,blocks_num,times):
    fr.seek(0,0)
    while True:
        cnt = 0
        rule = fr.readline()
        if(len(rule) <= 0):
            break

        while cnt < times:
            test = rule.split()[0]
            add_blocks = random.randint(0, 10)
            while add_blocks > 0:
                add_blocks = add_blocks-1
                block_len = random.randint(2,20)
                while block_len > 0:
                    block_len = block_len-1
                    test = test + random.choice(sample_list)
                test = test + '/'
            test = test + '\n'
            fw.write(test)
            cnt = cnt + 1
            
    print 'write match test file from rules_' + str(blocks_num)


def unmatch_test(fr,fw,blocks_num,times):
    fr.seek(0,0)
    while True:
        cnt = 0
        rule = fr.readline()
        if(len(rule) <= 0):
            break

        while cnt < times:
            test = ''
            tmp = rule.split('/')
            del tmp[-1]
            for block in tmp:
                block_list = list(block)
                random.shuffle(block_list)
                block = ''
                block = block.join(block_list)
                test = test + block + '/'

            add_blocks = random.randint(0, 10)
            while add_blocks > 0:
                add_blocks = add_blocks-1
                block_len = random.randint(2,20)
                while block_len > 0:
                    block_len = block_len-1
                    test = test + random.choice(sample_list)
                test = test + '/'
            test = test + '\n'
            fw.write(test)
            cnt = cnt+1
    print 'write unmatch test file from rules_' + str(blocks_num)              
           
        

blocks_num = 2
while blocks_num <= 32:
    file_rules = 'rules/rules_' + str(blocks_num) + '.txt'
    file_match = 'test/test_match_' + str(blocks_num) + '.txt'
    file_unmatch = 'test/test_unmatch_' + str(blocks_num) + '.txt'
    fr = open(file_rules,'r')
    fmatch = open(file_match,'w')
    funmatch = open(file_unmatch, 'w')
    
    match_test(fr, fmatch, blocks_num,5)
    unmatch_test(fr, funmatch, blocks_num,5)
    
    fr.close()
    fmatch.close()
    funmatch.close()

    blocks_num = blocks_num+1
