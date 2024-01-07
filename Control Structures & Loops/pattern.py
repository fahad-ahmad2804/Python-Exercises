# Declare a variable to store "*"
# Start a for loop with an iterating variable (i)
# Assign i the range 1, 10 for the loop to iterate through
# Nest within the for loop an if statement with the condition i <= 4
# Print the variable that contains "*"
# Define a condition where "*" is then incremented to itself + "*"
# Define an else condition/statement
# Print the variable with the stored symbol again
# By this point it should contain 5 instances of "*"
# Now that i is more than 4:
# Define a new condition where char is now sliced from right to left
# Begin from index 4, end at 0 and decrement by 1

char = "*"
for i in range(1, 10):
  if i <= 4:
    print (char)
    char = char + ("*")
  else:
    print(char)
    char = char[4:0:-1]