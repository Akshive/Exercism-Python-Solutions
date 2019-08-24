def rotate_char(c, key):
    if(c >= 'a' and c <= 'z'):
        return chr((ord(c) - ord('a') + key)%26 + ord('a'))
    elif(c >= 'A' and c <= 'Z'):
        return chr((ord(c) - ord('A') + key)%26 + ord('A'))
    return c

def rotate(text, key):
    ans = ""
    for i in range(len(text)):
        ans += rotate_char(text[i], key)
    return ans
