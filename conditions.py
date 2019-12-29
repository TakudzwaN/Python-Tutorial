price = input("How much did you pay?: ")
price = float(price)

if price >=1.00:
    tax = 0.7
else:
    tax = 0
print("Tax on amount paid is: " + str(tax))