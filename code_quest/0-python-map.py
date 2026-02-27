# In Python, one of the most common functions you'll need to know for coding comps is map()
# map() iterates over each item in a list and turns it into a memory object.
# you have to convert it into a list() if you want to use it.

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
a, b = map(int, input("Enter two numbers separated by space: ").split())
# Read a line of input, split it into tokens, convert each to int, and unpack into a and b.

print("a =", a)
print("b =", b)
print("Sum =", a + b)
print("Product =", a * b)
# Display the parsed integers and simple computations.


print("\n--- Without map() ---")
# The following section performs the same task but without using map().

# Example input to type when prompted: 4 9
parts = input("Enter two numbers separated by space: ").split()
# Read a line of input and split it into a list of string tokens.

print("Split parts:", parts)
# Show the raw string tokens before conversion.

a = int(parts[0])
# Convert the first token in the list to an integer and assign it to a.

b = int(parts[1])
# Convert the second token in the list to an integer and assign it to b.

print("a =", a)
print("b =", b)
print("Sum =", a + b)
print("Product =", a * b)
# Display the parsed integers and simple computations again.

