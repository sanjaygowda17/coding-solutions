# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, size = input().split()
print(
    '\n'.join(
    ''.join(i) for i in combinations_with_replacement(sorted(string), int(size))
    )
)
