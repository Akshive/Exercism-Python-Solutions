def flatten(iterable):
    if(iterable == None):
        return []
    ans = []
    try:
        for element in iterable:
            ans.extend(flatten(element))
    except:
        ans.append(iterable)
    return ans