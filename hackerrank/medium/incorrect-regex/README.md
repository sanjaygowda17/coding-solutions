# Incorrect Regex

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string $S$.  
Your task is to find out whether $S$ is a valid [regex](https://en.wikipedia.org/wiki/Regular_expression) or not.

**Input Format**

The first line contains integer $T$, the number of test cases.  
The next $T$ lines contains the string $S$.

__Constraints__

$0 < T < 100$

**Output Format**

Print "True" or "False" for each test case without quotes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-24T10:09:45.964Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(raw_input())):
    try:
        re.compile(raw_input())
        print(True)
    except re.error:
        print(False)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/incorrect-regex/problem)