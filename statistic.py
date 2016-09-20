max_blocks_num = 0
avg_blocks_num = 0
sum_blocks_num = 0
max_block_len = 0
avg_block_len = 0
sum_block_len = 0

blocks_num = 2
while blocks_num <= 32:
    filename = 'test/test_unmatch_' + str(blocks_num) + '.txt'
    fp = open(filename,'r')
    
    max_blocks_num = 0
    avg_blocks_num = 0
    sum_blocks_num = 0
    max_block_len = 0
    avg_block_len = 0
    sum_block_len = 0
    
    while True:
        p = fp.readline()
        if(len(p) <= 0):
            break

        tmp = p.split('/')
        del tmp[-1]
        sum_blocks_num = sum_blocks_num + len(tmp)
        if max_blocks_num < len(tmp):
            max_blocks_num = len(tmp)

        for block in tmp:
            sum_block_len = sum_block_len + len(block)
            if max_block_len < len(block):
                max_block_len = len(block)
                
    avg_blocks_num = sum_blocks_num/5120
    avg_block_len = sum_block_len/sum_blocks_num
    print filename
    print "max_blocks_num:%d  avg_blocks_num:%d  sum_blocks_num:%d"%\
          (max_blocks_num,avg_blocks_num,sum_blocks_num)
    print "max_block_len:%d  avg_block_len:%d  sum_block_len:%d"%\
          (max_block_len,avg_block_len,sum_block_len)
    blocks_num = blocks_num+1
    

        
        
