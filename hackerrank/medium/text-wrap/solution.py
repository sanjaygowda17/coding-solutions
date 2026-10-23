

def wrap(string, max_width):
    new_string_list =[]
    for i in range(len(string)//max_width +1):
        new_string_list.append(string[i*max_width : (i+1)*max_width])
    return '\n'.join(new_string_list)

