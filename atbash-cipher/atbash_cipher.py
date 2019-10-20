def isChar(c):
    if((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')):
        return True
    return False

def encode(plain_text):
    ans = ""
    plain_text = plain_text.lower()
    i = 0
    for c in plain_text:
        if(isChar(c)):
            t = 25 - (ord(c) - ord('a')) + ord('a')
            ans += chr(t)
            i += 1
        elif(c >= '0' and c <= '9'):
            ans += c
            i += 1
        if(i == 5):
            ans += ' '
            i = 0
    return ans.strip()
    
def decode(ciphered_text):
    ans = ""
    ciphered_text = ciphered_text.lower()
    for c in ciphered_text:
        if(isChar(c)):
            t = 25 - (ord(c) - ord('a')) + ord('a')
            ans += chr(t)
        elif(c >= '0' and c <= '9'):
            ans += c
    return ans.strip()
 