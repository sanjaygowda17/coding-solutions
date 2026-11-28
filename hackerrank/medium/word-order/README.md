# Word Order

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given $n$ words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

**Note:** Each input line ends with a **"\n"** character.

**Constraints:**  
$1\le n\le 10^5$  
The sum of the lengths of all the words do not exceed $10^6$  
All the words are composed of lowercase English letters only.

**Input Format**

The first line contains the integer, $n$.  
The next $n$ lines each contain a word. 

**Output Format**

Output $2$ lines.  
On the first line, output the number of distinct words from the input.  
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-28T08:10:56.836Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    string = input()
    d[string] = d.get(string, 0) + 1
print(len(d), ' '.join(map(str,(d.values()))), sep = '\n')

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/word-order/problem)