import itertools

#start to string
start_str=''.join(map(str,[it for it in range(1,start+1)]))
#get all perm
allresult=itertools.permutations(start_str, end)


def checking(sequence):
    '''
    get sequence and return true if it ok
    '''
    for it in range(0,len(sequence)-1):
        if int(sequence[it])+1!=int(sequence[it+1]) :
            if sequence[it+1]=='1' and sequence[it]==str(start):
                continue
            return False
    return True

#drop wrong result
total_result=list(filter(checking,allresult))

print(total_result)
[('1', '2', '3', '4'), ('2', '3', '4', '5'), ('3', '4', '5', '1'), ('4', '5', '1', '2'), ('5', '1', '2', '3')]
