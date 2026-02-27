# Some questions will have the number of test cases on one line, 
# Then the stdin on another line. 
# We don't want to accidentally treat the first line (the test cases) as data.

import sys
import math
import string

# Read number of test cases from stdin.
# rstrip() removes trailing newline characters.
T_line = sys.stdin.readline().rstrip()

# Convert the test case count (T) to integer.
T = int(T_line)
print("Number of cases:", T)

# Loop exactly T times since the first line contains the test case count.
for i in range(T):

    # Read the next line from standard input.
    # Each test case is assumed to contain two integers separated by whitespace.
    line = sys.stdin.readline().rstrip()

    # Split the line into separate string tokens.
    parts = line.split()

    # Convert string tokens into integers using map().
    # map() is lazy, meaning conversion happens during iteration.
    a, b = map(int, parts)

    # Compute the required outputs.
    total = a + b
    product = a * b

    # Print results separated by a space (default print behavior).
    print("Total:",total, "Product:", product)

# -------------------------------
# Additional Conceptual Notes
# -------------------------------
# In competitive programming:
# - Programs should not prompt users.
# - Input is provided automatically by the judge.
# - Using sys.stdin.readline() is generally faster than input().
# - rstrip() is used to remove newline characters safely.
#
# This pattern is standard for problems where:
# - The number of test cases is given first.
# - Each test case is on its own line.

