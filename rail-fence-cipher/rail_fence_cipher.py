def sort(message, index_array):
    ans = [' ' for i in range(len(message))]
    for i in range(len(message)):
        ans[index_array[i]] = message[i]
    return ''.join(ans)
    
def encode(message, rails):
    if(rails == 1 or rails == len(message)):
        return message
    idx = 0
    ans = ['' for i in range(len(message))]
    flag = 0
    for c in message:
        ans[idx] += c
        if(flag == 0):
            idx += 1 
        else:
            idx -= 1 
        if(idx == rails-1 or idx == 0):
            flag = 1-flag
    return ''.join(ans)
    
def decode(message, rails):
    m = len(message)
    n = rails
    gap = [0 for i in range(n)]
    gap[0] = 2*n - 3
    gap[n-1] = gap[0]
    for i in range(1, n-1):
        gap[i] = gap[i-1] - 2
    #print(gap)
    a = [0 for i in range(m)]
    idx = 0
    for i in range(1, m):
        if(a[i-1] + gap[idx] + 1 >= m):
            idx += 1
            a[i] = idx
        else:
            a[i] = a[i-1] + gap[idx] + 1
            if(idx != 0 and idx != n-1):
                gap[idx] = gap[0]-1-gap[idx]
    #print(a)
    return sort(message, a)

