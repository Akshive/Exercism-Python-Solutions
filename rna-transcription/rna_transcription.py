def to_rna(dna_strand):
    ans = ""
    for c in dna_strand:
        if(c == 'G'):ans += 'C'
        elif(c == 'C'):ans += 'G'
        elif(c == 'A'):ans += 'U'
        else: ans+='A'
    return ans
