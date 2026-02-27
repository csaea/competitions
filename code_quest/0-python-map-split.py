# In Python, two of the most common functions you'll need to know for coding comps is map() and split()

# map() iterates over each item in a list and turns it into a memory object.
# you have to convert it into a list with list() if you want to use it.

# split() separates all the parts of a single line, so you can use them separately. 

numbers = ["1", "2", "3"]
print("Original list:", numbers)

result = map(int, numbers)
# Apply the int() function to each element in numbers, producing a "lazy" map object, stored in memory.

print("Map object:", result)
# Show that result is a map object (an iterator), not yet a list.

converted = list(result)
# Force evaluation of the map object by converting it into a list of integers.

print("After converting map to list:", converted)
# Display the fully evaluated list of integers.

print("\n--- Using map() with input ---")
# Demonstrate converting user input using map().

# Example input to type when prompted: 3 7
user_input = input("Enter two numbers separated by space: ")
split_user_input = user_input.split()
print(split_user_input)

a, b = map(int, split_user_input)
# Read a line of input, split it into tokens, convert each to int, and unpack into a and b.

print("a =", a)
print("b =", b)
print("Sum =", a + b)
print("Product =", a * b)