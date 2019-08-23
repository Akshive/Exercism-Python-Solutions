def is_isogram(string):
    str = string.lower()
    setA = set([])
    for c in str:
        if(c in setA and c >= 'a' and c <= 'z'):
            return False
        setA.add(c)
    return True

