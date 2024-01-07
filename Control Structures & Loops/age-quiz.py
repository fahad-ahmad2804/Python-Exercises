#use input() to prompt user to provide their age
#store their input into a variable called "age"
#convert their input into an integer
#use a nested if & elif structure to evaluate the users input
#use a combination of comparison operators to judge which message to display
#order the nested if statements in descending order of age

#criterion:
#if the user enters a number higher than 100:
#output message = "Sorry, you're dead."

#if user is =>65:
#output message = "Enjoy your retirement!"

#if user is 40 or over:
#output message = "You're over the hill."

#if user is exactly 21:
#output message = "Congrats on your 21st!"

#if user is <13:
#output message = "You qualify for the kiddie discount."

#for any other age:
#output message = "Age is but a number."

age = input("Please enter your age: ")
age = int(age)

if age > 100:
  print("Sorry, you're dead.")
elif age >= 65:
  print("Enjoy your retirement!")
elif age >= 40:
  print("You're over the hill.")
elif age == 21:
  print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
  print("Age is but a number.")