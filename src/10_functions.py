# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def isEven(n):
    return n % 2 == 0

print('Input 2, expected TRUE:', isEven(2))
print('Input 3, expected FALSE:', isEven(3))
print('Input 2468, expected TRUE:', isEven(2648))
print('Input 1351, expected FALSE:', isEven(1351))

# Read a number from the keyboard
# num = input("4")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
def evenOrOdd(n):
    if (n % 2 == 0): 
        return "Even!" 
    else: 
        return "Odd!"

print(evenOrOdd(2))
print(evenOrOdd(5))

