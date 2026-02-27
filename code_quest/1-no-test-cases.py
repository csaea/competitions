# one of the first challenges of any coding competition is HOW TO DEAL WITH THE INPUT. 
# there are two types: questions without any test cases, and questions with a certain number of test cases.

# example problem with *no test cases*
# input will be two integers, separated by a whitespace, such as: 
# 5 2
# your program should output two more integers: the sum and the product, such as:
# 7 105 2

import sys

# sys.stdin allows iteration over all input lines.
for line in sys.stdin:
# .strip() removes trailing newline characters.
    line = line.strip()

# .split() separates values by whitespace.
# map(int, ...) converts strings to integers.
    a, b = map(int, line.split())
    
    total = a + b
    product = a * b
    
    print(total, product)

