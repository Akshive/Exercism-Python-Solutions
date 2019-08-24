def primes(limit):
    isPrime = [True for i in range(limit+1)]
    i = 4
    while i <= limit:
        isPrime[i] = False
        i += 2

    i = 3
    while i*i <= limit:
        if(isPrime[i] == True):
            j = 3*i
            while j <= limit:
                isPrime[j] = False
                j += 2*i
        i += 2
    
    ans = []
    for i in range(2, limit+1):
        if(isPrime[i] == True):ans.append(i)
    return ans
