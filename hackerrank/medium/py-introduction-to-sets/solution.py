def average(array):
    # your code goes here
    myset = set(arr)
    sum = 0
    for x in myset:
        sum+=x
    return f"{(sum/len(myset)):1.3f}"
