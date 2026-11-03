# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S = input().split()
result = list(permutations(sorted(S[0]), int(S[-1])))
result = ["".join(i) for i in result]
for i in result:
    print(i)
