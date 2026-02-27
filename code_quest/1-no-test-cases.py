# one of the first challenges of any coding competition is HOW TO DEAL WITH THE INPUT. 
# there are two types: questions without any test cases, and questions with a certain number of test cases.

# example problem with *no test cases*
# input will be two integers, separated by a whitespace, such as: 
# 5 2
# your program should output two more integers: the sum and the product, such as:
# 7 105 2

import sys
import math
import string

# First, iterate over every line in standard input until End of File (EOF).
for line in sys.stdin:
    # Remove trailing newline and extra whitespace.
    line = line.rstrip()

    # Skip empty lines defensively.
    if not line:
        continue

    # Split the line into tokens and convert them to integers. REMEMBER: stdin defaults to strings so we neet to convert them to integers
    a, b = map(int, line.split())

    # Compute required values.
    total = a + b
    product = a * b

    # Output results exactly as required.
    print(total, product)