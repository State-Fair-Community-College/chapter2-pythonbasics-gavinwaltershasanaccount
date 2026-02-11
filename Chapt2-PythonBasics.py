# --------------------------------------------
# Name:Gavin Walters
# Date: 02/10/2026
# Program: Chapter 2 Practice
# Description: Practice Program Building for Chapter 2
# Complete each section by following the
# directions in the comments.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Variables and print
# ------------------------------------------------
# TODO:
# 1. Create a variable named name
# 2. Store your name as a string in the variable
# 3. Use print() to display: Hello, <name>

name='placeholder' # placeholder definition of the variable named name

name=input('What is your name? ') # input used to redifine the value of the variable name

print('Hello,', name)  # blank line for readability


# ------------------------------------------------
# Practice 2: Input and output
# ------------------------------------------------
# TODO:
# 1. Ask the user to enter their favorite color
# 2. Store the input in a variable
# 3. Print a sentence that includes the color

favorite_color=input('What is your favorite color? ')

print('Oh, so your favorite color is', favorite_color, 'huh?')


# ------------------------------------------------
# Practice 3: Adding two numbers
# ------------------------------------------------
# TODO:
# 1. Ask the user for a number
# 2. Convert the input to an integer
# 3. Ask the user for a second number
# 4. Convert the input to an integer
# 5. Add the two numbers together
# 6. Print the total

number1=int(input('What is your first number? ')) # obtains the user's first number

number2=int(input('What is your second number? ')) # obtains the user's second number

total_number=number1 + number2 # calculates the users total

print('Your total is ', total_number) # prints the users final total number


# ------------------------------------------------
# Practice 4: Calculations with variables
# ------------------------------------------------
# TODO:
# 1. Ask the user for the price of an item
# 2. Convert the input to a float
# 3. Create a variable for the tax rate (use 0.08)
# 4. Calculate the tax amount
# 5. Calculate the final price
# 6. Print the final price

item_price=float(input('What is the items price? '))

tax_rate=float(0.08)

item_tax=item_price * tax_rate

final_price=item_price + item_tax

print('Your final price is ', final_price)


# ------------------------------------------------
# Practice 5: Formatted output with f-strings
# ------------------------------------------------
# TODO:
# 1. Ask the user how many hours they worked
# 2. Ask the user for their hourly pay
# 3. Convert both inputs to floats
# 4. Calculate weekly pay
# 5. Use an f-string to display the result
#    (Round to 2 decimal places)

hours=int(input('How many hours did you work? ')) # the user is asked how many hours they worked

hourly_pay=float(input('What is your hourly pay? ')) # the user is asked for their hourly pay

weekly_pay=hours*hourly_pay # the user's amount of hours worked is multiplied by their hourly pay to create their weekly pay

print(f'Your weekly pay is {weekly_pay:.2f}.') # the user's weekly pay is outputted rounded down to 2 digits