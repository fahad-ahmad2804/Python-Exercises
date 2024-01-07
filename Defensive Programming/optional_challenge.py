string = input("Please enter some text: ")
reverse = ""

# Runtime Error:
# Calling a function that does not exist ("length")
count = length(string)

# Logical Error:
# this line will work but results will not be as expected
while count > 1:
    
# Syntax Error: IndentationError
reverse += string[count - 1] 
  count = count - 1

# Syntax Error: missing parenthesis
print f"The string reversed is: {reverse}"