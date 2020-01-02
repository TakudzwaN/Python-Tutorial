# Using if Statements
# province = input("Which province do you live in ?: ")
# tax = 0

# if province == "Manicaland":
#     tax = 0.05
# if province == "Matebeleland":
#     tax = 0.05
# if province == "Masvingo":
#     tax = 0.25
# print(tax)

################################################################################################

# Using elif, this treats the evaluation like one if statement with different conditions
# province = input("Which province do you live in ?: ")
# tax = 0

# if province == "Manicaland":
#     tax = 0.05
# elif province == "Matebeleland":
#     tax == 0.05
# elif province == "Masvingo":
#     tax = 0.25
# else:
#      tax = 0.15
# print(tax)

################################################################################################

# Using elif and or
# province = input("Which province do you live in ?: ")
# tax = 0

# if province == "Manicaland" or province == "Matebeleland":
#     tax = 0.05
# elif province == "Masvingo":
#     tax = 0.25
# else:
#      tax = 0.15
# print(tax)

################################################################################################

# Using elif and in
province = input("Which province do you live in ?: ")
tax = 0

if province == in("Manicaland", "Matebeleland", "Mashonaland"):
    tax = 0.05
elif province == "Masvingo":
    tax = 0.25
else:
     tax = 0.15
print(tax)