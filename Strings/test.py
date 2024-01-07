'''
write a program that reads a string and makes each alternate character uppercase
and each other alternate character lower case

e.g. Hello World will become HeLlO WoRlD

do similar for a string but with alternating words

e.g. I am learning to code would become i AM learning TO code

tip: using the split() and join() functions will help

'''

string = "I am learning to code"
new_string = []

# what does this line do/mean?
# variable is being declared as a boolean?
# true is equal to 1 and false is equal to 0
# if the variable is true, then the code will run - ai wrote/suggested this line
lower = True

for letter in string:

# what does this line do/mean?
  # if letter in string is true?
    if lower:
        new_string.append(letter.lower())

# what does this line do/mean?
        lower = False
    else:
        new_string.append(letter.upper())
        lower = True
print("".join(new_string))

















# def alternate_case_upper(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result += str[i].lower()
#         else:
#             result += str[i].upper()
#     return result




# s = "hello world"
# #empty string is initialized with an join() function 
# #it returns the lowercase of the string when it is even
# new_s = ''.join([s[a].lower() 
# if a % 2 == 0 
# else 
# #it returns the uppercase of the string when it is odd
# s[a].upper() 
# #for loop is used to iterate through the loop along with the range of the length of list
# for a in range(len(s))])
# #return the string after converting it into another case
# print(new_s)

