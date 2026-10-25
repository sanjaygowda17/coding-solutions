# String Formatting

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer, $n$, print the following values for each integer $i$ from $1$ to $n$:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

**Function Description**   

Complete the *print_formatted* function in the editor below.   

*print_formatted* has the following parameters:   

-	*int number:* the maximum value to print  

**Prints**   

The four values must be printed on a single line *in the order specified above* for each $i$ from $1$ to $number$. Each value should be space-padded to match the width of the *binary* value of $number$ and the values should be separated by a single space.

**Input Format**

A single integer denoting $n$.

**Constraints**

- $1 \le n \le 99$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T07:43:32.588Z  

```py
def print_formatted(number):
    # your code goes here
    bin_n = f'{number:b}'
    width = len(bin_n)+1 #width of the largest binary number + 1 space
    
    for i in range(1, n+1):
        print(f'{i}'.rjust(width-1), end = '') #first column will not have space
        print(f'{i:o}'.rjust(width), end = '') #:o for octal
        print(f'{i:X}'.rjust(width), end = '') #:X for hexadecimal
        print(f'{i:b}'.rjust(width)) #:b for binary



```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-string-formatting/problem)