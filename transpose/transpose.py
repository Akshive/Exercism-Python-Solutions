def transpose(lines):
    mat = lines.split('\n')
    m = len(mat)
    n = 1
    for word in mat:
        n = max(n, len(word))
        
    ans = ['' for i in range(n)]
    for j in range(n):
        for i in range(m):
            if(j < len(mat[i])):
                ans[j] += mat[i][j]
            else:
                ans[j] += ' '
    ans[n-1] = ans[n-1].rstrip()
    size = len(ans[n-1])
    for i in reversed(range(n-1)):
        ans[i] = ans[i].rstrip()
        while(len(ans[i]) < size):
            ans[i] = ans[i] + ' '
        size = max(size, len(ans[i]))
    return '\n'.join(ans)