#create a variable called string
#store the provided sentence within the created variable
#using the replace() function, print the string but replace every instance of "!"
#with a blank space
#using the upper() function, print the string in upper case & with blank spaces
#using extended slice, reprint the sentence in reverse

string = "The!quick!brown!fox!jumps!over!the!lazy!dog.!"
print(string.replace("!"," "))
string = string.upper()
print(string.replace("!"," "))
print(string[::-1])