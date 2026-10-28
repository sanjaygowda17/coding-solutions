

# Complete the solve function below.
def solve(s):
    s_formatted =s[0].upper()
    previus_letter=s[0]
    for i in range(1,len(s)):
        if previus_letter==' ' and s[i]!=' ':
            s_formatted+=s[i].upper()
            previus_letter=s[i]
        else :
            s_formatted+=s[i]
            previus_letter=s[i]
    return s_formatted
