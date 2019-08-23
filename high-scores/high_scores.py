def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    dup_scores = scores
    dup_scores.sort()
    ans = []
    size = len(dup_scores)
    ans.append(dup_scores[size-1])
    if(size > 1):ans.append(dup_scores[size-2])
    if(size > 2):ans.append(dup_scores[size-3])
    return ans
    
