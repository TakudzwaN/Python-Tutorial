# String Declaration
# name = "Takudzwa"
# lastName = "N"

# # Combine Strings With '+' sign 
# print("Hello" + " " + name + " " + lastName)

# Example
# name = input("What is your Name? ")
# lastName = input("What is your Last Name? ")
# print("Hello, " +  name + " " + lastName)

# Formatting Strings
name = "Takudzwa"
lastName = "N"

# output = "Hello, " +  name + " " + lastName
# output = "Hello, {} {}".format(name, lastName)
# output = "Hello, {0} {1}".format(name, lastName)
output = f"Hello, {name} {lastName}"    # only available in python 3
print(output)


# String Functions
# converts value of name variable to upper case
# print(name.upper()) 

# converts value of name variable to lower case
# print(name.lower())      

# capitalizes the first letter of a word
# print(name.capitalize()) 

# counts how many times 'a' appears in name variable
# print(name.count("a"))   