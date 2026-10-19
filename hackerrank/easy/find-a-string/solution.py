def count_substring(string, sub_string):
    count = i = 0
    while i < len(string):
        i = string.find(sub_string, i)
        if i < 0: break
        count += 1
        i += 1
    return count
