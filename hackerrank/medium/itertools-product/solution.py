# Enter your code here. Read input from STDIN.
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = list(product(a, b))

for i in result:
    print(i, end= " ")
