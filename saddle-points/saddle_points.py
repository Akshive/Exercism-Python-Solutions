def is_smallest(matrix, x, y):
    m = len(matrix)
    for i in range(m):
        if(matrix[i][y] < matrix[x][y]): return False
    return True

def is_largest(matrix, x, y):
    n = len(matrix[0])
    for j in range(n):
        if(matrix[x][j] > matrix[x][y]): return False
    return True

def saddle_points(matrix):
    ans = []
    m = len(matrix)
    if(m == 0): return [{}]
    n = len(matrix[0])
    for i in range(m):
        if(len(matrix[i]) != n):
            raise ValueError('Invalid Arg')
    for i in range(m):
        for j in range(n):
            if(is_smallest(matrix, i, j) == True and is_largest(matrix, i, j) == True):
                ans.append({'row': i+1, 'column': j+1})
    if(len(ans) == 0):return [{}]
    return ans
