
string = "I am learning to code in Python"

# Create an empty list to store modified characters
char = []

# Loop through each character in the string
for index in range(len(string)):
# If the indexed location is an even number
# Append the character to the empty list and change it to uppercase
  if index % 2 == 0:
      char.append(string[index].upper())

# If the indexed location is an odd number
# Append the character to the empty list and change it to lowercase
  else:
    char.append(string[index].lower())

#Join the list into a string and print
print("".join(char))

# Split the string into a list of substrings
# Create a new empty list to store modified substrings
new_string = string.split()
word = []

# Loop through each substring in the list
for index in range(len(new_string)):
# If the indexed location is an even number
# Append the substring to the empty list and change it to uppercase
  if index % 2 == 0:
    word.append(new_string[index].upper())
# If the indexed location is an odd number
# Append the substring to the empty list and change it to lowercase
  else:
    word.append(new_string[index].lower())

#Join the list into a string and print
print(" ".join(word))