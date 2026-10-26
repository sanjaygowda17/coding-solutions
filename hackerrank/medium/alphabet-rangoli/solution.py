def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet[:size] 
    letters = letters[::-1] + letters[1:] 
    m = len("-".join(letters)) 
    newlist = ""
    result = ""
    for i in range(size):
        if i < 1:
            result += letters[i].center(m, "-") + "\n"
            newlist += letters[i]
        else:
            result += "-".join(newlist + letters[i] + newlist[::-1]).center(m, "-") + "\n"
            newlist += letters[i]
        
    newlist = newlist[:-1]
    
    for i in range(size-2, -1, -1):
        if i < 1:
            result += letters[i].center(m, "-")
        else:
            newlist = newlist[:-1]
            result += "-".join(newlist + letters[i] + newlist[::-1]).center(m, "-") + "\n"
            
    print(result)
