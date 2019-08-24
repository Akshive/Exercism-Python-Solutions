def slices(series, length):
    size = len(series)
    if(length > size or length <= 0):
        raise ValueError('Invlaid Argument')
    ans = []
    for i in range(0, size-length+1):
        ans.append(series[i:i+length])
    return ans