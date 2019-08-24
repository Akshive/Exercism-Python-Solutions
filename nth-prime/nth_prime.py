def prime(number):
    if(number == 0):
        raise ValueError('Invalid Args')
    limit = 1000000
    isPrime = [True for i in range(limit+1)]
    i = 4
    while i <= limit:
        isPrime[i] = False
        i += 2

    i = 3
    while i*i <= limit:
        if(isPrime[i] == True):
            j = 2*i
            while j <= limit:
                isPrime[j] = False
                j += i
        i += 2
    
    ans = []
    for i in range(2, limit+1):
        if(isPrime[i] == True):ans.append(i)
    return ans[number-1]
