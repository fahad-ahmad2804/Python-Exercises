## This example program is meant to demonstrate errors.
 
## There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# SyntaxError: Missing parentheses
# Error description: Missing parentheses when calling the print function
# Correction: parenthesis added to each side of the string
print("Welcome to the error program")
    
# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the print function

# SyntaxError: Missing parentheses
# Error description: Missing parentheses when calling the print function
# Correction: parenthesis added to each side of the new line expression
print ("\n")

## Variables declaring the user's age, casting the str to an int, and printing the result
    
# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the variable 'age_Str'

# Runtime Error: NameError
# Error description: Variable 'age_Str' has not been defined correctly
# (equal to comparison operator has been used instead of the equals assignment operator)
# Correction: x1 equals symbol has been removed from the line
age_Str = "24"

# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the variable 'age'

# Runtime Error: ValueError
# Variable 'age_Str' cannot be converted to an integer
# Correction: the characters ' years old' has been removed from the variable 'age_Str'
age = int(age_Str)

# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the print function

# Runtime Error: TypeError
# Error description: the variable 'age' is an integer and cannot be concatenated to a string
# Correction: string has been transformed to an f-string
# Variable 'age' has been enclosed in curly braces
# '+' operator has been removed
# Another correction could have been to use the 'age_Str' variable instead
# without initially removing 'years old' from the variable but from the below string
# I.e print("I'm " + age_Str + ".")
print(f"I'm {age} years old.")

## Variables declaring additional years and printing the total years of age

# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the variable 'years_from_now'
years_from_now = 3

# Syntax Error: IndentationError
# Error description: Unexpected indent
# Correction: all indentation removed from the variable 'total_years'

# Runtime Error: TypeError
# Error description: the variable 'years_from_now' is a string and cannot be concatenated to an integer
# Correction: variable 'years_from_now' has been changed to an int by removing the quotation marks
total_years = age + years_from_now

# SyntaxError: Missing parentheses
# Error description: Missing parentheses when calling the print function
# Correction: parenthesis added to each side of the string, space removed after 'print'

# Logical Error: Flawed logic
# The below line of code:
# print("The total number of years:" + "answer_years")
# Will print an illogical/nonsensical string
# Correction: String "answer_years" replaced with variable 'total_years'
# Argument within the parenthesis has been changed to an fstring, space added after colon
# String "The total number of years:" changed to add a little more context
print(f"In 3 years, I will be: {total_years}")

## Variable to calculate the total amount of months from the total amount of years and printing the result

# Runtime Error: NameError
# Error description: variable 'total' has not been defined correctly
# Correct: variable 'total' has been replaced with the already defined variable 'total_years'

# Logical Error: Flawed logic
# The below line of code will not produce the desired outcome
# Correction: '+ 6' has been added to the end of the calculation
total_months = total_years * 12 + 6

# SyntaxError
# Error description: Missing parentheses when calling the print function
# Correction: parenthesis added to each side of the string

# Runtime Error: TypeError
# Error description: the variable 'total_months' is an integer and cannot be concatenated to a string
# Correction: string has been transformed to an f-string
# the 'total_months' variable has been enclosed in curly braces
# '+' operator has been removed
print (f"In 3 years and 6 months, I'll be {total_months} months old")

##HINT, 330 months is the correct answer