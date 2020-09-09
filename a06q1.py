# ------------------------------------------------------------------------------
# Assignment 06, Question 1
# ------------------------------------------------------------------------------

# 1) Assignment 4: Factors
def factors(n):
    lofactors = []
    for i in range (1, n+1):
        if n % i == 0:
            lofactors.append(i)
    return lofactors
        
        
# 2) Assignment 3: Third Character    
def new_word(s):
    if len(s) < 3:
        return s
    else:
        char = s[2]
        newword = ""
        for c in s:
            if c == char:
                newword = newword + "#"
            else:
                newword = newword + c
        return newword[:2] + char + newword[3:]