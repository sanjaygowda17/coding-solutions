def swap_case(s):
    string = list(s)
    for n in range(len(string)):
        if string[n].islower():
            string[n] = string[n].upper()
        else:
            string[n] = string[n].lower()
    return "".join(string)
