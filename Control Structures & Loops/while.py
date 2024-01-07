# Define a variable to store user input
# Prompt the user to enter a number, cast their input into an integer
# Define two variables:
# One to store the total/sum of the numbers entered
# Another to store the count of numbers entered
# Start a while loop with the condition 'user input != -1'
# Inside the while loop:
# Increment the total variable by the users input
# I.e. if the user inputs 3, increment total by 3
# Increment the count variable by 1
# Ask the user to enter a number, cast their input into an integer
# Define a variable to calculate the average based on the total and count
# Exclude the '-1' from the average calculation
# Print the average

number = int(input("Please enter a number: "))
total = 0
count = 0
while number != -1:
  total += number
  count += 1
  number = int(input("Please enter a number: "))
average = total / count
print("The average is:", average)