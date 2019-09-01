def append(list1, list2):
    res = list1
    for item in list2:
        res.append(item)
    return res


def concat(lists):
    res = []
    for list_i in lists:
        for item in list_i:
            res.append(item)
    return res


def filter(function, list):
    res = []
    for item in list:
        if(function(item) == True):
            res.append(item)
    return res


def length(list):
    return(len(list))


def map(function, list):
    res = []
    for item in list:
        res.append(function(item))
    return res

def foldl(function, list, initial):
    res = initial
    for item in list:
        res = function(res, item)
    return res


def foldr(function, list, initial):
    res = initial
    list.reverse()
    for item in list:
        res = function(item, res)
    return res


def reverse(list):
    res = list
    res.reverse()
    return res
