# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["banana", "apple", "strawberry", "cherry", "tomato"]
# TODO: Use a for loop to print each fruit in the list
for fruits in fruits:
    print(fruits)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
    print(count)    
    count -= 1
    

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for num in range(1, 11):
    print(num ** 2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

# TODO: Create a list of colors
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

# TODO: Use a for loop to select and print 3 random colors from the list
for i in range(3):
    print(any.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module


# TODO: Import the custom module and use its functions
print("math_operations.".add(10, 5))
print("math_operations".subtract(10, 5))
print("math_operations".multiply(10, 5))
print("math_operations".divide(10, 5))


# TODO: Use a while loop to create a simple calculator
