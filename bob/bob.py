def no_letter(str):
    size = len(str)
    for i in range(size):
        if((str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z')):return False
    return True

def is_empty(str):
    for i in range(len(str)):
        if(str[i] != ' ' and str[i] != '\t' and str[i] != '\n' and str[i] != '\r'):
            return False
    return True

def is_question(str):
    for i in range(len(str)-1, -1, -1):
        if(str[i] != ' '):
            if(str[i] != '?'):return False
            return True
    return False

def is_all_capitals(str):
    if(no_letter(str)):
        return False
    size = len(str)
    for i in range(size):
        if(str[i] >= 'a' and str[i] <= 'z'):return False
    return True

def response(hey_bob):
    size = len(hey_bob)
    if(size == 0 or is_empty(hey_bob)):
        return "Fine. Be that way!"
    if(is_question(hey_bob)):
        if(is_all_capitals(hey_bob)):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if(is_all_capitals(hey_bob)):
        return "Whoa, chill out!"
    return "Whatever."
