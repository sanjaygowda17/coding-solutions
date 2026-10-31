def merge_the_tools(string, k):
    # your code goes here
    j = 0
    while j < len(string):
        substring = ""
        for char in string[j : j+k]:
            if char not in substring:
                substring += char
        print(substring)
        j += k   
