# good practice to always import these:
import sys
import math
import string

# In competitive programming, input comes from standard input (stdin),
# not from interactive prompts like we've been doing in class.

# map() applies a function to each item in an iterable.
# It returns an iterator (a lazy object) which MUST be converted to a list() to use properly.
# split() separates a single string by whitespace, so you can use each part separately.

numbers = ["1", "2", "3"]
print("Original list of strings:", numbers)

# Use map() as a quick way to iterate the list and convert strings to numbers: 
# map() takes 2 arguement to apply int to each string in the list.
result = map(int, numbers)

# This creates a map object.
print("Map object:", result)
# The map object returns only a memory location id. It must be convereted to a string.

converted = list(result)
# Converting forces evaluation of the iterator.

print("After converting map to list:", converted)


print("\n--- Using standard input ---")
# Read one line from standard input with readline() and rstrip() cleans up special characters like \n and \r and spaces.
# Example expected input line:
# 3 7
line = sys.stdin.readline().rstrip()
print("Before split", line)
# split() separates the line into string tokens.
split_line = line.split()
print("After split():", split_line)

# map(int, ...) converts each token into an integer.
a, b = map(int, split_line)

print("a =", a)
print("b =", b)
