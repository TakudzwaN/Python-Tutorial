country = input("Enter name of your country: ")
if country.lower() == "canada":
    print("You must be friendly!")
else:
    print("Hopefully you are friendly!")

    # Note comparing strings is case sensitive, so we need to call the lower() method to convert the user input to lowercase. 