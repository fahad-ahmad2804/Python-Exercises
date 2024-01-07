# Create a list of items that are sold in the cafe
menu = ["coffee", "tea", "sandwich", "juice", "water","cake"]

# Create a dictionary and declare the stock level of each menu item
stock = {"coffee" : 100, "tea" : 150, 
         "sandwich" : 35 , "juice" : 75, 
         "water" : 200, "cake" : 50}

# Create a dictionary and declare the price of each menu item
price = {"coffee" : 1.99, "tea" : 1.49, 
          "sandwich" : 2.99 , "juice" : 0.75, 
          "water" : 0.50, "cake" : 2.49}

# Create a variable to store the total value of all items & assign it the value 0
total = 0

print("The total value for each menu item is:\n")

# Create a for loop to iterate over each menu item
# Create a variable to store the calculation of each item * its price
for items in menu:
  value = round(stock[items] * price[items], 2)

# Print the total for each item  
  print(f"{items}: {value}")
  
# add the total of each item to the total variable
  total = total + value
print("")
print(f"The total value of all stock is: £{total}")