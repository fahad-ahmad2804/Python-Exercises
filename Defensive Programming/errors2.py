# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Runtime Error: NameError
# Error description: Expression 'Lion' has not been defined correctly
# Correction: Expression 'Lion' has been encased in quotation marks
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Logical Error: Flawed logic
# Error description: The below line of code will print the characters 
# between the quotation marks verbatim
# Correction: String has been encased in parenthesis
# String has been transformed to an f-string

# Logical Error: Flawed logic
# The below line of code will print an illogical/nonsensical string
# Correction: Variables 'animal_type' and 'number_of_teeth' have been switched
full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")

# SyntaxError: Missing parentheses
# Error description: Missing parentheses when calling the print function
# Correction: parenthesis added to each side of the new line expression
print(full_spec)