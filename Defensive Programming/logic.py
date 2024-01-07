print("This program will convert cm to inches or inches to cm\n")

# user input will be converted to lower case, but this is uneccessary
selection = input("""Please enter either '1' for cm to inch or '2' for inch to cm:\n""").lower()
if selection == "1":
  print("")
  print("You have selected 'cm to inch'\n")
  cm = float(input("Please enter a measurement in cm:\n"))
  cm2inch = cm / 2.54
  print("")  
# variables are displayed the wrong way around
# another variable should be created to round the variable cm2inch to 2 decimal places  
  print(f"{cm2inch}cm in inches is {cm}")
elif selection == "2":
  print("")
  print("You have selected 'inch to cm'\n")
  inch = float(input("Please enter a measurement in inches:\n"))
# conversion formula is slightly incorrect (should be 2.54)
  inch2cm = inch * 2.55
  print("")  
# message is not accurate
# another variable should be created to round the variable inch2cm to 2 decimal places 
  print(f"{inch} in inches is {inch2cm}")
else:
  print("Invalid Input")