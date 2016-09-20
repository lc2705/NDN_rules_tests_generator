rules_num_list = [10000,100000,1000000]


rules_file = 'rules/random/rules_random_'
match_test_file = 'test/random/test_match_random_'
unmatch_test_file = 'test/random/test_unmatch_random_'

def count_prefix(index,filename):
    fp = open(filename, 'r')

    max_blocks_num = 0
    avg_blocks_num = 0
    sum_blocks_num = 0
    max_block_len = 0
    avg_block_len = 0
    sum_block_len = 0
    prefix_num = 0

    count_list = [0 for x in range(2,44)] #index is from 0 to 30
    
    while True:
        p = fp.readline()
        if(len(p) <= 0):
            break
        
        prefix_num = prefix_num+1
        tmp = p.split('/')
        del tmp[-1]
        count_list[len(tmp)-2] = count_list[len(tmp)-2] + 1
        
        sum_blocks_num = sum_blocks_num + len(tmp)
        if max_blocks_num < len(tmp):
            max_blocks_num = len(tmp)

        for block in tmp:
            sum_block_len = sum_block_len + len(block)
            if max_block_len < len(block):
                max_block_len = len(block)
                
    avg_blocks_num = sum_blocks_num/prefix_num
    avg_block_len = sum_block_len/sum_blocks_num
    print filename
    print "prefix_num:%d" % prefix_num
    print "max_blocks_num:%d  avg_blocks_num:%d  sum_blocks_num:%d"%\
          (max_blocks_num,avg_blocks_num,sum_blocks_num)
    print "max_block_len:%d  avg_block_len:%d  sum_block_len:%d"%\
          (max_block_len,avg_block_len,sum_block_len)
    print 'count_list:'
    print count_list
    print '\n'


for rules_num in rules_num_list:
    index = 0
    while index < 10:
        count_prefix(index,rules_file + str(rules_num) + '_' +str(index) + '.txt')
        count_prefix(index,match_test_file + str(rules_num) + '_' + str(index) + '.txt')
        count_prefix(index,unmatch_test_file + str(rules_num) + '_' +str(index) + '.txt')
        index = index+1
