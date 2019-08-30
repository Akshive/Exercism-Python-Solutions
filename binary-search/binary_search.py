def find(search_list, value):
    i = 0
    j = len(search_list)-1
    if(j < 0):
        raise ValueError('Invalid Args !')
    while(i < j):
        m = int((i+j)/2)
        if(search_list[m] < value):
            i = m+1
        else:
            j = m
    if(search_list[j] != value):
        raise ValueError('Not Found !')
    return j
        
