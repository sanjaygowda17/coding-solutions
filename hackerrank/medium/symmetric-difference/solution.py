# Enter your code here. Read input from STDIN. Print output to STDOUT
input() # size
a = set(map(int, input().split()))
input() # size
b = set(map(int, input().split()))
print(*sorted(a ^ b), sep="\n")
