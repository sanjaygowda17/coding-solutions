# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
columns = input()
Student = namedtuple('Student', columns)
sum = 0
for i in range(1, n+1):
    col1, col2, col3, col4 = input().split()
    student = Student(col1, col2, col3, col4)
    sum += int(student.MARKS)
avg = sum / n
print(f"{avg:.2f}")
