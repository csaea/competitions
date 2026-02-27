# Some questions will have the number of test cases on one line, 
# Then the stdin on another line. 
# We don't want to accidentally treat the first line (the test cases) as data, so:

T = int(input())

# the _ is just a variable name, usually 'i' is used, but we aren't actually using 'i' in the loop, so the convention is to use _.
for _ in range(T):
    a, b = map(int, input().split())
    print(a + b, a * b)