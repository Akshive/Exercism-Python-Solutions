def classify(number):
    if(number <= 0):
        raise ValueError('Invalid')
    num = number
    i = 2
    ans = 1
    while(i*i <= number):
        cnt = 0
        while(number%i == 0):
            number = number/i
            cnt += 1
        #print("{} {} {}".format(i, cnt, ans))
        ans = (ans*(i**(cnt+1)-1))/(i-1)
        if(i == 2):
            i += 1 
        else:
            i += 2
    if(number > 1):
        #print("{} {}".format(number, 1))
        ans = (ans*(number**2-1))/(number-1)
    #print(ans)
    if(ans > 2*num):
        return "abundant"
    elif(ans == 2*num):
        return "perfect"
    else:
        return "deficient"